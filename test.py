import pygame
import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        
    return os.path.join(base_path, relative_path)

def render_chinese_character(character, font, target_height, outline_color=(255, 255, 255), outline_thickness=2):
    try:
        # Ensure Pygame is initialized
        if not pygame.get_init():
            pygame.init()

        # Render the character with black color to get its surface
        text_surface = font.render(character, True, (0, 0, 0))

        # Get the size of the rendered text
        text_width, text_height = text_surface.get_size()

        # Create a new surface with enough space for the outline
        surface_size = (text_width + outline_thickness * 2, text_height + outline_thickness * 2)
        outline_surface = pygame.Surface(surface_size, pygame.SRCALPHA)

        # Draw the outline
        for dx in range(-outline_thickness, outline_thickness + 1):
            for dy in range(-outline_thickness, outline_thickness + 1):
                if dx != 0 or dy != 0:
                    temp_surface = font.render(character, True, outline_color)
                    outline_surface.blit(temp_surface, (dx + outline_thickness, dy + outline_thickness))

        # Draw the main character on top of the outline
        outline_surface.blit(text_surface, (outline_thickness, outline_thickness))

        # Scale the text surface to the target size
        new_width = int(outline_surface.get_width() * (target_height / text_height))
        new_height = target_height
        scaled_surface = pygame.transform.smoothscale(outline_surface, (new_width, new_height))

        return scaled_surface
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize Pygame and Pygame font
        pygame.init()
        pygame.font.init()
        
        # Set up a display (needed for some Pygame functionality)
        pygame.display.set_mode((1, 1))

        # Load a font that supports Chinese characters
        font_path = "assets/font2.ttc"  # This can be a .ttf or .otf file
        font_size = 100
        font = pygame.font.Font(resource_path(font_path), font_size)
        
        # Define the Chinese character to render
        chinese_character = "韓"
        
        # Define the target height in pixels
        target_height = 200
        
        # Render the Chinese character with an outline
        rendered_image = render_chinese_character(chinese_character, font, target_height)
        
        if rendered_image:
            # Save the rendered image to a file for verification (optional)
            pygame.image.save(rendered_image, "rendered_character.png")
        
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
    finally:
        # Quit Pygame
        pygame.font.quit()
        pygame.quit()
