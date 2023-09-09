import matplotlib.pyplot as plt
xValues = list(range(1,101))
yValues = [x**3 for x in xValues]
print(xValues)
print(yValues)
plt.scatter(xValues,yValues,c=yValues,s=100,cmap=plt.cm.Blues)
plt.title("Cubes",fontsize=25)
plt.xlabel("Numbers",fontsize=10)
plt.ylabel("Cubes",fontsize=10)
plt.show()