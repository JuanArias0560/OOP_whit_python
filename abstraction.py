class Washing_machine:
    
    def __init__(self):
        pass

    def wash(self,temp='Hot'):
        self._fill_water_tank(temp)
        self._add_soap()
        self._wash()
        self._centrifuge()

    def _fill_water_tank(self, temp):
        print(f'filling the water tank {temp}')

    def _add_soap(self):
        print('adding soap')

    def _wash(self):
        print('washing clothes')

    def _centrifuge(self):
        print('spinning the clothes')

if __name__=='__main__':
    washing_machine = Washing_machine()
    washing_machine.wash()
