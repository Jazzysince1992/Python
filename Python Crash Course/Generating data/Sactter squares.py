import matplotlib.pyplot as plt
xValues = list(range(1,11))
yValues = [x**2 for x in xValues]
plt.scatter(xValues,yValues,edgecolors="none",c=yValues,s=25,cmap=plt.cm.Blues)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis="both",which="major",labelsize=14)
plt.show()