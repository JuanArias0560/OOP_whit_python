class Person():

    def __init__(self, name):
        self.name = name
    
    def get_moving(self):
        print('Im walking')

class Cyclist(Person):

    def __init__(self, name):
        super().__init__(name)

    def get_moving(self):
        print('Im moving on my bike')

def main():
    person1=Person('David')
    person1.get_moving()

    cyclist=Cyclist('Daniel')
    cyclist.get_moving()
        
if __name__=='__main__':
    main()

