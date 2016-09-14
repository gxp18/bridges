import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','knox_untrusted_app')
G.edge['init_shell']['knox_untrusted_app']['write-read'] = '[open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','knox_untrusted_app')
G.edge['init_shell']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','knox_untrusted_app')
G.edge['init_shell']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('init_shell','knox_untrusted_app')
G.edge['init_shell']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','init_shell')
G.edge['knox_untrusted_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open]'
G.add_edge('knox_untrusted_app','init_shell')
G.edge['knox_untrusted_app']['init_shell']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr]'
G.add_edge('knox_untrusted_app','init_shell')
G.edge['knox_untrusted_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['init_shell']['fill'] = 'red'
G.add_edge('knox_untrusted_app','init_shell')
G.edge['knox_untrusted_app']['init_shell']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read]'
G.edge['knox_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()