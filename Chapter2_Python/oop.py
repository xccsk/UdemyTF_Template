class CarData:
    def __init__(self,name: str,mf) -> None: #das ist eine Typernotaion, praktisch für automatische erweiterungen 
        self.name = name
        self.mf = mf
    
    def print_data(self):
        print('Name: ' + str(self.name))
        print(f"Modell: {self.mf}") #man nutzt immer f strings



class Audi(CarData):
    def __init__(self, name, ) ->None:
        super().__init__(name, 'Audi')

class Mercedes(CarData):
    def __init__(self, name) -> None:
        super().__init__(name, 'Mercedes')

def main():
    car1 = CarData('rs3','audi')
    car1.print_data()
    car2 = Audi('R8')
    car2.print_data()
    car3 = Mercedes('SLS')
    car3.print_data()

if __name__ == '__main__':
    main()

