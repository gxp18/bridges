import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][setattr getattr]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][setattr getattr][write read]'
G.edge['gad_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open execmod][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt]'
app = Viewer(G)
app.mainloop()