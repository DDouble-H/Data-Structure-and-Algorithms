def devide(x):
    
    if len(x) <= 1:
        return x
    
    mid_v = (len(x)//2)
    left_v = x[:mid_v]
    right_v = x[mid_v:]
    left = devide(left_v)
    right = devide(right_v)
    
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = 0
    j = 0
    
    while (i < len(left)) and (j < len(right)):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    while (i < len(left)):
            sorted_list.append(left[i])
            i += 1
    while (j < len(right)):
            sorted_list.append(right[j])
            j += 1
    
    return sorted_list

if __name__ == '__main__':
    
    import random
    
    before = random.sample(range(1, 100), 10)
    print('list', before)
    
    before = devide(before)
    print('sorted_list', before)
