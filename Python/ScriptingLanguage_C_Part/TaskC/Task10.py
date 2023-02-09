def main(num: int):
    result = num
    for i in range(2, num):

        if i * i >= num:
            break

        if num % i == 0:
            while num % i == 0:
                num /= i
            result -= result // i

    if num > 1:
        result -= result // num
    return int(result)


if __name__ == '__main__':
    print(main(99))
