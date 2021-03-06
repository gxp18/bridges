import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('qseecomd','rmt_storage')
G.edge['qseecomd']['rmt_storage']['write-read'] = '[open open]'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['qseecomd']['qseecomd']['fill'] = 'red'
G.add_edge('qseecomd','qseecomd')
G.edge['qseecomd']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('qseecomd','rmt_storage')
G.edge['qseecomd']['rmt_storage']['write-read'] = '[open open][write read]'
G.edge['qseecomd']['rmt_storage']['fill'] = 'red'
G.add_edge('qseecomd','rmt_storage')
G.edge['qseecomd']['rmt_storage']['write-read'] = '[open open][write read][append read]'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read]'
G.edge['rmt_storage']['qseecomd']['fill'] = 'red'
G.add_edge('rmt_storage','qseecomd')
G.edge['rmt_storage']['qseecomd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['rmt_storage']['rmt_storage']['fill'] = 'red'
G.add_edge('rmt_storage','rmt_storage')
G.edge['rmt_storage']['rmt_storage']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
app = Viewer(G)
app.mainloop()