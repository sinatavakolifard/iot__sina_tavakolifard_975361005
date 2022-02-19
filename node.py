from re import X
from tkinter import Y


class node:
    def __init__(self, id, X, Y) -> None:
        self.id = id
        self.X = X
        self.Y = Y
        self.neighbor_nodes = []