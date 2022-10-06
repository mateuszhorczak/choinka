def choinka(x):
    left = x // 2
    stars = 1

    while True:
        print(' ' * left, end='')
        print('*' * stars, end='')
        print('')
        stars += 2
        left -= 1

        if left == -1:
            break


if __name__ == '__main__':
    choinka(5)
    choinka(9)
