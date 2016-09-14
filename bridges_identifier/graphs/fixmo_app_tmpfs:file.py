import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][setattr getattr][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()