def all_perms(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def main():
    x = all_perms([1, 2, 3])
    for i in x:
        print(i)


if __name__ == '__main__':
    main()
