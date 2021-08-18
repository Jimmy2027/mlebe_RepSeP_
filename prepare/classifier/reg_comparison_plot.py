import os
from pathlib import Path

import nibabel as nib
import pandas as pd
from matplotlib import pyplot as plt

table = pd.DataFrame(
    [['sub-4005_ses-ofMaF_acq-TurboRARElowcov_T2w', 61], ['sub-4001_ses-ofMcF2_acq-TurboRARElowcov_T2w', 42],
     ['sub-4001_ses-ofMcF2_acq-TurboRARElowcov_T2w', 41], ['sub-4001_ses-ofMcF2_acq-TurboRARElowcov_T2w', 61],
     ['sub-4009_ses-ofMcF1_acq-TurboRARElowcov_T2w', 61],
     ['sub-4001_ses-ofMcF2_acq-TurboRARElowcov_T2w', 33]], columns=['volume', 'slice'], index=[1, 2, 3, 4, 5, 6])

preprocessed_folders = [os.path.expanduser('~/.scratch/hendrik/mlebe_threed/preprocessing/generic'),
                        os.path.expanduser('~/.scratch/hendrik/mlebe_threed/preprocessing/masked')]

template_path = '/usr/share/mouse-brain-atlases/dsurqec_200micron_mask.nii'
template_volume = nib.load(template_path).dataobj

generic_preprocessed_list = []
masked_preprocessed_list = []

for preprocessed_folder in preprocessed_folders:
    for root, dirs, files in os.walk(preprocessed_folder):
        for file in files:
            if file.split('.')[0] in table['volume'].to_list():
                file_path = '/'.join([root, file])
                subject = file.split('_')[0]
                if 'generic' in file_path:
                    table.loc[table['volume'] == file.split('.')[0], 'generic_path'] = file_path
                elif 'masked' in file_path:
                    table.loc[table['volume'] == file.split('.')[0], 'masked_path'] = file_path

save_dir = Path(__file__).parent.parent.parent / 'data/reg_comp'
save_dir.mkdir(exist_ok=True)

for idx, row in table.iterrows():
    volume = nib.load(row['generic_path']).dataobj
    plt.imshow(volume[:, row.slice, :], cmap='gray_r')
    plt.imshow(template_volume[:, row.slice, :], alpha=0.4, cmap='Blues')
    plt.axis('off')
    plt.savefig(save_dir / f'generic_{str(Path(row["generic_path"]).name).replace(".nii.gz", "")}_{row.slice}.png', bbox_inches='tight',
                pad_inches=0)
    plt.close()
    volume = nib.load(row['masked_path']).dataobj
    plt.imshow(volume[:, row.slice, :], cmap='gray_r')
    plt.imshow(template_volume[:, row.slice, :], alpha=0.4, cmap='Blues')
    plt.axis('off')
    plt.savefig(save_dir / f'masked_{str(Path(row["masked_path"]).name).replace(".nii.gz", "")}_{row.slice}.png', bbox_inches='tight', pad_inches=0)
    plt.close()
