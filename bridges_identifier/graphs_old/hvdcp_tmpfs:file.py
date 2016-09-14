import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('hvdcp','hvdcp')
G.edge['hvdcp']['hvdcp']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['hvdcp']['hvdcp']['fill'] = 'red'
app = Viewer(G)
app.mainloop()