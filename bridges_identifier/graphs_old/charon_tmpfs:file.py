import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('charon','charon')
G.edge['charon']['charon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['charon']['charon']['fill'] = 'red'
app = Viewer(G)
app.mainloop()