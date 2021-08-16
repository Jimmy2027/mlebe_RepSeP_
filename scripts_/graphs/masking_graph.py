from dataclasses import dataclass
from pathlib import Path

from scripts_.graphs import tikz

img_dir = Path('data/masking_examples')
bids_image_path = img_dir / 'bids_image.png'
masked_bids_image_path = img_dir / 'masked_bids_image.png'
mask_path = img_dir / 'mask_image.png'
preprocessed_image_path = img_dir / 'preprocessed_image.png'


@dataclass
class Nodes:
    bids_image: str = f'\\includegraphics[width=6cm]{{{str(bids_image_path)}}}'
    masked_image: str = f'\\includegraphics[width=5cm]{{{str(masked_bids_image_path)}}}'
    mask: str = f'\\includegraphics[width=5cm]{{{str(mask_path)}}}'
    preprocessed_image: str = f'\\includegraphics[width=7cm]{{{str(preprocessed_image_path)}}}'


nodes = Nodes()
pic = tikz.Picture(

    'empty/.style={minimum size=2mm},'

)

pic.set_node(text=nodes.bids_image, name='bids')
pic.set_node(name='placeholder1', options='right of=bids, xshift=8cm')
pic.set_node(text=nodes.masked_image, options='above of=placeholder1, yshift=3cm, xshift=3cm', name='masked')
pic.set_node(text=nodes.mask, options='below of=placeholder1, yshift=-3cm, xshift=3cm', name='mask')
pic.set_node(name='placeholder2', options='right of=placeholder1, xshift=5cm')
pic.set_node(text=nodes.preprocessed_image, options='right of=placeholder2,  xshift=8cm', name='preprocessed_image')

# todo consider using this fancy arrow: https://tex.stackexchange.com/questions/84143/fancy-arrows-with-tikz
pic.set_line('bids', 'placeholder1', label=r'\textbf{MLEBE}', label_pos='south, yshift=0.5cm, xshift=-0.4cm',
             edge_options='line width=0.5cm')
pic.set_line('placeholder2', 'preprocessed_image', label=r'\textbf{SAMRI}', label_pos='south, yshift=0.5cm, xshift=-0.4cm',
             edge_options='line width=0.5cm')

output = pic.make()
print(output)
