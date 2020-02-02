def bubble(x, ascending=True):


    if len(x) == 0: # X의 요소가 없는 경우 함수 실행 안함
        return False

    try:
        x = list(x) # X를 리스트로 변환할 수 없는 경우 함수 실행 안함
    except:
        return False

    if ascending: # ascending 인자의 값이 True인 경우 오름차순 정렬
        for i in range(0, len(x)-1):
            for j in range(0, len(x)-i-1):
                if x[j] > x[j+1]:
                    temp = x[j]
                    x[j] = x[j+1]
                    x[j+1] = temp
        return x

    else: # ascending 인자의 값이 True인 경우 내림차순 정렬
        for i in range(0, len(x)-1):
            for j in range(0, len(x)-i-1):
                if x[j] < x[j+1]:
                    temp = x[j]
                    x[j] = x[j+1]
                    x[j+1] = temp
        return x

if __name__ == '__main__':

    import random

    before = random.sample(range(1, 100), 10)
    print(before)

    after = bubble(before)
    print(after)

    before = random.sample(range(1, 100), 10)
    print(before)

    after = bubble(before, False)
    print(after)
