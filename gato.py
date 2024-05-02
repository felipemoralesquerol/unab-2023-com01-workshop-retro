from animal import Animal

class Gato(Animal):
    
    def __init__(self, peso, tipo, garra) -> None:
        super().__init__(peso, tipo)
        self.garra = garra
    
    def __str__(self) -> str:
        return super().__str__() + ' Garra: ' + self.garra

             