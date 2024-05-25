from turtle import*

screensize(500, 500)
bgcolor("black")
hideturtle()
title("PARA MI VALERIA HERMOSA")
penup()
goto(0, 0)
pendown()


def curvemove():
  for i in range(200):
    right(1)
    forward(1)

color("red")
begin_fill()
left(140)
forward(111.65)
curvemove()
left(120)
curvemove()
forward(111.65)
end_fill()

penup()
goto(0, -100)
pendown()
write("TE AMO VAL", align="center", font=("Times New Roman", 40, "normal"))

penup()
goto(-170, 50)
pendown()

write("V", align="center", font=("Times New Roman", 60, "normal"))

penup()
goto(170, 50)
pendown()

write("S", align="center", font=("Times New Roman", 60, "normal"))

mainloop()

# DE SEBITAS PARA TI :D
