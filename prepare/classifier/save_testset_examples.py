from pathlib import Path

import matplotlib
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
    map = {'x_test': x_test[:nbr_images], 'y_test': y_test[:nbr_images], 'y_pred': y_pred[:nbr_images]}

    fig = plt.figure(figsize=(nbr_images, 2), constrained_layout=True)
    grid = fig.add_gridspec(2, nbr_images, wspace=0, hspace=0)
    for (y_step, x_step), ax in np.ndenumerate(grid.subplots()):
        if y_step == 0:
            ax.imshow(x_test[x_step], cmap='gray_r')
        else:
            diff_ytest = np.where(y_test[x_step] - y_pred[x_step] > 0, 1, 0)
            diff_ypred = np.where(y_test[x_step] - y_pred[x_step] < 0, 2, 0)
            overlap = np.where(y_test[x_step] + y_pred[x_step] == 2, 3, 0)
            data = diff_ypred + diff_ytest + overlap

            ax.imshow(data, cmap=matplotlib.colors.ListedColormap(['white', 'green', 'red', 'whitesmoke']))
            # ax.imshow(diff_ytest, cmap=matplotlib.colors.ListedColormap(['white', 'red']))
            # ax.imshow(overlap, cmap=matplotlib.colors.ListedColormap(['white', 'blue']), alpha=0.4)
        ax.axis('off')
    # plt.show()
    plt.savefig(data_dir / f'testset_examples_{key}.png', bbox_inches='tight', pad_inches=0)
