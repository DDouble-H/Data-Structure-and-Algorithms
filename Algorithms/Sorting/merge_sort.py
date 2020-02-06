def devide(x):
    
    if len(x) <= 1:
        return x
    
    sorted_list = []
    
    mid_v = (len(x)//2) #중간
    
    left_v = x[:mid_v]#왼쪽
    right_v = x[mid_v:] #오른쪽
    
    left = devide(left_v)
    right = devide(right_v)
    
    return devide(left), devide(right)

def merge():
    pass

if __name__ == '__main__':
    
    import random
    
    before = random.sample(range(1, 100), 10)
#   print('list', before)
    
    after = devide(before)
#   print('list', after)
