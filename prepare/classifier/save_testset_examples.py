from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt

seed = 2
data_dir = Path('../data')
clf_datadir = data_dir / 'classifier'

x_test = np.load(clf_datadir / 'x_test.npy', allow_pickle=True)
y_test = np.load(clf_datadir / 'y_test.npy', allow_pickle=True)
y_pred = np.load(clf_datadir / 'y_pred.npy', allow_pickle=True)
np.random.seed(seed)
np.random.shuffle(x_test)
np.random.seed(seed)
np.random.shuffle(y_test)
np.random.seed(seed)
np.random.shuffle(y_pred)

for key, nbr_images in {'small': 6, 'big': 13}.items():
    list = [[x_test[:nbr_images]], [y_test[:nbr_images]], [y_pred[:nbr_images]]]

    for img in range(len(list[0])):
        patches = []
        for item in list:
            patch = item[img][0] * 255
            for slice in range(1, item[img].shape[0]):
                temp = item[img][slice] * 255
                patch = np.hstack((patch, temp))
            patches.append(patch)
        patch = patches[0]
        for i in range(1, len(patches)):
            patch = np.vstack((patch, patches[i]))
        image = np.vstack(patches)
        plt.figure()
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.savefig(data_dir / f'testset_examples_{key}.png', bbox_inches='tight', pad_inches=0)
