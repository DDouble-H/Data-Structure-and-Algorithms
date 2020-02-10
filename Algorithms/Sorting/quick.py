def quick(x):
    
    if len(x) <= 1:
        return x
    
    pivot = x[len(x)//2]
    s_arr, m_arr, b_arr = [], [], []
    
    for i in x:
        if i < pivot:
            s_arr.append(i)
        elif i > pivot:
            b_arr.append(i)
        else:
            m_arr.append(i)
            
    x = quick(s_arr) + m_arr + quick(b_arr)
    
    return x


if __name__ == '__main__':
    import random

    before = random.sample(range(1, 100), 10)
    print('list', before)

    after = quick(before)
    print('sorted', after)
