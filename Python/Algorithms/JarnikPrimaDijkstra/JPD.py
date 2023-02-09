import os


class JarikPrimDecstra:
    ves = 0

    def __init__(self):
        pass

    @staticmethod
    def serch_min(minimum_skeleton_graph: list):
        dist = 32767
        not_edge = 32767
        num_next_ver = 0
        num_now_ver = 0
        inc = 0

        for vertices in minimum_skeleton_graph:
            ver_min = min(vertices)
            if dist > ver_min:
                num_now_ver = inc
                dist = ver_min
            inc += 1

        if dist != not_edge:
            ver_curret = minimum_skeleton_graph[num_now_ver]
            num_next_ver = ver_curret.index(dist)
            ver_curret[num_next_ver] = not_edge

        return num_now_ver, num_next_ver, dist

    @staticmethod
    def tracker_skeleton_graph(matrix_skeleton_graph: list,
                               num_now_ver: int,
                               num_next_ver: int):
        curret_ver = matrix_skeleton_graph[num_now_ver]
        curret_ver[num_next_ver] = num_next_ver

        curret_ver = matrix_skeleton_graph[num_next_ver]
        curret_ver[num_now_ver] = num_now_ver

        return matrix_skeleton_graph

    def prim(self, matrix_graph, count_edge):
        hanged = [0]
        not_edge = 32767
        count_vertices = len(matrix_graph)
        minimum_skeleton_graph = [[32767 for x in range(count_vertices)] for y in range(count_vertices)]
        minimum_skeleton_graph[0] = matrix_graph[0]
        matrix_skeleton_graph = [[32767 for x in range(count_vertices)]
                                 for y in range(count_vertices)]

        for ver in range(count_edge):
            num_now_ver, num_next_ver, dist = self.serch_min(
                minimum_skeleton_graph)
            if (dist != not_edge) and (hanged.count(num_next_ver) == 0):
                matrix_skeleton_graph = self.tracker_skeleton_graph(
                    matrix_skeleton_graph, num_now_ver, num_next_ver)
                matrix_graph, minimum_skeleton_graph = \
                    self.translation_in_graphs(matrix_graph,
                                               minimum_skeleton_graph,
                                               num_now_ver,
                                               num_next_ver)
                hanged.append(num_next_ver)
        return matrix_skeleton_graph

    @staticmethod
    def translation_in_graphs(matrix_graph: list,
                              minimum_skeleton_graph: list,
                              num_now_ver: int,
                              num_next_ver: int) -> (list, list):
        ver = matrix_graph[num_next_ver]
        for vert in matrix_graph:
            vert[num_now_ver] = 32767
        # ver[index_ver_edge] = 32767
        minimum_skeleton_graph[num_next_ver] = ver
        return matrix_graph, minimum_skeleton_graph

    @staticmethod
    def create_matrix_graph(file_data: str) -> (list, int):
        matrix_graph = []
        vertices = []
        count_edge = 0

        file_parse_data = file_data.replace("\n", " ")
        file_parse_data = file_parse_data.split(" ")
        count_vertices = int(file_parse_data[0])

        for i in range(count_vertices):
            for j in range(count_vertices):
                num_vertices = count_vertices * i + j + 1
                len_edge = int(file_parse_data[num_vertices])
                if len_edge != 32767:
                    count_edge += 1
                vertices.append(len_edge)
            matrix_graph.append(vertices)
            vertices = []

        return matrix_graph, count_edge

    @staticmethod
    def file_read(file_path: str) -> str:
        with open(file_path, "r") as file:
            file_data = file.read()
            return file_data

    @staticmethod
    def print_to_file(matrix_skeleton_graph: list):
        not_edge = 32767
        now_ver = 1
        with open(os.path.dirname(os.path.abspath(__file__)) + "/out.txt", "w") as file:

            for i in matrix_skeleton_graph:
                file.write(str(now_ver) + " ")
                for j in i:
                    if j < not_edge:
                        file.write(str(j + 1) + " ")
                file.write(str(0) + "\n")
                now_ver += 1

    def start_alg(self, file_path: str):
        file_data = self.file_read(file_path)
        matrix_graph, count_edge = self.create_matrix_graph(file_data)
        matrix_skeleton_graph = self.prim(matrix_graph, count_edge)
        self.print_to_file(matrix_skeleton_graph)


if __name__ == '__main__':
    name = r"\in.txt"
    j = JarikPrimDecstra()
    j.start_alg(file_path=os.path.dirname(os.path.abspath(__file__)) + name)
