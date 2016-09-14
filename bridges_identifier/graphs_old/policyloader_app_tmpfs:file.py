import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('policyloader_app','policyloader_app')
G.edge['policyloader_app']['policyloader_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['policyloader_app']['policyloader_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()