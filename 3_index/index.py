def find_max_index(array):
    ref = array[0]
    i = 0
    for j in range(len(array)-1):
        if ref < array[j+1]: 
            ref=array[j+1]
            i = j
    return i+1

if __name__ == '__main__':
    test = [1,2,1,3,5,6,4]
    print(find_max_index(test))
    