import turtle

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        size /= 3
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)
        t.right(120)
        koch_curve(t, order-1, size)
        t.left(60)
        koch_curve(t, order-1, size)

def koch_snowflake(t, order, size):
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

if __name__ == "__main__":
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    order = 4  # Độ sâu đệ quy
    size = 300  # Kích thước cạnh của tam giác

    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()

    koch_snowflake(t, order, size)

    turtle.done()
