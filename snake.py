import turtle
import time
import random

posponer = 0.1

#Marcador.

puntos = 0
mejor_puntuacion = 0

#Configuracion De La Ventana.

wn = turtle.Screen()
wn.title("Juego De Snake")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Cabeza Serpiente.

cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("green")
cabeza.penup()
cabeza.goto(0,0)
cabeza.direction = "stop"

#Comida.

comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#Segmentos.

segmentos = []

#Texto.

texto = turtle.Turtle()
texto.speed(0)
texto.color("yellow")
texto.penup()
texto.hideturtle()
texto.goto(0,250)
texto.write("puntos:  0       mejor puntuacion:  0", align = "center", font = ("Courier", 16, "normal"))

#funciones.

def arriba():
    cabeza.direction = "up"
def abajo():
    cabeza.direction = "down"
def izquierda():
    cabeza.direction = "left"
def derecha():
    cabeza.direction = "right"

def mov():
    if cabeza.direction == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)
    if cabeza.direction == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)
    if cabeza.direction == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)
    if cabeza.direction == "right":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#teclado.

wn.listen()
wn.onkeypress(arriba, "Up")
wn.onkeypress(abajo, "Down")
wn.onkeypress(izquierda, "Left")
wn.onkeypress(derecha, "Right")
        


while True:
    wn.update()

    #Colisiones Bordes.

    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction = "stop"

        #Esconder Segmentos.

        for segmento in segmentos:
            segmento.goto(2000,2000)

        #limpiar lista.
        segmentos.clear()

        #Reset marcador.

        puntos = 0
        texto.clear()
        texto.write("puntos: {}       mejor puntuacion:  {}".format(puntos,mejor_puntuacion), 
                align = "center", font = ("Courier", 16, "normal"))    

    #Colisiones Comida.

    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)

        nuevo_segmento = turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("circle")
        nuevo_segmento.color("gray")
        nuevo_segmento.penup()        
        segmentos.append(nuevo_segmento)

        #Aumentar Marcador.

        puntos += 10

        if puntos > mejor_puntuacion:
            mejor_puntuacion = puntos

        texto.clear()
        texto.write("puntos: {}       mejor puntuacion:  {}".format(puntos,mejor_puntuacion), 
                align = "center", font = ("Courier", 16, "normal"))

    #Mover El Cuerpo. 
    
    totalSeg = len(segmentos)
    for index in range(totalSeg -1, 0, -1):
        x = segmentos[index -1].xcor()
        y = segmentos[index -1].ycor()
        segmentos[index].goto(x,y)

    if totalSeg > 0:            
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmentos[0].goto(x,y)

    mov()

    #Colisiones Con El Cuerpo.

    for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep(1)
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconde Segmentos
            for segmento in segmentos:
                segmento.goto(2000,2000)



            segmentos.clear()

            #Reset marcador.

            puntos = 0
            texto.clear()
            texto.write("puntos: {}       mejor puntuacion:  {}".format(puntos,mejor_puntuacion), 
                    align = "center", font = ("Courier", 16, "normal"))

    time.sleep(posponer)
