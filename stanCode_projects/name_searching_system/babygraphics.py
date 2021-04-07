"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE:
babygraphics.py draws the lines and name data such as names, years, and ranks on a canvas, which illustrates how the
trend of the searched names change.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    space = (width - GRAPH_MARGIN_SIZE * 2)/len(YEARS)
    x_coordinate = GRAPH_MARGIN_SIZE + space * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    color_num = 0
    for lookup_n in lookup_names:
        if lookup_n in name_data:
            color_num += 1
            color_index = (color_num % len(COLORS)) - 1
            year1 = YEARS[0]
            x1 = get_x_coordinate(CANVAS_WIDTH, 0)
            if f'{year1}' in name_data[lookup_n]:
                # According to the data, if the name exists in the data, the name's rank is not larger than 1000
                rank = int(name_data[lookup_n][f'{year1}'])
                y1 = GRAPH_MARGIN_SIZE + (rank - 1) * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 999
                canvas.create_text(x1 + TEXT_DX, y1, text=f'{lookup_n} {rank}', anchor=tkinter.SW,
                                   fill=COLORS[color_index])
            else:
                # Names in a certain year with its ranking larger than 1000 will not appear in the data
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(x1 + TEXT_DX, y1, text=f'{lookup_n} *', anchor=tkinter.SW, fill=COLORS[color_index])
            for i in range(len(YEARS)-1):
                year = YEARS[i+1]
                x = get_x_coordinate(CANVAS_WIDTH, i+1)
                if f'{year}' in name_data[lookup_n]:
                    # According to the data, if the name exists in the data, the name's rank is not larger than 1000
                    rank = int(name_data[lookup_n][f'{year}'])
                    y = GRAPH_MARGIN_SIZE + (rank - 1) * (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE * 2) / 999
                    canvas.create_text(x + TEXT_DX, y, text=f'{lookup_n} {rank}', anchor=tkinter.SW, fill=COLORS[color_index])
                    canvas.create_line(x1, y1, x, y, width=LINE_WIDTH, fill=COLORS[color_index])
                    x1 = x
                    y1 = y
                else:
                    # Names in a certain year with its ranking larger than 1000 will not appear in the data
                    y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    canvas.create_text(x + TEXT_DX, y, text=f'{lookup_n} *', anchor=tkinter.SW, fill=COLORS[color_index])
                    canvas.create_line(x1, y1, x, y, width=LINE_WIDTH, fill=COLORS[color_index])
                    x1 = x
                    y1 = y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
