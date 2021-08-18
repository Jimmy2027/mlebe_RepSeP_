from dataclasses import dataclass
from pathlib import Path

from scripts_.graphs import tikz
import glob

data_dir = Path('data/reg_comp')
generic_paths = sorted(glob.glob(str(data_dir / 'generic*')))
masked_paths = sorted(glob.glob(str(data_dir / 'masked*')))

pic = tikz.Picture(

    'empty/.style={text width=1cm},'

)

pic.set_node(text=r'\small{\textbf{Generic}}', name='generic', options='empty')
pic.set_node(text=r'\small{\textbf{Masked}}', name='masked', options='empty ,below of=generic, yshift=-2.5cm')
x_offset = 3
for generic_path, masked_path in zip(generic_paths, masked_paths):
    pic.set_node(text=f'\\includegraphics[width=2.5cm]{{{str(generic_path)}}}',
                 options=f'right of=generic, xshift = {x_offset}cm')
    pic.set_node(text=f'\\includegraphics[width=2.5cm]{{{str(masked_path)}}}',
                 options=f'right of=masked, xshift = {x_offset}cm')
    x_offset += 3

output = pic.make()
print(output)
