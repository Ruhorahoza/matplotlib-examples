import matplotlib.pyplot as plt

x = range (1, 50)

y = [value * 3 for value in x]

print ("value of x:")
print (range(1,50))
print ("value of y (thrice of x):")
print (y)

#plotlines and/or markers to the axes.

plt.plot(x,y)
# set the x axis label of the current axis.
plt.xlabel('x - axis')
#set the y axis label of current axis.
plt.ylabel('y - axis')
#set a title
plt.title('draw a line.')
#display the figure.
plt.show()


