import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('actlmand','actlmand')
G.edge['actlmand']['actlmand']['write-read'] = '[open open][add_name search][remove_name search][write read]'
G.edge['actlmand']['actlmand']['fill'] = 'red'
app = Viewer(G)
app.mainloop()