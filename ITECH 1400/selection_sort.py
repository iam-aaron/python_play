def indexOfMax(l,start,end):
    ind = start
    max = l[start]
    for i in range(start,end):
        if (max < l[i]):
            max = l[i]
            ind = i
    return ind

def selectionSort(l):
    length = len(l)
    for i in range(0,length):
        print(l)
        largest = indexOfMax(l,0,length-i)
        l[largest],l[length-i-1] = l[length-i-1],l[largest]
        

unsorted_list = [5,3,8,6,7,2]
selectionSort(unsorted_list)


