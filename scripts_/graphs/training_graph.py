from dataclasses import dataclass

from scripts_.graphs import tikz


@dataclass
class Nodes:
    unprocessed_volume: str = r"Unprocessed\\ Data"
    template: str = r"Template\\ Mask"
    unet: str = r"U-Net"
    mask: str = "Mask"
    processed_volume: str = r"Processed\\ Data"
    error: str = "Error"


nodes = Nodes()
pic = tikz.Picture(

    'node/.style={ellipse, draw=black!60, very thick, minimum size=5mm},'
    'unet/.style={rectangle, draw=black!60, fill=gray!15, very thick, minimum size=15mm},'
    'mask/.style={ellipse, draw=green!60, fill=green!5, very thick, minimum size=25mm},'
    'error/.style={circle, draw=red!60, fill=red!5, very thick, minimum size=5mm},'
    'bluesquare/.style={rectangle, draw=blue!60, fill=blue!5, very thick, minimum height=100mm, minimum width=120mm},'

)

pic.set_node(text=nodes.unprocessed_volume, name='unprocessed_volume', options="node, align=center")
pic.set_node(text=nodes.processed_volume, name='processed_volume',
             options="node, right of=unprocessed_volume, align=center, xshift=9cm")

pic.set_node(name='bluesquare', options="bluesquare, right of=processed_volume, yshift=-2.8cm, xshift=10cm")

pic.set_node(text=nodes.unet, name='unet', options="unet, right of=processed_volume, xshift=6cm")
pic.set_node(text=nodes.mask, name='mask', options="mask, right of=unet, xshift=6cm")
pic.set_node(text=nodes.template, name='template', options="mask, below of=mask, yshift=-4.5cm, align=center")
pic.set_node(text=nodes.error, name='error', options="error, below of=unet, yshift=-4.5cm")

pic.set_line('unprocessed_volume', 'processed_volume', edge_options='line width=0.1cm', label="SAMRI",
             label_pos="south")
pic.set_line('processed_volume', 'unet', edge_options='line width=0.1cm')
pic.set_line('unet', 'mask', edge_options='line width=0.1cm', label="prediction", label_pos="south")
pic.set_line('mask', 'error', edge_options='line width=0.1cm')
pic.set_line('template', 'error', edge_options='line width=0.1cm')
pic.set_line('error', 'unet', edge_options='line width=0.1cm', label="Update",
             label_pos="south, xshift=-0.1cm, rotate=90")

output = pic.make()
print(output)
