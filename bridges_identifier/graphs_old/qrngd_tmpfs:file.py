import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qrngd','qrngd')
G.edge['qrngd']['qrngd']['write-read'] = '[open open][write read][append read][write read]'
G.edge['qrngd']['qrngd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()