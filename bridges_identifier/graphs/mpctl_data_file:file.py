import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mpdecision']['mpdecision']['fill'] = 'red'
G.add_edge('mpdecision','mpdecision')
G.edge['mpdecision']['mpdecision']['write-read'] = '[write read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mpdecision']['perfd']['fill'] = 'red'
G.add_edge('mpdecision','perfd')
G.edge['mpdecision']['perfd']['write-read'] = '[write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['perfd']['mpdecision']['fill'] = 'red'
G.add_edge('perfd','mpdecision')
G.edge['perfd']['mpdecision']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read]'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['perfd']['perfd']['fill'] = 'red'
G.add_edge('perfd','perfd')
G.edge['perfd']['perfd']['write-read'] = '[open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()