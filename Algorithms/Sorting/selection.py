def selection(x, ascending=True):


    if len(x) == 0: # X의 요소가 없는 경우 함수 실행 안함
        return False

    try:
        x = list(x) # X를 리스트로 변환할 수 없는 경우 함수 실행 안함
    except:
        return False

    if ascending: # ascending 인자의 값이 True인 경우 오름차순 정렬
        for i in range(len(x)-1):
            min_index = i
            min_val = x[i]
            for j in range(min_index+1, len(x)):
                if min_val > x[j]:
                    min_val = x[i]
                    min_index = j
            x[min_index] = x[i]
            x[i] = min_val

        return x

if __name__ == '__main__':

    import random

    before = random.sample(range(1, 100), 10)
    print(before)

    after = selection(before)
    print(after)

    before = random.sample(range(1, 100), 10)
    print(before)

    after = selection(before, False)
    print(after)
