from pathlib import Path
from scipy import ndimage

import nibabel as nib
import numpy as np
from matplotlib import pyplot as plt

bids_path = Path(
    '~/.scratch/mlebe/bids/sub-4005/ses-ofM/anat/sub-4005_ses-ofM_acq-TurboRARElowcov_T2w.nii.gz').expanduser()
bids_volume = np.array(nib.load(bids_path).dataobj)

masked_bids_path = Path(
    '~/.scratch/mlebe/preprocessing/masked_bids/sub-4005/ses-ofM/anat/masked_sub-4005_ses-ofM_acq-TurboRARElowcov_T2w.nii.gz').expanduser()
masked_bids_volume = np.array(nib.load(masked_bids_path).dataobj)

mask_path = Path(
    '~/.scratch/mlebe/preprocessing/masked_bids/sub-4005/ses-ofM/anat/mask_sub-4005_ses-ofM_acq-TurboRARElowcov_T2w.nii.gz').expanduser()
mask_volume = np.where(np.array(nib.load(mask_path).dataobj) >= 0.5, 1, 0)

preprocessed_volume_path = Path(
    '~/.scratch/hendrik/mlebe_threed/preprocessing/masked/sub-4005/ses-ofM/anat/sub-4005_ses-ofM_acq-TurboRARElowcov_T2w.nii.gz').expanduser()
preprocessed_volume = np.array(nib.load(preprocessed_volume_path).dataobj)

slice_idx = 10

save_dir = Path(__file__).parent.parent.parent / 'data/masking_examples'
save_dir.mkdir(exist_ok=True)

plt.imshow(np.swapaxes(bids_volume[..., slice_idx], 0, 1), cmap='Gray_r')
plt.axis('off')
plt.savefig(save_dir / 'bids_image.png', bbox_inches='tight', pad_inches=0)
plt.close()

plt.imshow(np.swapaxes(masked_bids_volume[..., slice_idx], 0, 1), cmap='Gray_r')
plt.axis('off')
plt.savefig(save_dir / 'masked_bids_image.png', bbox_inches='tight', pad_inches=0)
plt.close()

plt.imshow(np.swapaxes(mask_volume[..., slice_idx], 0, 1), cmap='Gray_r')
plt.axis('off')
plt.savefig(save_dir / 'mask_image.png', bbox_inches='tight', pad_inches=0)
plt.close()

plt.imshow(ndimage.rotate(np.swapaxes(preprocessed_volume, 1, 0)[56, ...], 90), cmap='Gray_r')
plt.axis('off')
plt.savefig(save_dir / 'preprocessed_image.png', bbox_inches='tight', pad_inches=0)
plt.close()
