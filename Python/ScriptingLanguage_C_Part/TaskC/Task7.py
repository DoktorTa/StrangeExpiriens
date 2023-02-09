import os


def main(file_name: str, *args):
    path = os.path.dirname(os.path.abspath(__file__))
    with open(path + file_name, "wb") as file_all:
        for name_file in args:
            write_file_in_file_all(file_all, path + name_file)


def write_file_in_file_all(file_all, name_file: str):
    file_read_size = os.path.getsize(name_file)

    with open(name_file, "rb") as file_read:

        while file_read_size // 1024 != 0:
            read = file_read.read(1024)
            file_all.write(read)
            file_read_size -= 1024

        read = file_read.read(file_read_size)
        file_all.write(read)


if __name__ == '__main__':
    main(r"/Task7_all.txt", r"/Task7_1.txt", r"/Task7_2.txt")
