import matplotlib.pyplot as plt 


a = [1, 2, 3, 4, 5] 
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21] 
plt.plot(a) 

# o is for circles and r is 
# for red 
plt.plot(b, "or") 

plt.plot(list(range(0, 22, 3))) 

# naming the x-axis 
plt.xlabel('Day ->') 

# naming the y-axis 
plt.ylabel('Temp ->') 

c = [4, 2, 6, 8, 3, 20, 13, 15] 
plt.plot(c, label = '4th Rep') 

# get current axes command 
ax = plt.gca() 

# get command over the individual 
# boundary line of the graph body 
ax.spines['right'].set_visible(False) 
ax.spines['top'].set_visible(False) 

# set the range or the bounds of 
# the left boundary line to fixed range 
ax.spines['left'].set_bounds(-3, 40) 

# set the interval by which 
# the x-axis set the marks 
plt.xticks(list(range(-3, 10))) 

# set the intervals by which y-axis 
# set the marks 
plt.yticks(list(range(-3, 20, 3))) 

# legend denotes that what color 
# signifies what 
ax.legend(['1st Rep', '2nd Rep', '3rd Rep', '4th Rep']) 

# annotate command helps to write 
# ON THE GRAPH any text xy denotes 
# the position on the graph 
plt.annotate('Temperature V / s Days', xy = (1.01, -2.15)) 

# gives a title to the Graph 
plt.title('All Features Discussed') 

plt.show() 
