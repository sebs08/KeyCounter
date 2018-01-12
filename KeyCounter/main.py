import keyboard
import pygame
import button, scene
import math, time
#import pdb; pdb.set_trace()

display_width = 480
display_height = 320
# pygame.RESIZEABLE - adds the option to resize the window; is in testing ;)
screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)

pygame.init()

pygame.display.set_caption("KeyCounter")


class MainScene(scene.SceneBase):
    def __init__(self, display_screen, background=(255, 255, 255)):
        scene.SceneBase.__init__(self, display_screen, background)
        # make more dynamic

        self.count = 0

        self.buttons = {}

        self.buttons["add_one"] = button.Button(display_screen, (50, 200), (40, 40), (0, 102, 0), tag="add_1", execute=lambda: self.set_count(relative=1))
        self.buttons["sub_one"] = button.Button(display_screen, (50, 250), (40, 40), (204, 102, 0), tag="sub_1", execute=lambda: self.set_count(relative=-1))

        self.buttons["sub_5"] = button.Button(display_screen, (100, 250), (40, 40), (204, 102, 0), tag="sub_5", execute=lambda: self.set_count(relative=-5))
        self.buttons["add_5"] = button.Button(display_screen, (100, 200), (40, 40), (0, 102, 0), tag="add_5", execute=lambda: self.set_count(relative=5))

        self.buttons["reset"] = button.Button(display_screen, (300, 250), (40, 40), (102, 178, 255), tag="reset_0", execute=lambda: self.set_count(absolute=0))

        self.buttons["exit"] = button.Button(display_screen, (400, 250), (40, 40), (255, 0, 0), tag="exit", execute=self.ExitProgramm)

        #self.buttons["speed_up"] = button.Button(display_screen, (300, 180), (30, 30), (0, 102, 102), (0,102,0), tag="speed_up", execute=lambda: self.sinus_speed_add(1))
        #self.buttons["speed_down"] = button.Button(display_screen, (380, 180), (30, 30), (0, 102, 102), (0,102,0), tag="speed_down", execute=lambda: self.sinus_speed_add(-1))
        # for sinus variable speed
        self.sin_speed = 1

    def Update(self):
        scene.SceneBase.Update(self)

        for key in self.buttons:
            self.buttons[key].draw()

        self.sinus_window()

        self.display_count()

        pygame.display.update()


    def ProcessInput(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for key in self.buttons:
                    self.buttons[key].clicked(event)

    def Render(self, screen):
        pass

    def sinus_speed_add(self, increment=0):
        self.sin_speed += increment


    def sinus_window(self):
        width, height = 140, 80
        surface = pygame.Surface((width, height))
        surface.fill((255,255,255))

        speed = self.sin_speed
        speed2 = speed * 1.3
        amplitude = 35
        frequency = 3
        for x in range(0, width):
            # sinus curve 1
            y1 = int((height / 2) + amplitude * math.sin(
                frequency * ((float(x) / width) * (2 * math.pi) + (speed * time.time()))))
            y2 = int((height / 2) + amplitude * math.sin(
                frequency * (((float(x) / width)+ 0.5/float(frequency)) * (2 * math.pi) + (speed2 * time.time()))))
            """
            y1 = int((height / 2) + amplitude * math.sin(
                ((float(x) / width) * (2 * math.pi))))
            y2 = int((height / 2) + amplitude * math.sin(
                (((float(x) / width) +0.5 )* (2 * math.pi))))
            """
            surface.set_at((x, y1), (0,0,0))
            surface.set_at((x, y2), (0,0,0))

        self.display_screen.blit(surface, (300, 70))



    def display_count(self):
        font = pygame.font.SysFont(None, 70)

        display_text = font.render(str(self.count), True, (0, 0, 0))
        screen.blit(display_text, (80, 80))

    def set_count(self, relative=0, absolute=None):

        if absolute is not None:
            self.count = absolute
        else:
            self.count += relative


def run(activate_keys=False):



    screen.fill((255, 255, 255))
    pygame.display.update()
    clock = pygame.time.Clock()

    active_scene = MainScene(screen, (255, 255, 255))

    if activate_keys:
        # change key allocation here
        """
        keys = {}
        # structure of dictionary entries: [key combination (as string); increment amount / or abs value to be set;
        #                                      absolute value - 0, relative value - 1]
        keys['add_1'] = ["ctrl+alt", 1, 1]
        keys['add_5'] = ['5', 5, 1]
        keys['sub_5'] = ['plus', -5, 1]
        keys['sub_1'] = ['minus', -1, 1]
        keys['reset'] = ['.', 0, 0]
        for key in keys:
            #key_values = keys[key]
            print(keys[key])
            print(keys)

            if keys[key][2]:
                press_keys = keys[key][0]
                add_value = keys[key][1]
                keys[key].append(keyboard.add_hotkey(press_keys, lambda: active_scene.set_count(relative=add_value)))
            elif not keys[key][2]:
                press_keys = keys[key][0]
                set_value = keys[key][1]
                keys[key].append(keyboard.add_hotkey(press_keys, lambda: active_scene.set_count(absolute=set_value)))
        """

        keyboard.add_hotkey('ctrl+alt', lambda: active_scene.set_count(relative=5))
        keyboard.add_hotkey('plus', lambda: active_scene.set_count(relative=1))
        keyboard.add_hotkey('shift, alt', lambda: active_scene.set_count(absolute=0))
        keyboard.add_hotkey('minus', lambda: active_scene.set_count(relative=-1))

    time_passed = 0

    running = True
    filtered_events = []
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            else:
                filtered_events.append(event)

        time_passed += clock.tick()

        if time_passed >= 50:
            active_scene.ProcessInput(filtered_events)
            active_scene.Update()
            active_scene.Render(screen)

            time_passed = 0
            filtered_events = []

    pygame.quit()
    quit()


if __name__ == "__main__":
    # change to True if adding count by pressing keys should be enabled
    # for using key shortcuts the script must be run as administrator
    # for more information see 'keyboard' documentation
    activate_keys = True

    run(activate_keys)
