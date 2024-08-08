import pygame
import random
from config import SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, BLACK
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

class Hanja:
    def __init__(self, data, font):
        self.hanja = f"{data['hanja']}"
        self.hun = data["훈"]
        self.eum = data["음"]
        self.huneum = data["훈"] + " " + data["음"]
        self.name = data["english"].upper()
        self.english = data["english"]
        self.strokes = data["strokes"]
        self.grade = data["grade"]
        self.font = font
        self.is_caught = False
        self.caught_time = None
        self.ball_hit = False
        self.is_fast = False
        self.is_super_fast = False
        self.time_limit = self.get_time_limit()
        self.walk_offset = [0,0]
        self.start_time = pygame.time.get_ticks()
        self.current_position = [0,0]
        self.elapsed_time = 0
        self.total_paused_time = 0
        self.bg = self.load_bg_image()
        self.sprite = self.render_chinese_character(100)
        self.icon = self.render_chinese_character(25)
        
    def get_time_limit(self):
        return 10*1000
    
    def walk(self):
        self.walk_offset[0] += random.randint(-5, 5)
        self.walk_offset[1] += random.randint(-5, 10)
        
    def copy(self):
        # Create a new Pokemon instance without initializing it
        new_copy = Hanja.__new__(Hanja)

        # Copy the attributes from the current instance to the new one
        new_copy.__dict__ = self.__dict__.copy()

        return new_copy
    
    def render_chinese_character(self, target_height, outline_color = WHITE, outline_thickness = 2 ):
        
        character = self.hanja

        # Render the character with black color to get its surface
        text_surface = self.font.render(character, True, (0, 0, 0))

        # Get the size of the rendered text
        text_width, text_height = text_surface.get_size()

        # Create a new surface with enough space for the outline
        surface_size = (text_width + outline_thickness * 2, text_height + outline_thickness * 2)
        outline_surface = pygame.Surface(surface_size, pygame.SRCALPHA)

        # Draw the outline
        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:
                    temp_surface = self.font.render(character, True, outline_color)
                    outline_surface.blit(temp_surface, (dx + outline_thickness, dy + outline_thickness))

        # Draw the main character on top of the outline
        outline_surface.blit(text_surface, (outline_thickness, outline_thickness))

        # Scale the text surface to the target size
        new_width = int(outline_surface.get_width() * (target_height / text_height))
        new_height = target_height
        scaled_surface = pygame.transform.smoothscale(outline_surface, (new_width, new_height))

        return scaled_surface
    
    def load_bg_image(self, target_size=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2), gray_alpha=0.9):
        new_width, new_height = target_size
        
        scaled_image = self.render_chinese_character(new_height)
        gray_surface = pygame.Surface(scaled_image.get_size(), pygame.SRCALPHA)
        gray_surface.fill((128, 128, 128, int(255 * gray_alpha)))
        final_image = scaled_image.copy()
        final_image.blit(gray_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        
        japanese_surface = self.font.render(self.huneum, True, BLACK)  # Stylize the text as needed (e.g., color)
        korean_surface = self.font.render(f"Stroke: {self.strokes}", True, BLACK)  # Stylize the text as needed (e.g., color)
        id_surface = self.font.render(f"Grade: {self.grade}", True, BLACK)
        
        # Position the text at the bottom-right corner, justified to the right edge
        japanese_rect = japanese_surface.get_rect(bottomright=(new_width - 10, new_height - 10))  # 10-pixel padding from edges
        final_image.blit(japanese_surface, japanese_rect.topleft)
        korean_rect = korean_surface.get_rect(bottomright=(new_width - 10, japanese_rect.top - 10))  # 10-pixel padding from edges
        final_image.blit(korean_surface, korean_rect.topleft)
        id_rect = id_surface.get_rect(bottomright=(new_width - 10, korean_rect.top - 10))
        final_image.blit(id_surface, id_rect.topleft)
        
        return final_image

