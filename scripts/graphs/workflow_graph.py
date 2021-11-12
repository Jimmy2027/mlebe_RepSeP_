from dataclasses import dataclass

from scripts.graphs import tikz


@dataclass
class Nodes:
    unprocessed_volume: str = r"Unprocessed\\ Volume"
    mlebe: str = "MLEBE"
    samri: str = r"SAMRI\\ workflow"
    processed_volume: str = r"Processed\\ Volume"


nodes = Nodes()
pic = tikz.Picture(

    'node/.style={ellipse, draw=black!60, very thick, minimum size=5mm},'

)

pic.set_node(text=nodes.unprocessed_volume, name='unprocessed_volume', options="node, align=center")
pic.set_node(text=nodes.mlebe, name='mlebe', options="node, right of=unprocessed_volume, xshift=6cm")
pic.set_node(text=nodes.samri, name='samri', options="node, right of=mlebe, xshift=5.8cm, align=center")
pic.set_node(text=nodes.processed_volume, name='processed_volume',
             options="node, right of=samri, xshift=6cm, align=center")

pic.set_line('unprocessed_volume', 'mlebe', edge_options='line width=0.1cm')
pic.set_line('unprocessed_volume', 'samri', edge_options='line width=0.1cm, bend left=40')

pic.set_line('mlebe', 'samri', edge_options='line width=0.1cm')

pic.set_line('samri', 'processed_volume', edge_options='line width=0.1cm')

output = pic.make()
print(output)
