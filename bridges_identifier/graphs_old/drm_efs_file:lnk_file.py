import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('insthk','insthk')
G.edge['insthk']['insthk']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('insthk','insthk')
G.edge['insthk']['insthk']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('insthk','insthk')
G.edge['insthk']['insthk']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['insthk']['insthk']['fill'] = 'red'
G.add_edge('insthk','insthk')
G.edge['insthk']['insthk']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()