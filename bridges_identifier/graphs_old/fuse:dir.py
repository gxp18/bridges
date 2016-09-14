import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init','newAttr1')
G.edge['init']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search]'
G.add_edge('init','newAttr1')
G.edge['init']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][add_name search][remove_name search]'
G.add_edge('init','qlogd')
G.edge['init']['qlogd']['write-read'] = '[add_name search]'
G.add_edge('init','qlogd')
G.edge['init']['qlogd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('newAttr1','qlogd')
G.edge['newAttr1']['qlogd']['write-read'] = '[open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('newAttr1','qlogd')
G.edge['newAttr1']['qlogd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','qlogd')
G.edge['newAttr1']['qlogd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['qlogd']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open execmod][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('newAttr1','qlogd')
G.edge['newAttr1']['qlogd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('newAttr1','qlogd')
G.edge['newAttr1']['qlogd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qlogd','newAttr1')
G.edge['qlogd']['newAttr1']['write-read'] = '[open open]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('qlogd','newAttr1')
G.edge['qlogd']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('qlogd','newAttr1')
G.edge['qlogd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['qlogd']['newAttr1']['fill'] = 'red'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['qlogd']['qlogd']['fill'] = 'red'
G.add_edge('qlogd','newAttr1')
G.edge['qlogd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('qlogd','newAttr1')
G.edge['qlogd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('qlogd','qlogd')
G.edge['qlogd']['qlogd']['write-read'] = '[open open][setattr getattr][write read][append read][setopt getopt][write read][open open][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][add_name search]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search]'
G.add_edge('system_server','qlogd')
G.edge['system_server']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open][append read][add_name search]'
G.add_edge('system_server','qlogd')
G.edge['system_server']['qlogd']['write-read'] = '[setopt getopt][write read][add_name search][open open][append read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()