import matplotlib.pyplot as plt

fname = "Random.txt"
myx = []

with open(fname) as f:
    for line in f:
        myx.append(line)
f.close()     

#create histogram of our data
n, bins, patches = plt.hist(myx, 50, density=True, facecolor='g', alpha=0.75)

# plot formating options
plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)

#Show the figure
plt.show()