import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sysprof','sysprof')
G.edge['sysprof']['sysprof']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['sysprof']['sysprof']['fill'] = 'red'
app = Viewer(G)
app.mainloop()