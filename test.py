import turtle

# Screen
wn = turtle.Screen()
wn.title("My Game")
wn.bgcolor("Black")
wn.setup(width=800, height=800)


# Moving square
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, -380)
head.direction = "stop"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"

def move():
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
# Key bindings
wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")





while True:
    wn.update()
    move()


wn.mainloop()