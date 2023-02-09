class Alg:

    def __init__(self):
        with open("input.txt", "rb") as file:
            inc_c = 0
            inc_r = 0
            size, file = self.read_one(file)
            size = int(size)
            pole = self.pole_create(size)
            while inc_c != size:
                while inc_r != size:
                    way = file.read(6)
                    pole[inc_c][inc_r] = int(way)
                    file.seek(1, 1)
                    inc_r += 1
                file.seek(1, 1)
                inc_r = 0
                inc_c += 1
            start, file = self.read_one(file)
            end, file = self.read_one(file)
        print(int(start))
        self.fb_out(pole, int(start) - 1, int(end), size, size)

        # self.ford_bellman(ver)

    def read_one(self, file):
        s = b''
        sumbol = b''
        while sumbol != b'\n':
            s += sumbol
            sumbol = file.read(1)
        return s, file

    def ford_bellman(self, ver: dict, start: int, end: int):
        distans = {start: 0}
        pervision = {start: 0}
        for v in ver:
            distans = 1

    @staticmethod
    def generator_graf(size):
        ver = []
        for s in range(1, size + 1):
            ver.append(s)
        return ver

    def fb_out(self, pole: list, start: int, end: int, all_ver: int, size: int):
        d, p = self.fb_in(pole, start, all_ver, size)
        if d[end - 1] != -32768:
            print(d, "|", p)
        else:
            print("Not exists")

    def fb_in(self, pole: list, start: int, all_ver: int, size: int):
        d = [0 for x in range(size)]
        p = [0 for x in range(size)]
        ver = self.generator_graf(size)
        # ver.pop(start - 1)
        d[start] = 0
        p[start] = 0
        k = 1
        for v in ver:
            d[v - 1] = pole[start][v - 1]
            p[v - 1] = start
        for k in range(all_ver - 2):
            for v in ver:
                for w in range(all_ver):
                    if d[w] + pole[w][v - 1] < d[v - 1]:
                        d[v - 1] = d[w] + pole[w][v - 1]
                        p[v - 1] = w
        return d, p

    @staticmethod
    def pole_create(size):
        pole = [[0 for x in range(size)] for y in range(size)]
        return pole

def main():
    a = Alg()


if __name__ == '__main__':
    main()