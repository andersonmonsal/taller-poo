class Cuadro:
    def __init__(self):
        self.lanzamientos = []

    def agregar_lanzamiento(self, pines):
        self.lanzamientos.append(pines)

    def es_strike(self):
        return len(self.lanzamientos) == 1 and self.lanzamientos[0] == 10

    def es_spare(self):
        return len(self.lanzamientos) == 2 and sum(self.lanzamientos) == 10


class Juego:
    def __init__(self):
        self.cuadros = [Cuadro() for _ in range(10)]
        self.cuadro_actual = 0

    def lanzar(self, pines):
        cuadro = self.cuadros[self.cuadro_actual]
        cuadro.agregar_lanzamiento(pines)
        if cuadro.es_strike() or len(cuadro.lanzamientos) == 2:
            self.cuadro_actual += 1

    def calcular_puntaje(self):
        puntaje = 0
        indice_cuadro = 0
        for cuadro in self.cuadros:
            puntaje += sum(cuadro.lanzamientos)
            if cuadro.es_strike():
                if indice_cuadro < 9:
                    siguiente_cuadro = self.cuadros[indice_cuadro + 1]
                    puntaje += sum(siguiente_cuadro.lanzamientos[:2])
                    if siguiente_cuadro.es_strike() and indice_cuadro < 8:
                        puntaje += self.cuadros[indice_cuadro + 2].lanzamientos[0]
                elif indice_cuadro == 9:
                    puntaje += sum(cuadro.lanzamientos)
            elif cuadro.es_spare():
                if indice_cuadro < 9:
                    puntaje += self.cuadros[indice_cuadro + 1].lanzamientos[0]
                elif indice_cuadro == 9:
                    puntaje += self.cuadros[indice_cuadro].lanzamientos[2]
            indice_cuadro += 1
        return puntaje


juego = Juego()
juego.lanzar(10)
juego.lanzar(5)
juego.lanzar(5)
juego.lanzar(9)
juego.lanzar(0)
print("Puntaje total:", juego.calcular_puntaje())

