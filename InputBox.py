
import pygame


pygame.init()
screen = pygame.display.set_mode((640, 480))
COLOR_INACTIVE = (200, 200, 200)
COLOR_ACTIVE = pygame.Color('black')
FONT = pygame.font.Font('Futura-Medium.otf', 35)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.h = h
        self.x = x
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.secure = False

    def get_text(self):
        return self.text

    def get_text_secure(self):
        return "*"*len(self.text)
<<<<<<< HEAD
=======

>>>>>>> parent of 8e2665b (Fixed InputBox, Button, Sign in, and nesting of modules)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    print(self.text)
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    # def update(self):
    #     # Resize the box if the text is too long.
    #     width = max(200, self.txt_surface.get_width()+10)
    #     self.rect.w = width

    def draw(self, screen):
        # Blit the text.
<<<<<<< HEAD

        if self.secure:
            screen.blit(FONT.render("*"*len(self.text), True, self.color),
                        (self.rect.x + 20, self.rect.y + self.h/6 + 10))
        else:
            screen.blit(self.txt_surface, (self.rect.x +
                        20, self.rect.y + self.h/6 + 3))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 3, int(
            self.rect.height/3), int(self.rect.height/3))
=======
        
        if self.secure:
            screen.blit(FONT.render("*"*len(self.text), True, self.color), (self.rect.x + 20, self.rect.y+ self.h/6 + 10))
        else:
            screen.blit(self.txt_surface, (self.rect.x + 20, self.rect.y+ self.h/6 + 3))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 3, int(self.rect.height/3), int(self.rect.height/3))
>>>>>>> parent of 8e2665b (Fixed InputBox, Button, Sign in, and nesting of modules)
