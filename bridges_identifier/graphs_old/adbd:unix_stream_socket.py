import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('domain','domain')
G.edge['domain']['domain']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setpgid getpgid][setcap getcap][setsched getsched][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read]'
G.edge['domain']['domain']['fill'] = 'red'
app = Viewer(G)
app.mainloop()