import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][open execmod][open open][write read][setopt getopt][open open][setattr getattr][open execmod][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()