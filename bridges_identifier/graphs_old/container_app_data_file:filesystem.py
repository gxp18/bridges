import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][relabelto relabelfrom]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
app = Viewer(G)
app.mainloop()