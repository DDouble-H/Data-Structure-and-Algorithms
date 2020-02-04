def insertion(x, ascending=True):

    if len(x) == 0: # X의 요소가 없는 경우 함수 실행 안함
        return False

    try:
        x = list(x) # X를 리스트로 변환할 수 없는 경우 함수 실행 안함
    except:
        return False
    
    if ascending: # ascending 인자의 값이 True인 경우 오름차순 정렬
        for i in range(1, len(x)): 
            j = i-1
            key = x[i]
            while x[j] > key and j>=0:
                x[j+1] = x[j]
                j = j-1
            x[j+1] = key

        return x
    
    else:
        for i in range(1, len(x)): 
            j = i-1
            key = x[i]
            while x[j] < key and j>=0:
                x[j+1] = x[j]
                j = j-1
            x[j+1] = key

        return x


if __name__ == '__main__':

    import random

    before = random.sample(range(1, 100), 10)
    print('list',before)

    after = insertion(before)
    print('ascending',after)

    before = random.sample(range(1, 100), 10)
    print('list',before)

    after = insertion(before, False)
    print('descending',after)
