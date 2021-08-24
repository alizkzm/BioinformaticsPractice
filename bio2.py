import numpy as np
blues = np.arange(2,1000,2)
reds = np.arange(1,1000)

for blue in blues:
    for red in reds:
        p = red*(red-1)/((blue+red)*(blue+red-1))
        if (p==0.5):
            print(blue,red)