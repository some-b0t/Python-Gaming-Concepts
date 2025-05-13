import turtle
pen=turtle.Turtle()
pen.color("green")
pen.speed(1)
pen.fillcolor("green")
pen.begin_fill()
for base in range(4):
    pen.forward(200)
    pen.right(90)
pen.end_fill()
pen.color("orange")
pen.fillcolor("orange")
pen.begin_fill()
for roof in range(3):
    pen.forward(200)
    pen.left(120)
pen.end_fill()
turtle.done()