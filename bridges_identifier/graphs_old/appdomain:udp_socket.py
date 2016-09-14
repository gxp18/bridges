import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][open open][write read][append read][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt]'
app = Viewer(G)
app.mainloop()