import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('system_domain','system_domain')
G.add_edge('system_domain','trusteddomain')
G.add_edge('trusteddomain','system_domain')
G.edge['trusteddomain']['system_domain']['read-write'] = '* >getattr'
G.add_edge('trusteddomain','trusteddomain')
G.edge['trusteddomain']['trusteddomain']['write-read'] = '[setattr getattr]'
G.add_edge('trusteddomain','system_domain')
G.edge['trusteddomain']['system_domain']['read-write'] = '* >read'
G.add_edge('trusteddomain','trusteddomain')
G.edge['trusteddomain']['trusteddomain']['write-read'] = '[setattr getattr][write read]'
G.edge['trusteddomain']['trusteddomain']['fill'] = 'red'
G.add_edge('trusteddomain','trusteddomain')
G.edge['trusteddomain']['trusteddomain']['write-read'] = '[setattr getattr][write read][append read]'
G.add_edge('trusteddomain','system_domain')
G.edge['trusteddomain']['system_domain']['read-write'] = '* >getopt'
G.add_edge('trusteddomain','trusteddomain')
G.edge['trusteddomain']['trusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()