import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, PASS_MARK, MAX_MISTAKE, RED, AMBER, GREEN, GRAY, LIGHT_GRAY, COMBOCOLOR1, COMBOCOLOR2, FONTPATH, TRANSITION_TIME, REWARD_MAP, GENS, SUPER_FAST_THRESHOLD, FAST_THRESHOLD, NOT_SHOW_NAME_TIME
from kanji import Hanja
import random
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

SPAWN_POKEMON_EVENT = pygame.USEREVENT + 1
MESSAGE_CLEAR_EVENT = pygame.USEREVENT + 2
WALK_EVENT = pygame.USEREVENT + 3
JIGGLE_EVENT = pygame.USEREVENT + 4
SPECIAL_MESSAGE_CLEAR_EVENT = pygame.USEREVENT + 5
TRANSITION_END_EVENT = pygame.USEREVENT + 6

class GameSession:
    PAUSE_OPTIONS = ["Resume", "Restart", "End Game"]
    END_OPTIONS = ["Restart", "Quit"]

    def __init__(self, data, screen, font, large_font):
        self.screen = screen
        self.font = font
        self.large_font = large_font
        self.reset_game(data)
        
    def reset_game(self, data):
        self.hanja_data = data
        self.elapsed_time = 0
        self.game_paused = False
        self.selected_pause_option = 0
        self.transitioning = False
        self.game_ended = False
        self.selected_end_option = 0
        self.paused_time_start = 0
        self.total_paused_time = 0
        self.caught_pokemon_count = 0
        self.combo_count = 0
        self.mistake_count = 0
        self.total_mistake_count = 0
        self.total_score = 0
        self.current_pokemon = None
        self.typed_name = ""
        self.animation_start_time = 0
        self.current_animating_char = ''
        self.is_correct = False
        self.start_time = pygame.time.get_ticks()
        self.keystroke_sound = pygame.mixer.Sound(resource_path('assets/clack.wav'))
        self.messages = []
        self.special_message = {"text": "", "start_time": pygame.time.get_ticks()}
        self.jiggle_offset = [0, 0]
        self.ball_sprite = None
        self.premier_ball_sprite = self.load_and_scale_sprite("assets/premier-ball.png")
        self.dive_ball_sprite = self.load_and_scale_sprite("assets/dive-ball.png")
        self.dusk_ball_sprite = self.load_and_scale_sprite("assets/dusk-ball.png")
        self.combo_sprite = self.load_and_scale_sprite("assets/pearl.png")
        self.score_sprite = self.load_and_scale_sprite("assets/fire-gem.png")
        self.mistake_sprite = self.load_and_scale_sprite("assets/charcoal.png")
        self.halo_effect = self.load_and_scale_sprite("assets/dawn-stone.png")  # Load halo effect sprite
        self.animation_state = "IDLE"  # Track the state of the animation
        self.ball_position = [0, 0]  # Initial ball position
        self.ball_target = [0, 0]  # Target position for the ball
        self.ball_start = [0, 0]  # Start position for the ball
        self.halo_visible = False
        self.halo_timer = 0
        self.caught_pokemons = []
        self.combo_indices = []
        self.reward_map = REWARD_MAP
        self.current_generation = 0
        self.current_level = 1
        self.level_reached = self.current_level
        self.bg_image = pygame.image.load(resource_path(f"assets/Rock Garden.jpg"))
        self.caught_pokemon_surface = None
        self.should_update_caught_pokemon_surface = True
        pygame.mixer.music.load(resource_path(f"assets/Main.mp3"))
        self.start_transition()

    def load_and_scale_sprite(self, path):
        return pygame.transform.scale(pygame.image.load(resource_path(path)), (30, 30))

    def change_generation(self, new_generation):
        self.bg_image = pygame.image.load(resource_path(f"assets/{GENS[new_generation]['bg']}"))
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(resource_path(f"assets/{GENS[new_generation]['music']}"))
        '''if new_generation > self.current_generation:
            self.add_message(f"Excellent! {GENS[new_generation]['name']} unlocked!", 5000)
            self.max_region_reached = GENS[new_generation]['name']
        if new_generation == self.current_generation:
            self.add_message(f"Stay in {GENS[self.current_generation]['name']}.", 5000)
        if new_generation < self.current_generation:
            self.add_message(f"Move back to in {GENS[new_generation]['name']}.", 5000)'''
        self.current_generation = new_generation
        self.start_transition()

    def start_transition(self):
        self.pause_game(pygame.time.get_ticks(), False)
        pygame.mixer.music.play()
        pygame.time.set_timer(TRANSITION_END_EVENT, TRANSITION_TIME, True)

    def display_region_transition(self):
        self.screen.blit(self.bg_image, (0, 0))
        # Create a semi-transparent overlay
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((50, 50, 50, 200))  # Grey with 200 alpha for transparency
        self.screen.blit(overlay, (0, 0))

        # Prepare the welcome message
        message = "Welcome to Grade!"

        x = SCREEN_WIDTH // 2 - self.font.size(message)[0] // 2
        y = SCREEN_HEIGHT // 2

        self.draw_text(self.screen, message, self.font, BLACK, x, y, outline_color = WHITE, outline_thickness = 1)

    def update_time(self, time):
        if not self.game_paused:
            self.elapsed_time = time - self.start_time - self.total_paused_time
            if self.current_pokemon:
                self.current_pokemon.elapsed_time = time - self.current_pokemon.start_time - self.current_pokemon.total_paused_time

    def get_combo_reward(self, combo_count):
        return self.reward_map.get(combo_count, 500*(combo_count-14))
    
    def get_speed_multiplier(self, elapsed_time, time_limit):
        percentage = elapsed_time / time_limit
        if percentage <= SUPER_FAST_THRESHOLD : # 0.35
            return 1.5
        elif percentage <= FAST_THRESHOLD : # 0.55
            return 1.2
        else:
            return 1.0

    def check_progress(self):
        if self.caught_pokemon_count >=50:
                self.end_game()
        elif not self.current_level * 10 > self.caught_pokemon_count:
            if self.caught_pokemon_count and self.caught_pokemon_count % 10 == 0:
                legend_or_fast = np.array([x[2] for x in self.caught_pokemons[-10:]]).sum()
                legend_or_fast += np.array([x[1] for x in self.caught_pokemons[-10:]]).sum() / 2
                if (legend_or_fast >= PASS_MARK) and (self.mistake_count <= MAX_MISTAKE):
                    self.change_generation(self.current_generation + 1)
                if (legend_or_fast < PASS_MARK/2) or (self.mistake_count > 2* MAX_MISTAKE):
                    self.change_generation(max(0, self.current_generation - 1))
                else:
                    self.change_generation(self.current_generation)
                self.current_level += 1
                self.mistake_count = 0
        else:
            self.spawn_pokemon()
            
    def add_message(self, text, howlong=1000):
        self.messages.append({"text": text, "start_time": pygame.time.get_ticks()})
        pygame.time.set_timer(MESSAGE_CLEAR_EVENT, howlong, True)

    def add_special_message(self, text, howlong=1000):
        self.special_message["text"] = text
        self.special_message["start_time"] = pygame.time.get_ticks()
        pygame.time.set_timer(SPECIAL_MESSAGE_CLEAR_EVENT, howlong, True)
        
    def display_special_message(self, screen, font, color, width, height):
        self.draw_text(screen, self.special_message["text"], font, color, (width - font.size(self.special_message["text"])[0] - 50) // 2, 70)

    def display_messages(self, screen, font, color, width):
        for i, message in enumerate(self.messages[:]):
            self.draw_text(screen, message["text"], font, color, width - font.size(message["text"])[0] - 50, 50 + i * 50)

    def spawn_pokemon(self):
        hanja_data_choice = random.choice(self.hanja_data[GENS[self.current_generation]["indices"][0]:GENS[self.current_generation]["indices"][1]])
        self.current_pokemon = Hanja(hanja_data_choice, self.font)
        self.caught_pokemon = None
        self.typed_name = ""
        
    def start_capture_animation(self):
        self.animation_state = "PARABOLIC"
        self.ball_start = [SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT - 50]  # Starting from the center bottom
        self.ball_position = list(self.ball_start)
        self.ball_target = list(self.current_pokemon.current_position)  # Current Pokémon position
        self.halo_visible = False
        self.halo_timer = 0
        
    def pokemon_caught(self, elapsed_time):
        self.current_pokemon.is_caught = True
        self.current_pokemon.caught_time = elapsed_time
        self.caught_pokemon_count += 1
        self.combo_count += 1       

        # Calculate score
        base_score = self.get_combo_reward(self.combo_count)
        speed_multiplier = self.get_speed_multiplier(elapsed_time, self.current_pokemon.time_limit)
        score = base_score * speed_multiplier
        self.total_score += score
        self.current_pokemon.is_fast = speed_multiplier == 1.2
        self.current_pokemon.is_super_fast = speed_multiplier == 1.5
        
        # Start capture animation
        if self.current_pokemon.is_super_fast:
            self.ball_sprite = self.premier_ball_sprite
        elif self.current_pokemon.is_fast:
            self.ball_sprite = self.dive_ball_sprite
        else:
            self.ball_sprite = self.dusk_ball_sprite
        
        # Add messages
        self.add_message(f"{self.current_pokemon.hanja} caught!")
        if speed_multiplier == 1.5:
            self.add_special_message(f"{round(base_score)} x 1.5")
        elif speed_multiplier == 1.2:
            self.add_special_message(f"{round(base_score)} x 1.2")
        else:
            self.add_special_message(f"{round(base_score)}")
        if self.combo_count > 3:
            self.add_message(f"Combo {self.combo_count}!")
        
        self.caught_pokemon = self.current_pokemon.copy()
        
        # Add to caught Pokémon list
        self.caught_pokemons.append((self.caught_pokemon.icon,
                                            self.caught_pokemon.is_fast, 
                                            self.caught_pokemon.is_super_fast))
        self.should_update_caught_pokemon_surface = True
        self.start_capture_animation()
        
        pygame.time.set_timer(SPAWN_POKEMON_EVENT, 1000, True)

    def pokemon_missed(self, wait_time_ms):
        self.add_message("Missed!")
        if self.combo_count >= 3:
            self.combo_indices.append((len(self.caught_pokemons) - self.combo_count, len(self.caught_pokemons)))
        self.combo_count = 0
        self.mistake_count += 1
        self.total_mistake_count += 1
        self.current_pokemon = None
        pygame.time.set_timer(SPAWN_POKEMON_EVENT, wait_time_ms, True)
        
    def draw_pause_menu(self, screen, font):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(GRAY)
        overlay.set_alpha(150)  # Set transparency to 150
        screen.blit(overlay, (0, 0))

        # Draw pause menu options
        menu_rect = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50, 250, 150)
        self.draw_rounded_rect(screen, menu_rect, WHITE, radius=15, outline_color=BLACK)

        for i, option in enumerate(GameSession.PAUSE_OPTIONS):
            color = GREEN if i == self.selected_pause_option else BLACK
            self.draw_text(screen, option, font, color, menu_rect.x + 50, menu_rect.y + 20 + i * 30)
            
        self.draw_caught_pokemon_icons(screen)
    
    def pause_game(self, current_time, pause_music = True):
        self.paused_time_start = current_time
        if pause_music == True:
            pygame.mixer.music.pause()
            self.game_paused = True
        else:
            self.transitioning = True
    
    def unpause_game(self, current_time, pause_music = True):
        if pause_music == True:
            self.total_paused_time += current_time - self.paused_time_start
            if self.current_pokemon:
                self.current_pokemon.total_paused_time += current_time - self.paused_time_start
            pygame.mixer.music.unpause()
            self.game_paused = False
        else:
            self.transitioning = False
            
    def end_game(self):
        if self.combo_count >= 3:
            self.combo_indices.append((len(self.caught_pokemons) - self.combo_count, len(self.caught_pokemons)))
        self.current_pokemon = None
        self.game_ended = True
        pygame.mixer.music.stop()
        pygame.mixer.music.unload()
        pygame.mixer.music.load(resource_path(f"assets/Results.mp3"))
        pygame.mixer.music.play()
        
    def handle_pause_menu_input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_pause_option = (self.selected_pause_option - 1) % len(GameSession.PAUSE_OPTIONS)
            elif event.key == pygame.K_DOWN:
                self.selected_pause_option = (self.selected_pause_option + 1) % len(GameSession.PAUSE_OPTIONS)
            elif event.key == pygame.K_RETURN:
                if GameSession.PAUSE_OPTIONS[self.selected_pause_option] == "Resume":
                    self.unpause_game(pygame.time.get_ticks())
                elif GameSession.PAUSE_OPTIONS[self.selected_pause_option] == "Restart":
                    self.reset_game(self.hanja_data)
                elif GameSession.PAUSE_OPTIONS[self.selected_pause_option] == "End Game":
                    self.end_game()
                    
    def animate_last_letter(self, char):
        """
        Set up the animation for the last typed letter.
        """
        self.animation_start_time = pygame.time.get_ticks()
        self.current_animating_char = char
        self.is_correct = self.current_pokemon.name.startswith(self.typed_name)
        self.keystroke_sound.play()
        
    def animate_letter_appearance(self, screen, font, x, y, animation_duration=200):
        """
        Animate the appearance of the last typed letter with a "boom" effect.
        - animation_duration: Total duration of the animation (in milliseconds).
        """
        elapsed = pygame.time.get_ticks() - self.animation_start_time
        if elapsed > animation_duration:
            if self.is_correct:
                # At the end of animation, correct letters stay as red
                text_surface = font.render(self.current_animating_char, True, RED)
                screen.blit(text_surface, (x, y))
            return  # Animation completed, no need to draw

        # Calculate the scale factor based on elapsed time
        half_duration = animation_duration / 2
        if elapsed <= half_duration:
            # Growing phase
            scale = 1.0 + (0.5 * (elapsed / half_duration))  # Scale from 1.0 to 1.5
        else:
            # Shrinking phase
            scale = 1.5 - (0.5 * ((elapsed - half_duration) / half_duration))  # Scale from 1.5 to 1.0

        # Create a new font object with the scaled size
        scaled_font_size = int(font.get_height() * scale)
        scaled_font = pygame.font.Font(resource_path(FONTPATH), scaled_font_size)

        # Render the character with the scaled font
        text_surface = scaled_font.render(self.current_animating_char, True, BLACK)

        # Calculate new position to keep the letter centered
        new_x = x - (text_surface.get_width() - font.size(self.current_animating_char)[0]) // 2
        new_y = y - (text_surface.get_height() - font.size(self.current_animating_char)[1]) // 2

        self.draw_text(screen, self.current_animating_char, scaled_font, BLACK, new_x, new_y)
        
        
    def draw_game_elements(self, screen, font, elapsed_time, bg_image):
        if self.current_pokemon:
        
            # Apply jiggle offset
            jiggle_x, jiggle_y = self.jiggle_offset
            walk_x, walk_y = self.current_pokemon.walk_offset

            # Draw the Pokemon Background
            screen.blit(self.current_pokemon.bg, (SCREEN_WIDTH - SCREEN_HEIGHT//2 - 50, SCREEN_HEIGHT// 2 -50))

            # Draw the Pokemon sprite
            max_pokemon_scale = 2.0
            scale = 1 + (max_pokemon_scale - 1) * elapsed_time / self.current_pokemon.time_limit

            # Calculate the scaled size of the ball
            scaled_width = int(self.current_pokemon.sprite.get_width() * scale)
            scaled_height = int(self.current_pokemon.sprite.get_height() * scale)
            
            # Scale the hanja
            scaled_pokemon_sprite = pygame.transform.smoothscale(self.current_pokemon.sprite, (scaled_width, scaled_height))

            self.current_pokemon.current_position[0] = SCREEN_WIDTH // 2 - self.current_pokemon.sprite.get_width() // 2 + walk_x +  jiggle_x
            self.current_pokemon.current_position[1] = min(100 + walk_y + jiggle_y, 200)
            
            if not self.caught_pokemon or not self.caught_pokemon.ball_hit:
                screen.blit(scaled_pokemon_sprite, self.current_pokemon.current_position)

            # Draw the rounded rectangle around the Pokémon name and timer bar
            name_x = SCREEN_WIDTH // 2 - font.size(self.current_pokemon.name)[0] // 2
            name_width = font.size(self.current_pokemon.name)[0]
            name_height = font.size(self.current_pokemon.name)[1]
            rect_width = name_width + 20  # Add some padding
            rect_height = name_height + 60  # Enough height to cover the name and timer bar
            rect_x = name_x - 10 + walk_x
            rect_y = 320
            self.draw_rounded_rect(screen, pygame.Rect(rect_x, rect_y, rect_width, rect_height), LIGHT_GRAY, radius=15, outline_color=BLACK)

            # Draw the Pokemon name in full capital letters
            name_x = SCREEN_WIDTH // 2 - font.size(self.current_pokemon.name)[0] // 2
            if elapsed_time > NOT_SHOW_NAME_TIME or len(self.typed_name) > 0:
                self.draw_text(screen, self.current_pokemon.name, font, BLACK, name_x + walk_x, rect_y + 20)
                
                # Draw the timer bar just below the typed name
                time_to_draw = self.current_pokemon.caught_time if self.current_pokemon.is_caught else elapsed_time
                self.draw_timer_bar(screen, name_x + walk_x, rect_y + name_height + 20, font.size(self.current_pokemon.name)[0], 15, time_to_draw, self.current_pokemon.time_limit)

            # Draw each typed letter exactly below each corresponding letter of the Pokemon name
            for i, char in enumerate(self.typed_name[:-1]):  # All typed letters except the last one
                char_x = name_x + font.size(self.current_pokemon.name[:i])[0]
                self.draw_text(screen, char, font, RED, char_x + walk_x, rect_y + 20)

            # Animate the last typed letter
            if self.typed_name:
                last_char_x = name_x + font.size(self.current_pokemon.name[:len(self.typed_name) - 1])[0]
                self.animate_letter_appearance(screen, font, last_char_x + walk_x, rect_y + 20)
        else:
            screen.blit(bg_image, (0, 0))

    def get_target_position_in_array(self):
        x_start = 20
        y_start = SCREEN_HEIGHT - 205
        cols = 10
        icon_size = 32
        padding = 5
        
        index = len(self.caught_pokemons)
        col = (index) % cols
        row = (index) // cols
        x = x_start + col * (icon_size + padding)
        y = y_start + row * (icon_size + padding)
        
        return x,y
    
    def update_caught_pokemon_surface(self):
        # Create an off-screen surface with the same size as the caught Pokémon box
        rect_width = 400
        rect_height = 200
        self.caught_pokemon_surface = pygame.Surface((rect_width, rect_height), pygame.SRCALPHA)
        
        cols = 10
        icon_size = 32
        padding = 5
        offset = 21
        x_start = 10
        y_start = 5

        # Include the current combo if it exists and is of length 3 or more
        combo_indices = self.combo_indices.copy()
        if self.combo_count >= 3:
            combo_indices.append((len(self.caught_pokemons) - self.combo_count, len(self.caught_pokemons)))

        # Draw combo outlines for all combos of length 3 or more
        for start_index, end_index in combo_indices:
            start_col = start_index % cols
            start_row = start_index // cols
            end_col = (end_index - 1) % cols
            end_row = (end_index - 1) // cols

            for row in range(start_row, end_row + 1):
                row_start_col = start_col if row == start_row else 0
                row_end_col = end_col if row == end_row else cols - 1
                x1 = x_start + row_start_col * (icon_size + padding) - 2
                x2 = x_start + row_end_col * (icon_size + padding) + icon_size + 2
                y = y_start + row * (icon_size + padding) - 2
                highlight_rect = pygame.Rect(x1, y + 2, x2 - x1, icon_size + 2)

                # Draw gradient background
                self.draw_gradient_rect(self.caught_pokemon_surface, highlight_rect, COMBOCOLOR1, COMBOCOLOR2)

        for index, (icon, fast, superfast) in enumerate(self.caught_pokemons):
            col = index % cols
            row = index // cols
            x = x_start + col * (icon_size + padding)
            y = y_start + row * (icon_size + padding)

            self.caught_pokemon_surface.blit(icon, (x, y))

            # Draw Legendary outline
            if superfast:
                self.caught_pokemon_surface.blit(self.premier_ball_sprite, (x + offset, y + offset))
            elif fast:
                self.caught_pokemon_surface.blit(self.dive_ball_sprite, (x + offset, y + offset))
            else:
                self.caught_pokemon_surface.blit(self.dusk_ball_sprite, (x + offset, y + offset))

        self.should_update_caught_pokemon_surface = False
        
    def draw_caught_pokemon_icons(self, screen, rect_x=10, rect_y=SCREEN_HEIGHT - 210):
        if self.should_update_caught_pokemon_surface:
            self.update_caught_pokemon_surface()

        # Draw the box around it
        rect_width = 400  # Add some padding
        rect_height = 200  # Enough height to cover the name and timer bar
        self.draw_rounded_rect(screen, pygame.Rect(rect_x, rect_y, rect_width, rect_height), WHITE, radius=15, outline_color=BLACK)

        # Blit the off-screen surface containing the caught Pokémon icons
        screen.blit(self.caught_pokemon_surface, (rect_x, rect_y))
        
    def draw_end_screen(self,screen, font):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.fill(GRAY)
        overlay.set_alpha(150)  # Set transparency to 150
        screen.blit(overlay, (0, 0))

        # Draw box around 
        menu_rect = pygame.Rect(SCREEN_WIDTH // 2 - 300, SCREEN_HEIGHT // 2 - 250, 600, 550)
        self.draw_rounded_rect(screen, menu_rect, WHITE, radius=15, outline_color=BLACK)

        # Display Stats
        self.draw_text(screen, f"SCORE : {round(self.total_score)}", font, BLACK, menu_rect.x + 50, menu_rect.y + 20 )
        self.draw_text(screen, f"MISTAKES: {self.total_mistake_count}", font, BLACK, menu_rect.x + 50, menu_rect.y + 50 )
        max_combo_length = max(end - start for start, end in self.combo_indices) if self.combo_indices else 0
        self.draw_text(screen, f"MAX COMBO: {max_combo_length}", font, BLACK, menu_rect.x + 50, menu_rect.y + 80 )
        self.draw_text(screen, f"REACHED: {self.level_reached}", font, BLACK, menu_rect.x + 50, menu_rect.y + 110 )

        for i, option in enumerate(GameSession.END_OPTIONS):
            color = GREEN if i == self.selected_end_option else BLACK
            self.draw_text(screen, option, font, color, menu_rect.x + 250, menu_rect.y + 470 + i * 30)

        # Draw the caught Pokémon icons
        self.draw_caught_pokemon_icons(screen , SCREEN_WIDTH // 2 - 200 , SCREEN_HEIGHT // 2 )
        
    def handle_end_menu_input(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.selected_end_option = (self.selected_end_option - 1) % len(GameSession.END_OPTIONS)
            elif event.key == pygame.K_DOWN:
                self.selected_end_option = (self.selected_end_option + 1) % len(GameSession.END_OPTIONS)
            elif event.key == pygame.K_RETURN:
                if GameSession.END_OPTIONS[self.selected_end_option] == "Restart":
                    self.reset_game(self.hanja_data)
                elif GameSession.END_OPTIONS[self.selected_end_option] == "Quit":
                    pygame.quit()
                    exit()

    def draw_game_scores(self, screen, font):
        # Draw the score and combo count
        font_height = font.size("Caught")[1] * 1.75
        beginning = 15
        x_offset = 20
        
        screen.blit(self.premier_ball_sprite, (x_offset, beginning))
        self.draw_text(screen, f"Caught: {self.caught_pokemon_count}", font, BLACK, 3*x_offset, 20)
        screen.blit(self.combo_sprite, (x_offset, beginning + 1.15*font_height))
        self.draw_text(screen, f"Combo: {self.combo_count}", font, BLACK, 3*x_offset, 60)
        screen.blit(self.score_sprite, (x_offset, beginning + 2.3*font_height))
        self.draw_text(screen, f"Score: {int(self.total_score)}", font, BLACK, 3*x_offset, 100)
        screen.blit(self.mistake_sprite, (x_offset, beginning + 3.45*font_height))
        self.draw_text(screen, f"Mistakes: {int(self.mistake_count)} / {MAX_MISTAKE}", font, BLACK, 3*x_offset, 140)
        
    def update_capture_animation(self, screen):
        if self.animation_state == "PARABOLIC":
            
            # Horizontal movement towards Pokémon
            horizontal_distance = self.ball_target[0] - self.ball_start[0]
            self.ball_position[0] += horizontal_distance / 40  # Adjust denominator for speed

            # Calculate height for the parabola
            peak_height = (self.ball_target[1] - self.ball_start[1]) / 2 - 100  # Adjust -100 for peak height
            x_fraction = (self.ball_position[0] - self.ball_start[0]) / horizontal_distance
            self.ball_position[1] = (self.ball_start[1] * (1 - x_fraction) + 
                                     self.ball_target[1] * x_fraction + 
                                     peak_height * (1 - (2 * x_fraction - 1) ** 2))

            # Calculate the scale
            ball_scale_max = 4.0
            scale = ball_scale_max - (ball_scale_max - 1) * ((self.ball_position[0] - self.ball_start[0])  / horizontal_distance)

            # Calculate the scaled size of the ball
            scaled_width = int(self.ball_sprite.get_width() * scale)
            scaled_height = int(self.ball_sprite.get_height() * scale)
            
            # Scale the halo effect image
            scaled_ball_sprite = pygame.transform.scale(self.ball_sprite, (scaled_width, scaled_height))

            screen.blit(scaled_ball_sprite, self.ball_position)

            # Check if the ball reached the target
            if abs(self.ball_position[0] - self.ball_target[0]) < 5:
                if self.caught_pokemon:
                    self.caught_pokemon.ball_hit = True
                self.animation_state = "HALO"
                self.halo_timer = pygame.time.get_ticks()

        elif self.animation_state == "HALO":
            # Calculate the time elapsed since the halo animation started
            elapsed = pygame.time.get_ticks() - self.halo_timer
            halo_effect_duration = 300
            halo_offset_x = 40  # Example offset values
            halo_offset_y = 60
            halo_scale_max = 7.0
            
            # Determine the scale factor (from 1.0 to 4.0 and back to 1.0)
            if elapsed <= halo_effect_duration / 2:
                scale = 1.0 + (halo_scale_max - 1) * (elapsed / (halo_effect_duration/2))  # Expanding phase
            else:
                scale = halo_scale_max - (halo_scale_max - 1) * ((elapsed - (halo_effect_duration/2)) / (halo_effect_duration/2))  # Shrinking phase

            # Prevent scale from becoming negative
            scale = max(scale, 1.0)
            
            # Calculate the scaled size of the halo effect
            scaled_width = int(self.halo_effect.get_width() * scale)
            scaled_height = int(self.halo_effect.get_height() * scale)
            
            # Scale the halo effect image
            scaled_halo_effect = pygame.transform.scale(self.halo_effect, (scaled_width, scaled_height))
            
            # Calculate the position to center the scaled halo at the ball's position with offset
            halo_x = self.ball_target[0] + halo_offset_x - scaled_halo_effect.get_width() // 2
            halo_y = self.ball_target[1] + halo_offset_y - scaled_halo_effect.get_height() // 2
            
            # Draw the halo effect
            screen.blit(scaled_halo_effect, (halo_x, halo_y))
    
            # Transition to the next state after the halo animation completes
            if elapsed > halo_effect_duration:
                self.animation_state = "BEELINE"
                self.ball_target = self.get_target_position_in_array()

        elif self.animation_state == "BEELINE":
            # Smooth transition to bottom left
            speed = 10
            if self.ball_position[0] > self.ball_target[0]:
                self.ball_position[0] -= speed
            if self.ball_position[1] < self.ball_target[1]:
                self.ball_position[1] += speed

            screen.blit(self.ball_sprite, self.ball_position)

            # Check if the ball reached the destination
            if (abs(self.ball_position[0] - self.ball_target[0]) < 5 and
                abs(self.ball_position[1] - self.ball_target[1]) < 5):
                self.animation_state = "IDLE"
                
                # Create a transparent surface
                transparent_patch = pygame.Surface((100, 100), pygame.SRCALPHA)
                transparent_patch.fill((0, 0, 0, 0))  # Fill with transparent color

                # Blit the transparent patch onto the screen at the desired position
                screen.blit(transparent_patch, self.ball_position)
                
    @staticmethod
    def draw_text(screen, text, font, color, x, y, outline_color = WHITE, outline_thickness = 2):
        """
        Draw text with an outline.
        """
        # Draw outline
        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:
                    outline_surface = font.render(text, True, outline_color)
                    screen.blit(outline_surface, (x + dx, y + dy))
        
        text_obj = font.render(text, True, color)
        screen.blit(text_obj, (x, y))
        
    @staticmethod
    def draw_timer_bar(surface, x, y, width, height, elapsed_time, time_limit):
        fill_width = (elapsed_time / time_limit) * width
        color = GREEN if fill_width < width * 0.55 else AMBER if fill_width < width * 0.80 else RED
        
        # Draw the white rounded rectangle as the background
        rounded_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(rounded_surface, (255, 255, 255, 255), rounded_surface.get_rect(), border_radius=height // 2)
        surface.blit(rounded_surface, (x, y))
        
        # Draw the colored filled bar on top of the white background
        filled_rect = pygame.Surface((fill_width, height), pygame.SRCALPHA)
        pygame.draw.rect(filled_rect, color, filled_rect.get_rect(), border_radius=height // 2)
        surface.blit(filled_rect, (x, y))

    @staticmethod
    def jiggle():
        return random.randint(-5, 5), random.randint(-5, 5)

    @staticmethod
    def draw_gradient_rect(surface, rect, color1, color2, radius=15):
        """Draw a vertical gradient rounded rectangle."""
        gradient_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        for y in range(rect.height):
            ratio = y / rect.height
            color = (
                int(color1[0] * (1 - ratio) + color2[0] * ratio),
                int(color1[1] * (1 - ratio) + color2[1] * ratio),
                int(color1[2] * (1 - ratio) + color2[2] * ratio)
            )
            pygame.draw.line(gradient_surface, color, (0, y), (rect.width, y))

        # Create a rounded mask
        mask_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        pygame.draw.rect(mask_surface, (255, 255, 255), mask_surface.get_rect(), border_radius=radius)
        mask = pygame.mask.from_surface(mask_surface)

        # Apply the mask to the gradient
        rounded_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        for x in range(rect.width):
            for y in range(rect.height):
                if mask.get_at((x, y)):
                    rounded_surface.set_at((x, y), gradient_surface.get_at((x, y)))

        surface.blit(rounded_surface, rect.topleft)

    @staticmethod
    def draw_rounded_rect(surface, rect, color, radius=15, outline_color=None, outline_width=2):
        """Draw a rounded rectangle with optional outline."""
        rounded_surface = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        
        # Adjust the color to include 50% transparency
        color_with_alpha = (*color, 128)  # Assuming color is (R, G, B)
        
        pygame.draw.rect(rounded_surface, color_with_alpha, rounded_surface.get_rect(), border_radius=radius)
        if outline_color:
            pygame.draw.rect(rounded_surface, outline_color, rounded_surface.get_rect(), outline_width, border_radius=radius)
        surface.blit(rounded_surface, rect.topleft)

    def process_game_loop(self, event, current_time, screen):
        
        if event.type == pygame.QUIT:
            running = False
            
        elif self.game_ended:
            self.handle_end_menu_input(event)

        elif self.game_paused:
            self.handle_pause_menu_input(event)            
        
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if self.game_paused:
                self.unpause_game(current_time)
            else:
                self.pause_game(current_time)

        elif self.current_pokemon and event.type == pygame.KEYDOWN:
            self.typed_name += event.unicode.upper()
            self.animate_last_letter(event.unicode.upper())

            if self.current_pokemon.name.startswith(self.typed_name):
                if self.typed_name == self.current_pokemon.name:
                    self.pokemon_caught(self.current_pokemon.elapsed_time)
            elif not self.transitioning:
                self.pokemon_missed(500)

        elif event.type == SPAWN_POKEMON_EVENT:
            self.check_progress()
        elif event.type == MESSAGE_CLEAR_EVENT:
            self.messages.clear()
        elif event.type == SPECIAL_MESSAGE_CLEAR_EVENT:
            self.special_message["text"] = ""
        elif self.current_pokemon and event.type == JIGGLE_EVENT:
            self.jiggle_offset = self.jiggle()
        elif self.current_pokemon and event.type == WALK_EVENT:
            self.current_pokemon.walk()
        elif event.type == TRANSITION_END_EVENT:
            self.unpause_game(current_time, False)
            self.spawn_pokemon()
        
        return None
    