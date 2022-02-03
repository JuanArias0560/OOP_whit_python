import random

def bubble_sort(list):
    n = len (list)

    for i in range(n):
        for j in range(0,n - i -1): #O(n) * O(n-i-1)=0(n**2) exponential
            if list[j] > list[j+1]:
                list[j],list[j+1]= list[j+1] , list[j]

    return list

if __name__=='__main__':
    list_size = int(input('How big will your list be?'))

    list= [random.randint(0,100) for i in range(list_size)] 
    print (list)

    sorted_list= bubble_sort(list) 
    print (sorted_list)