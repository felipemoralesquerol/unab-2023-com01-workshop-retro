class Animal():
    """
    Clase que representa a los animales
    """
    def __init__(self, peso, tipo) -> None:
        self.peso = peso
        self.tipo = tipo

    def __str__(self) -> str:
        return "Peso: " + str(self.peso) + " Tipo : " + self.tipo    