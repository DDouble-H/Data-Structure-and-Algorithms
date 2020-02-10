def sequential_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    print('값이 없습니다') # 수정필요


if __name__ == '__main__':
    
    import random
    
    data = random.sample(range(1, 100), 10)
    print(data)
    
    target = int(input("data 입력 :"))
    
    result = sequential_search(data, target)
    print('idx', result)
