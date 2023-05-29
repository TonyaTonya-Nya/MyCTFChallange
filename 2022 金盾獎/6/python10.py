from PIL import Image
import numpy as np

I = Image.open('./F1rsT@ke.png')
arr = np.array(I)

data = []

for i in arr:
    for j in i:
        if (str(j) == '[0 0 0]'):
            data.append(0)
        else:
            data.append(1)



print(''.join(str(x) for x in data))

