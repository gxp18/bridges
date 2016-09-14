import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bintvoutservice','bintvoutservice')
G.edge['bintvoutservice']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][write read]'
G.edge['bintvoutservice']['bintvoutservice']['fill'] = 'red'
app = Viewer(G)
app.mainloop()