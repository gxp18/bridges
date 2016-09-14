import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['appdomain']['system_server']['fill'] = 'red'
G.add_edge('appdomain','system_server')
G.edge['appdomain']['system_server']['write-read'] = '[open open][write read][append read][setattr getattr][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open execmod][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read]'
G.edge['fixmo_app']['system_server']['fill'] = 'red'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['samsung_app']['system_server']['fill'] = 'red'
G.add_edge('samsung_app','system_server')
G.edge['samsung_app']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open]'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read]'
G.edge['untrusteddomain']['system_server']['fill'] = 'red'
G.add_edge('untrusteddomain','system_server')
G.edge['untrusteddomain']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()