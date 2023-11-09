from utils import randbool
# from utils import randcell



class Clouds:
    def __init__(self, w, h):
         self.h = h
         self.w = w
         self.cells = [[0 for i in range(w)] for j in range (h)]

    def update(self, r = 1, mxr = 20, g = 1, mxg = 10):
        for i in range (self.h):
            for j in range (self.w):
                if randbool(r, mxr):
                    self.cells[i][j] = 1
                    if randbool(g, mxg):
                        self.cells[i][j] = 2
                else:
                    self.cells[i][j] = 0

    # def add_storm(self):
        # c = randcell(self.w, self.h)
        # cx, cy = c[0], c[1]
        # if self.cells[cx][cy] == 0:
        #     self.cells[cx][cy] = 1

    def export_data (self):
        return {"cells ": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)] for j in range (self.h)]