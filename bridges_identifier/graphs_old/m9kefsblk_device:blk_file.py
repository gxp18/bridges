import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['init_shell']['efsks']['fill'] = 'red'
G.add_edge('init_shell','efsks')
G.edge['init_shell']['efsks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['init_shell']['ks']['fill'] = 'red'
G.add_edge('init_shell','ks')
G.edge['init_shell']['ks']['write-read'] = '[open open][write read][add_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['init_shell']['qcks']['fill'] = 'red'
G.add_edge('init_shell','qcks')
G.edge['init_shell']['qcks']['write-read'] = '[open open][write read][add_name search][remove_name search][add_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open]'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['ks']['efsks']['fill'] = 'red'
G.add_edge('ks','efsks')
G.edge['ks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['ks']['init_shell']['fill'] = 'red'
G.add_edge('ks','init_shell')
G.edge['ks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['ks']['ks']['fill'] = 'red'
G.add_edge('ks','ks')
G.edge['ks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read]'
G.edge['ks']['qcks']['fill'] = 'red'
G.add_edge('ks','qcks')
G.edge['ks']['qcks']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open][write read]'
G.edge['qcks']['efsks']['fill'] = 'red'
G.add_edge('qcks','efsks')
G.edge['qcks']['efsks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['qcks']['init_shell']['fill'] = 'red'
G.add_edge('qcks','init_shell')
G.edge['qcks']['init_shell']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['qcks']['ks']['fill'] = 'red'
G.add_edge('qcks','ks')
G.edge['qcks']['ks']['write-read'] = '[open open][write read][add_name search][open open][write read][add_name search][open open][append read][open open][write read][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['qcks']['qcks']['fill'] = 'red'
G.add_edge('qcks','qcks')
G.edge['qcks']['qcks']['write-read'] = '[open open][write read][append read][open open][add_name search][remove_name search][open open][write read][add_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()