class TextDraw:
    def __init__(self, height, width, bound = 1, sepsize = 1):
        self.fld = [[' ']*width for i in range(height)]
        self.height = height
        self.width = width
        self.bound = bound
        self.splitters = [[False]*width for i in range(height)]
        self.busy = [[False]*width for i in range(height)]
        self.cnt = 1
        self.sepsize = sepsize
        self.boxes = [[1]*width for i in range(height)]
    def safe(self, x, y):
        if x < 0: return False
        if y < 0: return False
        if x >= self.height: return False
        if y >= self.width: return False
        return True
    def busyceil(self, x, y):
        bound = self.bound
        for xx in range(x - bound, x + bound + 1):
            for yy in range(y - bound, y + bound + 1):
                if self.safe(xx, yy):
                    self.busy[xx][yy] = True
                    self.boxes[xx][yy] = 0
    def _box(self, x1, y1, x2, y2):
        self.cnt += 1
        x1 = max(0, x1)
        x2 = min(self.height-1, x2)
        y1 = max(0, y1)
        y2 = min(self.width-1, y2)
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                self.fld[x][y] = ' '
                self.boxes[x][y] = self.cnt
                self.splitters[x][y] = False
        for x in range(x1, x2+1):
            for y in (y1, y2):
                self.busyceil(x, y)
                if not self.splitters[x][y]:
                    self.fld[x][y] = '|'
                else:
                    if self.fld[x][y] != '|':
                        self.fld[x][y] = '+'
                self.splitters[x][y] = True
        for y in range(y1, y2+1):
            for x in (x1, x2):
                self.busyceil(x, y)
                if not self.splitters[x][y]:
                    self.fld[x][y] = '-'
                else:
                    if self.fld[x][y] != '-':
                        self.fld[x][y] = '+'
                self.splitters[x][y] = True

    def box(self, x1, y1, x2, y2):
        for d in range(self.sepsize):
            self._box(x1+d, y1+d, x2-d, y2-d)
    def print(self):
        print('\n'.join(''.join(x) for x in self.fld))
    def avaible(self, x, y):
        if not self.safe(x, y): return False
        if self.busy[x][y]: return False
        return True
    def puttext(self, text, x, y, x1 = None, y1 = None):
        if not self.avaible(x, y): return
        text = text.split('\n')
        if y1 != None:
            text = [x.center(y1-y+1) for x in text]
        for dx in range(len(text)):
            for dy in range(len(text[dx])):
                if self.safe(x+dx, y+dy):
                    if self.boxes[x+dx][y+dy] == self.boxes[x][y]:
                        self.fld[x+dx][y+dy] = text[dx][dy]
