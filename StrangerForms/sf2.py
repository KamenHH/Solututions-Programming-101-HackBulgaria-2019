"""Please read sample_input_and_output.txt file first
to see how to paste the input. :)"""

from collections import deque
from copy import deepcopy


class Vertex:
    """Vertex class used to construct vertices in the Graph() class."""
    # (row, column)
    moves = {
        'A': (-1, 0),
        'B': (1, 0),
        'R': (0, 1),
        'L': (0, -1)
    }

    def __init__(self, key):
        """id = the name tag
        row and col are the coordinates of the vertex
        when it is set on the matrix grid,
         """
        self.id = key
        self.row = 0
        self.col = 0
        self.connections = {}

    def __str__(self):
        return '{}'.format(self.id)

    def add_connection(self, adj_vertex, position=None):
        """Adds a new edge connecting the current vertex and the adjacent one
        and stores the position of the adjacent vertex in respect of the current"""
        self.connections[adj_vertex] = Vertex.moves[position]
        # adj_vertex.connections[self.id] = (Vertex.moves[position][0]*(-1), Vertex.moves[position][1]*(-1))

    def get_connections(self):
        return self.connections.items()

    def get_id(self):
        return self.id

    def set_row(self, row):
        self.row = row

    def set_col(self, col):
        self.col = col

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col


class Graph:
    """The class used to build the relations between the people sitting in the cinema
    It implements a adjacency list, when a vertex is created, a name tag (id) is stored
    as a key in a dict. The value is a vertex object which stores the specified id and
    all the relations (edges) with each connected neighbouring vertex.
    {A: Vertex obj} -> Vertex obj =
    {id, row, col, connections={B:(1,0)}"""
    def __init__(self):
        self.vertices = {}

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, item):
        if item in self.vertices:
            return True
        else:
            return False

    def add_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def get_vertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        else:
            return None

    def get_vertices(self):
        return self.vertices.keys()

    def set_vertex_row(self, key, row):
        self.vertices[key].set_row(row)

    def set_vertex_col(self, key, col):
        self.vertices[key].set_col(col)

    def get_vertex_row(self, key):
        return self.vertices[key].get_row()

    def get_vertex_col(self, key):
        return self.vertices[key].get_col()

    def add_edge(self, fr, to, pos=None):
        """Adds edges always form an existing vertex to a newly added one."""
        if fr not in self.vertices:
            self.add_vertex(fr)
            self.vertices[to].add_connection(self.vertices[fr], pos)
        elif to not in self.vertices:
            self.add_vertex(to)
            self.vertices[fr].add_connection(self.vertices[to], pos)

    def get_all_connections(self):
        neighbours = {}
        for vertex in self:
            neighbours[vertex.get_id()] = [(v.id, pos) for v, pos in vertex.get_connections()]
        return neighbours

    def build_from_configs(self, configs):
        self.add_vertex(configs[0])
        for config in configs[1]:
            self.add_edge(config[0], config[2], config[1])


def build_matrix(hall):
    matrix = []
    hall = hall.split(sep='\n')
    for line in hall[:-1]:
        temp = [seat for seat in line]
        matrix.append(temp)
    return matrix


def find_all_sitting_combinations(matrix, graph):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            temp_matrix = deepcopy(matrix)
            if matrix[row][col] == '.':
                name_deck = deque(graph.get_vertices())
                temp_matrix[row][col] = name_deck[0]
                graph.set_vertex_row(name_deck[0], row)
                graph.set_vertex_col(name_deck[0], col)
                build_pattern(temp_matrix, graph, name_deck)
            else:
                continue


def build_pattern(t_matrix, graph, name_deck):
    """Tries builds the sitting pattern from the current coordinates in the matrix.
     Builds a vertex and all of it's neighbours before moving to te next one.
     If a vertex has no neighbours, it has already been added."""
    curr_name = name_deck.popleft()
    neighbours = list(graph.get_all_connections()[curr_name])
    for i in range(len(neighbours)):
        n_row = graph.get_vertex_row(curr_name) + neighbours[i][1][0]
        n_col = graph.get_vertex_col(curr_name) + neighbours[i][1][1]
        if n_row < 0 or n_col < 0:
            return
        try:
            if t_matrix[n_row][n_col] == '.':
                t_matrix[n_row][n_col] = neighbours[i][0]
                graph.set_vertex_row(neighbours[i][0], n_row)
                graph.set_vertex_col(neighbours[i][0], n_col)
            else:
                return None
        except IndexError:
            return None
    if name_deck:
        build_pattern(t_matrix, graph, name_deck)
    else:
        print_results(t_matrix)
        global count
        count += 1
    

def print_results(matrix):
    for row in matrix:
        for elem in row:
            print(elem, end='')
        print('')
    print('-'*len(row))


def get_cinema_dimensions():
    while True:
        try:
            input_list = input("Enter number of rows & columns of the cinema:\n").strip('\n').split(' ')
            rows, columns = int(input_list[0]), int(input_list[1])
            break
        except ValueError:
            print("Error, invalid input detected!")
        except IndexError:
            pass
    return rows, columns


def get_cinema(dimensions):
    rows = dimensions[0]
    cols = dimensions[1]
    print("Valid characters: '.' - free, '*' - taken")
    cinema = ''
    for i in range(rows):
        row = input()
        while len(row) != cols or not validate_row(row):
            print('Number of seats per row must be {}\nTry again:\n!'.format(cols))
            row = input()
        cinema += row + '\n'
    return cinema


def validate_row(row):
    for char in row:
        if char != '.' and char != '*':
            return False
    return True


def get_num_config():
    while True:
        num_config = input('Enter number of configurations:\n')
        try:
            num_config = abs(int(num_config))
            return num_config
        except ValueError:
            print('Input must be an integer!')


def get_configurations(num_config):
    # No input validation has been made here, as we assume the inputs is correct..
    print('Start with a pivot name, afterwards enter configurations (one per line):')
    pivot = input().upper()
    configs = []
    for i in range(num_config):
        config = input()
        config.strip('\n')
        configs.append(config)
    return pivot, configs


count = 0


def main():
    dimensions = get_cinema_dimensions()
    matrix = build_matrix(get_cinema(dimensions))
    num_of_config = get_num_config()
    configurations = get_configurations(num_of_config)

    graph = Graph()
    graph.build_from_configs(configurations)

    find_all_sitting_combinations(matrix, graph)
    print(count)


if __name__ == '__main__':
    main()



