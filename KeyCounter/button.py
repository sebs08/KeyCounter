import pygame

# don't forget to initialize pygame (pygame.init())

# TODO: change the button position relative to the window size!!
# TODO: otherwise resizing the window changes the position of the button, does not change the designated area though

class Button():
    def __init__(self,screen, pos, measures, color=(255, 255, 0), color2 = (0,0,-1), tag=None, execute=None):
        """

        :param screen: pycharm display
        :param pos: position of the button ( upper left corner ?! )
        :param measures: width und height of the button
        :param color: normal display color
        :param color2: mouse over display color
        :param tag: name (gets displayed)
        :param execute: function to be evaluated of button is pressed
                        -- by default, the .clicked function return True or False
                        -- if a function is assigned to execute ( e.g. execute=lambda : function ), the function gets
                            called
        """
        font = pygame.font.SysFont(None, 16)

        self.execute = execute
        self.screen = screen
        self.position = pos
        self.measures = measures
        self.color = color
        self.color2 = color2
        self.mouse_on_button = 0
        self.text = font.render(tag, True, (0, 0, 0))

        # get relative position
        screen_width, screen_height = pygame.display.get_surface().get_size()
        # set relativ x and y as x_rel = x / width of screen; y_rel = y / height of screen
        self.relative_pos = (float(pos[0])/screen_width, float(pos[1]/screen_height))





    def clicked(self, event):
        """

        :param event: pygame event
        :return:
                * if execute == None, the return will be an True or False statement, depending on whether the button
                    has been clicked or not (at this event)
                * if execute == function, the return will be the evaluated function
        """
        screen_width, screen_height = pygame.display.get_surface().get_size()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.relative_pos[0] * screen_width < event.pos[0] <= (self.relative_pos[0] * screen_width * \
                                                                      (1 + self.measures[0]) ):
                if self.relative_pos[1]*screen_height < event.pos[1] <= (self.relative_pos[1]*screen_height * \
                                                                      (1 + self.measures[1]) ):
                    if self.execute is not None:
                        return self.execute()
                    return True
        return False

    def on_button(self):
        mouse_pos = pygame.mouse.get_pos()
        screen_width, screen_height = pygame.display.get_surface().get_size()
        x, y = mouse_pos[0], mouse_pos[1]

        if self.relative_pos[0]*screen_width < x < (self.relative_pos[0]*screen_width + \
                                                    self.measures[0]*self.relative_pos[0]) and \
                self.relative_pos[1]*screen_height < y < (self.relative_pos[1]*screen_height + \
                                                      self.measures[1]*self.relative_pos[1]):
            self.mouse_on_button = 1
            return True
        self.mouse_on_button = 0

        return False

    def draw(self):
        # make more efficent?!
        if self.on_button() and self.color2 != (0,0,-1):
            pygame.draw.rect(self.screen, self.color2, pygame.Rect(self.position, self.measures), 0)
            self.screen.blit(self.text,(self.position[0],self.position[1]+self.measures[1]/2))
        else:
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.position, self.measures), 0)
            self.screen.blit(self.text,(self.position[0],self.position[1]+self.measures[1]/2))