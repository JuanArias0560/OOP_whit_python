class Car:

    def __init__(self,model,brand, color):
        self.model = model
        self.brand = brand
        self.color = color 
        self._condition= 'Resting'
        self._engine = Engine(cylinders=4)

    def speed_up(self,type='Slow'):
        if type=='Fast':
            self._engine.inject_gasoline(10)
        else:
            self._engine.inject_gasoline(3)

        self._condition = 'moving'

class Engine:

    def __init__(self,cylinders, type='gasoline'):
        self.cylinders = cylinders
        self.type = type
        self._temperature = 0

    def inject_gasoline():
        pass