from perro import Perro

class Bulldog(Perro):
    
    def __init__(self, peso, tipo) -> None:
        super().__init__(peso, tipo, 'Bulldog')