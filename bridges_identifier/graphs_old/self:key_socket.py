import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('domain','domain')
G.add_edge('domain','racoon')
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >getattr'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >read'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['racoon']['racoon']['fill'] = 'red'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read]'
G.add_edge('racoon','domain')
G.edge['racoon']['domain']['read-write'] = '* >getopt'
G.add_edge('racoon','racoon')
G.edge['racoon']['racoon']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()