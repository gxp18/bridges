import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('system','system')
G.edge['system']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system']['system']['fill'] = 'red'
G.add_edge('system','system_app')
G.edge['system']['system_app']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system']['system_app']['fill'] = 'red'
G.add_edge('system','s_system_app')
G.edge['system']['s_system_app']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system']['s_system_app']['fill'] = 'red'
G.add_edge('system','system')
G.edge['system']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('system','system_app')
G.edge['system']['system_app']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('system','s_system_app')
G.edge['system']['s_system_app']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('system_app','system')
G.edge['system_app']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system_app']['system']['fill'] = 'red'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system_app']['system_app']['fill'] = 'red'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['system_app']['s_system_app']['fill'] = 'red'
G.add_edge('system_app','system')
G.edge['system_app']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('system_app','system_app')
G.edge['system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('system_app','s_system_app')
G.edge['system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('s_system_app','system')
G.edge['s_system_app']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['s_system_app']['system']['fill'] = 'red'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['s_system_app']['system_app']['fill'] = 'red'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read]'
G.edge['s_system_app']['s_system_app']['fill'] = 'red'
G.add_edge('s_system_app','system')
G.edge['s_system_app']['system']['write-read'] = '[open open][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('s_system_app','system_app')
G.edge['s_system_app']['system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
G.add_edge('s_system_app','s_system_app')
G.edge['s_system_app']['s_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][send_msg recv_msg][setattr getattr][setopt getopt][sendto recvfrom][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][write read][setopt getopt]'
app = Viewer(G)
app.mainloop()