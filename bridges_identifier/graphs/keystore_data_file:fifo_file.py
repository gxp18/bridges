import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['keystore']['keystore']['fill'] = 'red'
G.add_edge('keystore','keystore')
G.edge['keystore']['keystore']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()