import random


def lineal_search(list,objective):
    match = False

    for element in list: #O(n)
        if element == objective:
            match= True
            break

    return match 

if __name__=='__main__':
    list_size= int(input('how big will the list be? '))
    objective = int(input('how number you will witch'))

    list=[random.randint(0,100) for i in range(list_size)]
    find=lineal_search(list,objective)
    print(list)

    print(f'the element {objective} {"esta" if find else "no esta"} en la lista ')