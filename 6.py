from turtle import *

screensize(10000, 10000)
tracer(100)
pensize(4)
n= 15
down()

for i in range(8):
    right(45)
    forward(n * 8)


up()
for x in range(-30,30):
    for y in range(-30,30):
        goto(n * x, n * y)
        dot(6, "red")
done()