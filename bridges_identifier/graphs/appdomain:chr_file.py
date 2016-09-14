import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['trusted_app_domain']['trusted_app_domain']['fill'] = 'red'
G.add_edge('trusted_app_domain','trusted_app_domain')
G.edge['trusted_app_domain']['trusted_app_domain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()