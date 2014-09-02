from OpenGL.GL import *from OpenGL.GLU import *import pygameimport os.pathclass ReadOBJ(object):    def __init__(self, fname = False):        self.vertices = []        self.normals = []        self.two_indices = []       # vertex to normal index        if fname:            self.read_file( fname )    def read_file(self, fname):        with open( fname, "Urb" ) as file_in:            for line in file_in:                words = line.split()                command = words[0]                data = words[1:]                if command == 'v': # Vertex                    x, y, z = data                    vertex = (float(x), float(y), float(z))                    self.vertices.append(vertex)                elif command == 'vn': # Normal                    x, y, z = data                    normal = (float(x), float(y), float(z))                    self.normals.append(normal)                elif command == 'f':                    for combo in data:                        vi, ni = combo.split('//')                        indices = (int(vi) - 1, int(ni) - 1)                        self.two_indices.append(indices)class ReadPoints(object):    def __init__(self, fpath = False):        self.vertices = []        if fpath:            self.read_file( fpath )    def __iter__(self):        """Iterates over self.vertices."""        return iter(self.vertices[:])    def __getitem__(self, index):        """Gets a component as though the reader were a list."""        return self.vertices[index]    def read_file(self, fpath):        with open( fpath, "Urb" ) as the_file:            for line in the_file:                words = line.split()                command = words[0]                data = words[1:]                if command == 'v': # Vertex                    x, y, z = data                    vertex = (float(x), float(y), float(z))                    self.vertices.append(vertex)