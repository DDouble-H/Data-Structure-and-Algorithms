def binary_search(data, target):

    start = 0
    end = len(data)-1
    mid = len(data)//2 

    while data[mid] != target:
        mid = (start+end)//2
        if data[mid] > target:
            end = mid-1
        elif data[mid] < target:
            start = mid+1
        else:
            return mid


if __name__ == '__main__':
    
    data = list(range(1,10))
    print(data)
    
    target = data[2]
    
    after = binary_search(data, target)
    print(after)
