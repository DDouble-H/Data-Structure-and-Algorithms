import random


def bubble(x):
    type = input('ascending or descending:')

    if type == 'ascending':
        for i in range(0, len(x)-1):
            for j in range(0, len(x)-i-1):
                if x[j] > x[j+1]:
                    temp = x[j]
                    x[j] = x[j+1]
                    x[j+1] = temp

    elif type == 'descending':
        for i in range(0, len(x)-1):
            for j in range(0, len(x)-i-1):
                if x[j] < x[j+1]:
                    temp = x[j]
                    x[j] = x[j+1]
                    x[j+1] = temp

    else:
        print('error')


if __name__ == '__main__':
    x = random.sample(range(1, 100), 10)
    print(x)
    bubble(x)
    print(x)
