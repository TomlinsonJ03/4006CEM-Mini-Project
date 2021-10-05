import tkinter as tk
from options import options


def main():
    root = tk.Tk()
    app = App(master=root)

    app.createButton(options['Start']['xStart'], options['Start']['yStart'],
                     options['Start']['xEnd'], options['Start']['yEnd'], 'Start')

    app.map.bind('<Button-1>', app.checkIfButtonExists)

    app.mainloop()


class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.grid()
        self.mapWidth = 1000
        self.mapHeight = 600
        self.buttons = []

        self.map = tk.Canvas(self.master, width=self.mapWidth, height=self.mapHeight)
        self.map.grid()

    def createButton(self, xStart, yStart, xEnd, yEnd, text, color='yellow'):
        """Creates a button and the text within it, changes it's status to activated. Takes in the
        coordinates where the button where will be drawn and the color which fills the button.
        Returns the button ID. Can also be used to update buttons"""

        button = self.map.create_rectangle(self.mapWidth*xStart, self.mapHeight*yStart,
                                           self.mapWidth*xEnd, self.mapHeight*yEnd,
                                           fill=color)

        self.map.create_text(self.mapWidth*((xStart+xEnd)/2),
                             self.mapHeight*(yStart+yEnd)/2, text=text)

        options[text]['activated'] = True
        return button

    def drawConnection(self, xStart, yStart, xEnd, yEnd):
        """Draws a line between 2 buttons. Takes the coordinate of the bottom centre of the parent button
        and the top centre of the child button."""

        self.map.create_line(xStart*self.mapWidth, yStart*self.mapHeight,
                             xEnd*self.mapWidth, yEnd*self.mapHeight)

    def checkIfButtonExists(self, event):
        """Checks if the button 1 click happend on a activated button. Compares the x and y
        of the event, to the location of any activated buttons. Passes the button that was clicked
        to the updateButton function."""

        for option in options:
            if (options[option]['activated'] is True and
                    event.x > options[option]['xStart']*self.mapWidth and
                    event.y > options[option]['yStart']*self.mapHeight and
                    event.x < options[option]['xEnd']*self.mapWidth and
                    event.y < options[option]['yEnd']*self.mapHeight):

                self.updateButton(option)

    def updateButton(self, option):
        """Changes the clicked button's color to green or red if it's an ending button. Draws the
        child buttons and the connections between the clicked button and the child buttons."""

        if options[option]['ending'] is False:
            color = 'green'
        else:
            color = 'red'

        self.createButton(options[option]['xStart'], options[option]['yStart'],
                          options[option]['xEnd'], options[option]['yEnd'],
                          option, color)

        for child in options[option]['children']:

            if child is not None:
                self.drawConnection((options[option]['xStart']+options[option]['xEnd'])/2,
                                    options[option]['yEnd'],
                                    (options[child]['xStart']+options[child]['xEnd'])/2,
                                    options[child]['yStart'])

            if child is not None and options[child]['activated'] is False:
                self.createButton(options[child]['xStart'], options[child]['yStart'],
                                  options[child]['xEnd'], options[child]['yEnd'],
                                  child, 'yellow')
            else:
                pass


if __name__ == '__main__':
    main()
