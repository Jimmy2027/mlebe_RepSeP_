from dataclasses import dataclass

from scripts_.graphs import tikz


@dataclass
class Nodes:
    unprocessed_volume: str = r"Unprocessed\\ Volume"
    template: str = "Template Mask"
    unet: str = r"U-Net"
    mask: str = "Mask"
    processed_volume: str = r"Processed\\ Volume"
    error: str = "Error"


nodes = Nodes()
pic = tikz.Picture(

    'node/.style={ellipse, draw=black!60, very thick, minimum size=5mm},'
    'mask/.style={ellipse, draw=green!60, fill=green!5, very thick, minimum size=5mm},'
    'error/.style={ellipse, draw=red!60, fill=red!5, very thick, minimum size=5mm},'

)

pic.set_node(text=nodes.unprocessed_volume, name='unprocessed_volume', options="node, align=center")
pic.set_node(text=nodes.processed_volume, name='processed_volume',
             options="node, right of=unprocessed_volume, align=center, xshift=9cm")
pic.set_node(text=nodes.template, name='template', options="mask, right of=mask, yshift=0cm, xshift=1cm")
pic.set_node(text=nodes.unet, name='unet', options="node, right of=processed_volume, xshift=6cm")
pic.set_node(text=nodes.mask, name='mask', options="mask, right of=unet, xshift=6cm")
pic.set_node(text=nodes.error, name='error', options="error, right of=template, xshift=13cm")

pic.set_line('unprocessed_volume', 'processed_volume', edge_options='line width=0.1cm', label="SAMRI",
             label_pos="south")
pic.set_line('processed_volume', 'unet', edge_options='line width=0.1cm')
pic.set_line('unet', 'mask', edge_options='line width=0.1cm', label="prediction", label_pos="north")
pic.set_line('mask', 'error', edge_options='line width=0.1cm')
pic.set_line('template', 'error', edge_options='line width=0.1cm')
pic.set_line('error', 'unet', edge_options='line width=0.1cm, bend right= 30', label="Update",
             label_pos="north, xshift=0.7cm, rotate=30")

output = pic.make()
print(output)
