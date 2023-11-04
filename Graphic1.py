from turtle import*
import colorsys
bgcolor("black")
width(2)
h=0.0
for i in range(250):
    speed=(25)
    c=colorsys.hsv_to_rgb(h,1,1)
    color(c)
    forward(i*2)
    right(121)
    h+=0.005
draw()
done()
