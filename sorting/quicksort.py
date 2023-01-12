import random

def partition(array, low, high):

    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    
    return i + 1

def sort(array):
    sort_util(array,0 , len(array)-1)

def sort_util(array, l, r):
    if l >= r:
        return


    pivot = partition(array, l, r)
    
    sort_util(array, l, pivot-1)
    sort_util(array, pivot+1, r)
    
if __name__ == "__main__":
    lst = [random.randrange(100) for _ in range(10)]
    sort(lst)
    print(lst)