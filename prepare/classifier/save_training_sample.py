from pathlib import Path
from matplotlib import pyplot as plt
import numpy as np
import random

data_dir = Path(__file__).parent.parent.parent / 'data/classifier'
x_train_path = data_dir / 'x_train.npy'
y_train_path = data_dir / 'y_train.npy'
x_train = np.load(x_train_path, allow_pickle=True)
y_train = np.load(y_train_path, allow_pickle=True)

# 
for i in range(10):
    plt.imshow(x_train[random.randint(0, len(x_train))])
    plt.show()
