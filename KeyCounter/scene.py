import pygame

# don't forget to initialize pygame (pygame.init())


class SceneBase:
    def __init__(self, display_screen, background = (255,255,255)):
        self.display_screen = display_screen
        self.running = True
        self.background = background
        self.next = self

    def ProcessInput(self, events):
        print("nothing to process")

    def ExitProgramm(self):
        pygame.quit()
        quit()

    def change_background(self, new_background = None):
        if new_background != None:
            self.background = new_background


    def Update(self):
        self.display_screen.fill(self.background)
        # print("uh-oh, you didn't override this in the child class")

    def Render(self, screen):
        pass
        #print("nothing to render")

    def SwitchToScene(self, next_scene):
        self.next = next_scene