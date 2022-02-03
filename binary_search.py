import random

def binary_search(list, start, end, objective):
    if start > end :
        return False
    
    mid= (start + end )//2

    if list[mid] == objective:
        return True 
    elif list[mid] <objective:
        return binary_search(list, mid + 1, end, objective)
    else:
        return binary_search(list , start,mid -1, objective) 

if __name__=='__main__':
    list_size = int(input('How big is your list?  '))
    objective = int(input('What number do you want to find? '))

    list=sorted([random.randint(0,100) for i in range(list_size)])

    find =binary_search(list,0, len(list), objective)

    print(list)
    print(f'The element {objective} {"is" if find else "isnt" } in the list ')