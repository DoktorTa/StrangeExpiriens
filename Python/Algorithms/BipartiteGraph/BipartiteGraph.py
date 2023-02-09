INFINITY = 10000


def one_to_zero(x) -> int:
    return x - 1


def zero_to_one(x) -> int:
    return x + 1


def parse_line(s) -> list:
    ans = []
    t = s.split()
    for x in t:
        if len(x):
            ans.append(int(x))
    return ans


class BipartiteGraph:

    def __init__(self, filename: str):
        with open(filename, "r") as f:
            self.k, self.l = parse_line(f.readline())
            self.x_edges = {}
            self.n = int(f.readline())
            array_to_parse = []

            while True:
                line = f.readline()
                if "32767" in line:
                    array_to_parse.extend(parse_line(line)[:-1])
                    break
                array_to_parse.extend(parse_line(line))

            self.parse_x_array(array_to_parse)

    def parse_x_array(self, array):
        array = [one_to_zero(x) for x in array]
        bounds = array[:self.k + 1]

        for i in range(len(bounds) - 1):
            self.x_edges[i] = []
            start_bound = bounds[i]

            if start_bound == -1:
                continue

            end_bound = bounds[i+1]

            if end_bound == -1:
                end_bound = bounds[i+2]

            for j in range(start_bound, end_bound):
                self.x_edges[i].append(array[j])


class Graph:

    def __init__(self, graph: BipartiteGraph):
        self.bipartite_graph = graph
        self.pair_x = [-1] * self.bipartite_graph.k
        self.pair_y = [-1] * self.bipartite_graph.l
        self.used = set()

    def dfs(self, x) -> bool:

        if x in self.used:
            return False
        self.used.add(x)

        if x not in self.bipartite_graph.x_edges:
            return False

        for y in self.bipartite_graph.x_edges[x]:
            if self.pair_y[y] == -1 or self.dfs(self.pair_y[y]):
                self.pair_y[y] = x
                self.pair_x[x] = y
                return True

        return False

    def ford_Falkerson(self):
        is_path = True

        while is_path:
            is_path = False
            self.used = set()
            for x in [i for i in range(self.bipartite_graph.k)]:
                if self.pair_x[x] == -1:
                    if self.dfs(x):
                        is_path = True

        return [zero_to_one(i) for i in self.pair_x]


path = input("File: ")
bg = BipartiteGraph(path)
with open("out.txt", "w") as file:
    print(' '.join([str(i) for i in Graph(bg).ford_Falkerson()]), file=file)
