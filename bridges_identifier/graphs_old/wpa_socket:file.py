import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][setopt getopt][open open]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][setopt getopt][open open][setattr getattr]'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read]'
G.edge['netd']['netd']['fill'] = 'red'
G.add_edge('netd','netd')
G.edge['netd']['netd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][write read][append read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][setopt getopt][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()