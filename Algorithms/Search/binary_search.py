def binary_search(data, target):
    
    start = 0
    end = len(data)-1
    mid = len(data)//2
    
    if data[mid] > target:
        # mid : 최댓값
        end = mid-1
    elif data[mid] < target:
        # mid : 최솟값
        start = mid+1
    else:
        return mid


if __name__ == '__main__':
    
    data = list(range(1,10))
    print(data)
    
    target = data[2]
    
    after = binary_search(data, target)
