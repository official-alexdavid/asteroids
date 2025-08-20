import pygame
from constants import *
import pygame.freetype

class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.freetype.Font(FONT_PATH, FONT_SIZE)
        self.font.origin = True
    
    def increase(self, amount):
        self.score += amount
    
    def draw(self, screen):
        score_text = f"Score: {self.score}"
        self.font.render_to(screen, (10, 10), score_text, "white")
    
    def reset(self):
        self.score = 0