import turtle

background = turtle.Screen()
background.setup(width = 1000, height = 1000)


graph_pen = turtle.Turtle()
graph_pen.hideturtle()
graph_pen.right(180)
graph_pen.speed(0)


def move(x,y):

    graph_pen.penup()

    graph_pen.goto(x,y)

    graph_pen.pendown()


def line_draw(xcor,ycor,xdiv,ydiv):

    graph_pen.shape('circle')

    graph_pen.resizemode('user')
    
    graph_pen.shapesize(.25,.25,.25)

    graph_pen.color('red')

    for x in range(0,len(xcor)):

        x_cor = xcor[x]

        x_cor = (x_cor * 50)/xdiv

        y_cor = ycor[x]

        y_cor = (y_cor * 50)/ydiv

        if x == 0:

            move(x_cor,y_cor)

            graph_pen.stamp()
        
        else:

            graph_pen.goto(x_cor,y_cor)

            graph_pen.stamp()


def graph_draw(average_x,average_y,xcor,ycor):

    if average_x <= 20:

        x_parameters = 25

    elif average_x <= 50:

        x_parameters = 10


    elif average_x <= 100:

        x_parameters = 5


    elif average_x <= 250:

        x_parameters = 2

    else:

        x_parameters = 1


    x_div = 50/x_parameters


    if average_y <= 20:

        y_parameters = 25

    elif average_y <= 50:

        y_parameters = 10

    elif average_y <= 100:

        y_parameters = 5

    elif average_y <= 250:

        y_parameters = 2

    else:

        y_parameters = 1


    y_div = 50/y_parameters


    start = -500

    move(start,0)

    graph_pen.stamp()
    
    graph_pen.setheading(0)

    for x in range(40):

        start = start + 25

        graph_pen.forward(25)

        if start != 0:

            hashes('x',start,x_parameters,y_parameters)

    start = -500

    graph_pen.stamp()

    graph_pen.right(90)

    move(0,start)

    graph_pen.stamp()

    graph_pen.right(180)

    for x in range(40):

        start = start + 25

        graph_pen.forward(25)

        if start != 0:

            hashes('y',start,x_parameters,y_parameters)

    graph_pen.stamp()

    graph_pen.setheading(0)

    line_draw(xcor,ycor,x_div,y_div)

    background.mainloop()


def hashes(x_or_y,start,x_parameters,y_parameters):

    if x_or_y == 'x':

        graph_pen.pencolor('light gray')

        graph_pen.sety(-500)

        graph_pen.sety(500)

        graph_pen.sety(15)

        graph_pen.pencolor('black')

        if start % 50 == 0:

            graph_pen.write((start/x_parameters), font=('Arial',10,'bold'))

        graph_pen.sety(-15)

        graph_pen.sety(0)

    else:

        graph_pen.pencolor('light gray')

        graph_pen.setx(-500)

        graph_pen.setx(500)

        graph_pen.setx(15)

        graph_pen.pencolor('black')

        if start % 50 == 0:

            graph_pen.write((start/y_parameters), font=('Arial',10,'bold'))

        graph_pen.setx(-15)

        graph_pen.setx(0)