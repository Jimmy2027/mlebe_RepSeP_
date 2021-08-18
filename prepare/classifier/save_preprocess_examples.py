"""Save two volume slices overlayed with the template: one is preprocessed, the other not. """
import os
from pathlib import Path

import nibabel as nib
import numpy as np
from matplotlib import pyplot as plt
from mlebe.training.configs.utils import json_to_dict
from mlebe.training.dataio.loaders.utils import arrange_mask
from mlebe.training.dataio.loaders.utils import data_normalization

from make_config import CONFIG_PATH as config_path

config = json_to_dict(config_path)

example = 'sub-6570_ses-4mo_acq-TurboRARE_T2w.nii.gz'
slice = 65

dir = config['workflow_config']['data_path']

mask_dir = '/usr/share/mouse-brain-atlases/'

save_dir = Path('../data') / 'preprocessing_examples'
save_dir.mkdir(exist_ok=True)

in_data = [
    os.path.join(mask_dir, o)
    for o in os.listdir(mask_dir)
    if o == 'dsurqec_200micron_mask.nii'
]

in_data = np.sort(in_data)

for i in in_data:
    img = nib.load(i)
    orig_mask = img.get_data()
    orig_mask = np.moveaxis(orig_mask, 1, 0)

for o in os.listdir(dir):
    if o != 'irsabi' and not o.startswith('.') and not o.endswith('.xz') and not o.startswith('mlebe'):
        for x in os.listdir(os.path.join(dir, o)):
            if x.endswith('preprocessing'):
                for root, dirs, files in os.walk(os.path.join(dir, o, x)):
                    for file in files:
                        if file.endswith(example):
                            img = nib.load(os.path.join(root, file))
                            img_data = img.get_data()
                            img_data = np.moveaxis(img_data, 1, 0)
                            for t in ['unpreprocessed', 'preprocessed']:
                                if t == 'preprocessed':
                                    img_data = data_normalization(img_data)
                                    mask = arrange_mask(img_data, orig_mask)
                                else:
                                    mask = orig_mask

                                image = img_data[slice]
                                mask = mask[slice]

                                image = np.swapaxes(image, 0, 1)

                                image = np.flipud(image)
                                mask = np.swapaxes(mask, 0, 1)
                                mask = np.flipud(mask)

                                plt.imshow(np.squeeze(image), cmap='gray_r')
                                plt.imshow(np.squeeze(mask), alpha=0.3, cmap='Blues')
                                plt.axis('off')
                                plt.savefig(save_dir / f'{t}.png', bbox_inches='tight', pad_inches=0)
                                plt.close()
