class Vertex:
    moves = {
        'A': (0, 1),
        'B': (0, -1),
        'R': (1, 0),
        'L': (-1, 0)
    }

    def __init__(self, key):
        self.id = key
        self.connections = {}

    def __str__(self):
        return '{}'.format(self.id)

    def add_connection(self, adj_vertex, position=None):
        self.connections[adj_vertex] = Vertex.moves[position]
        # adj_vertex.connections[self.id] = (Vertex.moves[position][0]*(-1), Vertex.moves[position][1]*(-1))

    def get_connections(self):
        return self.connections.items()

    def get_id(self):
        return self.id


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, item):
        if item in self.vertices:
            return True
        else:
            return False

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)
        self.num_vertices += 1

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()

    def add_edge(self, fr, to, pos=None):
        if fr not in self.vertices:
            self.add_vertex(fr)
        elif to not in self.vertices:
            self.add_vertex(to)
        self.vertices[fr].add_connection(self.vertices[to], pos)

    def get_all_neighbours(self):
        neighbours = {}
        for vertex in self:
            neighbours[vertex.get_id()] = [(v.id, pos) for v, pos in vertex.get_connections()]
        return neighbours




def main():
    g = Graph()
    g.add_vertex('A')
    g.add_edge('A', 'B', 'B')
    g.add_edge('B', 'C', 'R')
    g.add_edge('B', 'D', 'L')

    print(g.get_all_neighbours())


if __name__ == '__main__':
    main()



    # g = Graph()
    # g.add_vertex('A')
    # g.add_edge('B', 'A', 'A')
    # g.add_edge('F', 'A', 'R')
    # g.add_edge('C', 'B', 'A')
    # g.add_edge('D', 'C', 'R')
    # g.add_edge('E', 'D', 'A')
    # g.add_edge('G', 'E', 'L')

    # ex_input = '..*...*.**\n' \
    #            '.....**...\n' \
    #            '*.*...*..*\n' \
    #            '.**....*.*\n' \
    #            '...*..*.*.\n' \
    #            '.***...*..\n' \
    #            '*......*.*\n' \
    #            '.....**..*\n' \
    #            '..*.*.*..*\n' \
    #            '***.*.**..\n'