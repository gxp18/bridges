import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
app = Viewer(G)
app.mainloop()