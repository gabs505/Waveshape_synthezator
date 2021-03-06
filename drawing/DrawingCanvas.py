from .DrawingCanvas_methods import *


class DrawingCanvas:
    def __init__(self):
        self.drawing_area = tk.Canvas(width= Setup.width, height=Setup.height)
        self.drawing_area.bind("<Motion>", self.motion)
        self.drawing_area.bind("<ButtonPress-1>", self.left_but_down)
        self.drawing_area.bind("<ButtonRelease-1>", self.left_but_up)
        introducing_lines(self)
        #self.drawing_area.pack()


    drawing_tool = "pencil"
    left_but = "up"             # Tracks whether left mouse is down
    x_pos, y_pos = None, None   # x and y positions for drawing with pencil


    # ---------- DRAW PENCIL ----------
    pencil_draw = pencil_draw_method

    # ---------- CATCH MOUSE MOVEMENT ----------
    motion = motion_method

    # ---------- CATCH MOUSE UP ----------
    left_but_down = left_but_down_method
    left_but_up = left_but_up_method


    delete_lines = delete_lines_method










