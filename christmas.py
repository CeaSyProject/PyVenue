# Sử dụng module turtule - một module có sẵn trong python nên là bạn không cần tải thêm gì khác
# Module này có khă năng làm đồ họa cơ bản hay còn gọi là giao diện người dùng (như là tạo 1 cửa sổ trên Windows chả hạn)
import turtle

print("Giáng Sinh vui vẻ nhé!")

# Tạo một cửa sổ nhỏ
window = turtle.Screen()
tur=turtle.Turtle()
scr=tur.getscreen()
# Tên cửa sổ
scr.title("Merry Christmas - PyVenue")
scr.bgcolor("#32cd32")

tur.color("green")
tur.pensize(5)
tur.begin_fill()



# Nửa phải của cây
tur.forward(100)
tur.left(150)
tur.forward(90)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(40)
tur.left(150)
tur.forward(100)
tur.end_fill()

# Nửa trái
tur.begin_fill()
tur.left(60)
tur.forward(100)
tur.left(150)
tur.forward(40)
tur.right(150)
tur.forward(60)
tur.left(150)
tur.forward(60)
tur.right(150)
tur.forward(90)
tur.left(150)
tur.forward(133)
tur.end_fill()

# Thân cây
tur.color("brown")
tur.pensize(1)
tur.begin_fill()
tur.right(90)
tur.forward(80)
tur.right(90)
tur.forward(40)
tur.right(90)
tur.forward(80)
tur.end_fill()

# Trang trí
tur.penup()
tur.color("red")
tur.goto(110,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-120,-10)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("yellow")
tur.goto(100,40)
tur.begin_fill()
tur.circle(10)
tur.end_fill()



tur.penup()
tur.color("yellow")
tur.goto(-105,38)
tur.begin_fill()
tur.circle(10)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(85,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

tur.penup()
tur.color("red")
tur.goto(-95,70)
tur.begin_fill()
tur.circle(7)
tur.end_fill()

# Chuông (hay mấy hình tam giác trên lá)
tur.shape("triangle")
tur.fillcolor("yellow")
tur.goto(-20,30)
tur.setheading(90)
tur.stamp()
tur.fillcolor("red")
tur.goto(20,60)
tur.setheading(90)
tur.stamp()
tur.goto(-40,75)
tur.setheading(90)
tur.stamp()

# Hình ngôi sao
tur.speed(1)
tur.penup()
tur.color("yellow")
tur.goto(-20,110)
tur.begin_fill()
tur.pendown()

for i in range(5):
    tur.forward(40)
    tur.right(144)

tur.end_fill()

# Chiếu chữ lên cửa sổ
tur.penup()
message="Merry Christmas From PyVenue!!!"
tur.goto(-10,-180)
tur.color("White")
tur.pendown()
tur.write(message,move=False,align="center",font=("Arial",15,"bold"))
tur.hideturtle()
turtle.done()

