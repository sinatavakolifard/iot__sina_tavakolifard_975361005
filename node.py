class node:
    def __init__(self, id, X, Y) -> None:
        self.id = id
        self.X = X
        self.Y = Y
        self.neighbor_nodes = []
        
        self.R = 0
        self.G = 0
        self.B = 0
    
    def set_rgb(self, r, g, b):
        self.R = r
        self.G = g
        self.B = b