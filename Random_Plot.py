import matplotlib.pyplot as plt
import numpy as np
import sys

def Rando_Plot(fname):
    myx = []
    with open(fname) as f:
        for line in f:
            value = (line.split('\n')[0])
            myx.append(float(value))
            
    #create histogram of our data
    n, bins, patches = plt.hist(myx,50, density=True, facecolor='g', alpha=0.75)


    # plot formating options
    plt.xlabel('Random Number: X')
    plt.ylabel('Probability')
    plt.title('Uniform random number')
    plt.grid(True)

    plt.show()

if __name__ == "__main__":
    
    file_name = sys.argv[1]
    Rando_Plot(str(file_name))