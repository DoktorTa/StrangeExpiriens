class A:

    def alex(self, num):
        x = self.chech(num)
        if num in x:
            return True
        else:
            return False

    @staticmethod
    def chech(num):
        x = divisor_generator(num)
        n = num + 1
        seen = set()

        a = 3
        while len(seen) < n:
            for b in range(2, a):

                if (a * b) % (a + b) != 1:
                    continue

                alex_num = a * b * (a * b - 1) // (a + b)
                seen.add(alex_num)
                print(len(seen), (a, b), alex_num)

            if num in seen:
                return seen

            try:
                a = x.__next__()
            except StopIteration:
                return seen

        return seen


def divisor_generator(n):
    for i in range(1, n):
        if n % i == 0:
            yield i
    yield n


if __name__ == '__main__':
    print(A().alex(37506))
