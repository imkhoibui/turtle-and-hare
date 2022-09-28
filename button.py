"""
This class is used to create and work with button in the program.
There are four main functions in this class, including:
    __init__(self, insert_image, position, display_text, text_font, preset_color, mouse_over_color)
    update(self, screen)
    check_input(self, position)
    change_color(self, position)
   
"""
class Button():
    def __init__(self, insert_image, position, display_text, text_font, preset_color, mouse_over_color):
        """This function defines the attributes of the class, and assign each variables for each instances passes
        Parameters:
            self - a class instance
            insert_image - the image used to display for the button
            position - the position of the button to be drawn
            display_text - the text being displayed on the button
            text_font - the font of the text for the button
            preset_color - the initially color of the button
            mouse_over_color - the color the button changes to when the mouse is hovering above the button
        """
        self.insert_image = insert_image
        self.x_position = position[0]
        self.y_position = position[1]
        self.text_font = text_font
        self.preset_color, self.mouse_over_color = preset_color, mouse_over_color
        self.display_text = display_text
        self.text = self.text_font.render(self.display_text, True, self.preset_color)
        if self.insert_image is None:
            self.insert_image = self.text
        self.rect = self.insert_image.get_rect(center=(self.x_position, self.y_position))
        self.text_rect = self.text.get_rect(center=(self.x_position, self.y_position))

    def update(self, screen):
        """This function updates the button's image on the screen
        Parameters:
            self - an instance
            screen - the screen where the button's image will be displayed"""
        if self.insert_image is not None:
            screen.blit(self.insert_image, self.rect)
        screen.blit(self.text, self.text_rect)

    def check_input(self, position):
        """This function checks for the event if it's in the rectangle area of the button
        Parameters:
            self - an instance
            position - the position of the mouse"""
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def change_color(self, position):
        """This function changes the button's color when the mouse is being hovered upon
        Parameters:
            self - an instance
            position - the position of the mouse"""
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.text_font.render(self.display_text, True, self.mouse_over_color)
        else:
            self.text = self.text_font.render(self.display_text, True, self.preset_color)