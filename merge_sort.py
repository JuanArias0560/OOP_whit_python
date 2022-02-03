import random


def merge_sort(list):
    if len(list)>1 :
        mid = len(list)//2
        left = list[:mid]       #llamada recursiva en cada mitad 
        rigth = list[mid:]
        print(left, '*' *5 ,rigth)

        merge_sort(left)
        merge_sort(rigth)

        #iteradores para recorrer las sublistas 
        i=0
        j=0
        #iterador para la lista principal 
        k=0

        while i< len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                list[k]= left[i]
                i += 1
            else:
                list[k] = rigth[j]
                j += 1
            
            k +=1

        while i < len(left):
            list[k] = left[i]
            i += 1 
            k  +=1

        while j < len(rigth):
            list[k] = rigth[j]
            j += 1
            k +=1

        print(f'left {left}, right {rigth}')
        print(list)
        print('-'*50)
        

    return list 


if __name__=='__main__':
    list_size= int(input('how big will the list be '))

    list=[random.randint(0,100) for i in range(list_size)]
    print(list)
    print('-' * 20 )

    list_sort = merge_sort(list)
    print (list_sort)