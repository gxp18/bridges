import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()