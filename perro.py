from animal import Animal

class Perro(Animal):
    
    def __init__(self, peso, tipo, raza) -> None:
        super().__init__(peso, tipo)
        self.raza = raza

    def __str__(self) -> str:
        return super().__str__() + ' Raza: ' + self.raza
