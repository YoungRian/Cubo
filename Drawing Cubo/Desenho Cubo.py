import turtle

class DesenhoCubo:
    
    def __init__(self):
        print("Iniciando desenho...")
    
    def startCube(self):
        
        #<- Definindo Nome do Turtle ->#
        t = turtle.Turtle()
        
        #<<-- Velocidade do Turle -->>#
        t.speed(7)
        
        #<<<--- Espessura da Caneta --->>>#
        t.pensize(2)
        
        #<<<--- Desenhar Quadrado --->>>#
        for i in range(4):
            t.forward(150)
            t.left(90)
    
        #<<<--- Desenhar partes para forma o cubo --->>>#
        t.left(45)
        t.forward(75)
        t.left(45)
        t.forward(150)
        t.right(90)
        t.forward(150)
        t.right(90)
        t.forward(150)
        t.right(45)
        t.forward(75)
        t.penup()
        t.right(135)
        t.forward(52)
        t.pendown()
        t.left(90)
        t.back(52)
        t.forward(150)
        t.penup()
        t.right(90)
        t.forward(150)
        t.left(135)
        t.pendown()
        t.forward(75)
        t.penup()
        t.left(135)
        t.forward(150)
        t.pendown()
        t.left(45)
        t.forward(75)
        t.penup()
        t.home()

        turtle.mainloop()   
        
Desenhar = DesenhoCubo()
Desenhar.startCube()