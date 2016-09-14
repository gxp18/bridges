import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read]'
app = Viewer(G)
app.mainloop()