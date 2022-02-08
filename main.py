import graph_draw as ghd

print("welcome to your quadratic calculator")


print("")


def vertex_form(vertexx,vertexy):

  x_coords = []
  
  y_coords = []

  for x in all_numbers:

    average_divider = 0

    x_total = 0

    x_total += x

    a = (vertexx-xint1)*(vertexx-xint2)

    a = vertexy/a

    #print(a)

    y = x*x + x*-xint1 + x*-xint2 + -xint2*-xint1

    y = y*a

    x_coords.append(x)

    y_coords.append(y)

    average_divider += 1

    print(str(x)+','+str(y))

    print("")

  x_average = x_total/average_divider

  absolute_vertex = abs(vertexy)

  print("standard form: y = "+str(a)+"x^2 + "+str(a*(-xint2+-xint1))+"x + "+str(a*(-xint1*-xint2)))

  print("intercept form: y = "+str(a)+"(x - "+str(xint1)+")(x - "+str(xint2)+")")

  print("vertex form: y = "+str(a)+"(x - "+str(vertexx)+")^2 + "+str(vertexy))

  print("")

  print("now drawing graph...")

  print("")

  ghd.graph_draw(x_average,absolute_vertex,x_coords,y_coords)


xints = input(("please enter your x-intercepts as 1x(smallest),2x(biggest): "))

xints = xints.split(",")

xint1 = int(xints[0])

xint2 = int(xints[1])

all_numbers = list(range(xint1-4,xint2+5))


print("")


vertex_present = input("do you have the vertex? Enter y or n: ")

if vertex_present == 'y':

  vertex = input("what is your vertex? Enter x,y: ")

  print("")

  vertex = vertex.split(",")

  vertex_form(int(vertex[0]),int(vertex[1]))

else:

  print("")

  yintercept = input("do you have the y-intercept? Enter y or n: ")


  if yintercept == 'y':

    yintercept = int(input("enter y-intercept: "))

    print("")

    a = yintercept/((-xint1)*(-xint2))

    line_of_sym = (xint1 + xint2)/2

    y = (line_of_sym - xint1)*(line_of_sym - xint2)

    y = y*a
  
    vertex_form(line_of_sym,y)

  else:

    print("")

    point = input("give me a point on your parabola in x,y form: ")

    print("")

    point = point.split(",")

    point1 = int(point[0])

    point2 = int(point[1])

    a = point2/((point1 - xint1)*(point1 - xint2))

    los = (xint1 + xint2)/2

    y = (los - xint1)*(los - xint2)

    y = y*a

    vertex_form(los,y)