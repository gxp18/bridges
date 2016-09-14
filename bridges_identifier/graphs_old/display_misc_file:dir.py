import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mm-pp-daemon']['surfaceflinger']['fill'] = 'red'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-pp-daemon','mm-pp-daemon')
G.edge['mm-pp-daemon']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-pp-daemon','surfaceflinger')
G.edge['mm-pp-daemon']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['mm-pp-daemon']['fill'] = 'red'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['surfaceflinger']['surfaceflinger']['fill'] = 'red'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('surfaceflinger','mm-pp-daemon')
G.edge['surfaceflinger']['mm-pp-daemon']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('surfaceflinger','surfaceflinger')
G.edge['surfaceflinger']['surfaceflinger']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()