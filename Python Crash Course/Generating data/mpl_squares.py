import matplotlib.pyplot as plt
numbers = [1,4,9,16,25]
plt.plot(numbers,linewidth=5)
plt.title("Numbers",fontsize = 24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Numbers",fontsize=14)
plt.tick_params(axis="both",labelsize=14)
plt.show()