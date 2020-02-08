def sequential_search(x, val):
    for i in range(len(x)):
        if x[i] == val:
            return i
        else: # 리스트에 값이 없을 때 (수정필요)
            print('값이 없습니다')

if __name__ == '__main__':
    import random
    
    before = random.sample(range(1, 100), 10)
    
    val = before[8]
    
    after = sequential_search(before, val)
    print('idx', after)   
