import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open]'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['gpsd']['gpsd']['fill'] = 'red'
G.add_edge('gpsd','gpsd')
G.edge['gpsd']['gpsd']['write-read'] = '[open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()