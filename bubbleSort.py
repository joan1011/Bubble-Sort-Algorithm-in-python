def bubbleSort(array):
    issorted = False
    counter = 0
    while not issorted:
        issorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i,i+1,array)
                issorted = False
        counter = counter + 1
    return array
    
def swap(i,j,array):
    array[i],array[j] = array[j],array[i]
bubbleSort([-7, 2, 3, 8, -10, 4, -6, -10, -2, -7, 10, 5, 2, 9, -9, -5, 3, 8])
