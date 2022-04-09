class Background():
    def __init__(self):
        self.image = self.image.load("game_stuff/assets/magma.png")
    
    def draw(self, display):
        display.blit(self.image, (0, 0))

        