import turtle
# Crear el objeto tortuga y establecer su color, forma y posición 
class tortuga(turtle.Turtle):
    def __init__(self, color, shape, x, y):
        super().__init__()
        self.color(color)
        self.shape(shape)
        self.penup()
        self.goto(x, y)
        self.pendown()
        
# Establecer la posición de la tortuga(inicio y final)
    def posicion(self, x, y):
        self.goto(x, y)

# Mover la tortuga hacia adelante
    def mover(self, distancia):
        self.forward(distancia)

# Mover la tortuga hacia atrás
    def mover_atras(self, distancia):
        self.backward(distancia)

# Girar la tortuga a la izquierda
    def girar_izquierda(self, angulo):
        self.left(angulo)

# Girar la tortuga a la derecha
    def girar_derecha(self, angulo):
        self.right(angulo)  

# crear mi tortuga y establecer su color, forma y posición
mi_tortuga = tortuga("blue", "turtle", 0, 0)

# dibujar un cuadrado con la tortuga
mi_tortuga.mover(100)
mi_tortuga.girar_derecha(90)

mi_tortuga.mover(100)
mi_tortuga.girar_derecha(90)

mi_tortuga.mover(100)
mi_tortuga.girar_derecha(90)

mi_tortuga.mover(100)

# Mantener la ventana abierta
turtle.done()