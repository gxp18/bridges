import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('platform_app','dumpstate')
G.edge['platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['platform_app']['dumpstate']['fill'] = 'red'
G.add_edge('platform_app','irm_platform_app')
G.edge['platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['platform_app']['platform_app']['fill'] = 'red'
G.add_edge('platform_app','platform_app')
G.edge['platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['platform_app']['platform_app']['fill'] = 'red'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('platform_app','s_platform_app')
G.edge['platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','dumpstate')
G.edge['s_platform_app']['dumpstate']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['s_platform_app']['dumpstate']['fill'] = 'red'
G.add_edge('s_platform_app','irm_platform_app')
G.edge['s_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][write read]'
G.edge['s_platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['s_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','platform_app')
G.edge['s_platform_app']['platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['s_platform_app']['platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['s_platform_app']['s_platform_app']['fill'] = 'red'
G.add_edge('s_platform_app','s_platform_app')
G.edge['s_platform_app']['s_platform_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read]'
G.edge['s_platform_app']['s_platform_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()