import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('fixmo_app','mediaserver')
G.edge['fixmo_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('fixmo_app','nfc')
G.edge['fixmo_app']['nfc']['write-read'] = '[open open]'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','sensorhubservice')
G.edge['fixmo_app']['sensorhubservice']['write-read'] = '[open open]'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('fixmo_app','bintvoutservice')
G.edge['fixmo_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['fixmo_app']['bluetooth']['fill'] = 'red'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['fixmo_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('fixmo_app','commonplatformappdomain')
G.edge['fixmo_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['drmserver']['fill'] = 'red'
G.add_edge('fixmo_app','drmserver')
G.edge['fixmo_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['good_app']['fill'] = 'red'
G.add_edge('fixmo_app','good_app')
G.edge['fixmo_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','mediaserver')
G.edge['fixmo_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['fixmo_app']['mediaserver']['fill'] = 'red'
G.add_edge('fixmo_app','mediaserver')
G.edge['fixmo_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('fixmo_app','nfc')
G.edge['fixmo_app']['nfc']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['nfc']['fill'] = 'red'
G.add_edge('fixmo_app','nfc')
G.edge['fixmo_app']['nfc']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['radio']['fill'] = 'red'
G.add_edge('fixmo_app','radio')
G.edge['fixmo_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','sensorhubservice')
G.edge['fixmo_app']['sensorhubservice']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['sensorhubservice']['fill'] = 'red'
G.add_edge('fixmo_app','sensorhubservice')
G.edge['fixmo_app']['sensorhubservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['fixmo_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('fixmo_app','surfaceflinger')
G.edge['fixmo_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['fixmo_app']['system_server']['fill'] = 'red'
G.add_edge('fixmo_app','system_server')
G.edge['fixmo_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('good_app','mediaserver')
G.edge['good_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open]'
G.add_edge('good_app','nfc')
G.edge['good_app']['nfc']['write-read'] = '[open open]'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','sensorhubservice')
G.edge['good_app']['sensorhubservice']['write-read'] = '[open open]'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['good_app']['bintvoutservice']['fill'] = 'red'
G.add_edge('good_app','bintvoutservice')
G.edge['good_app']['bintvoutservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['good_app']['bluetooth']['fill'] = 'red'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read]'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read]'
G.edge['good_app']['commonplatformappdomain']['fill'] = 'red'
G.add_edge('good_app','commonplatformappdomain')
G.edge['good_app']['commonplatformappdomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][append read]'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['good_app']['drmserver']['fill'] = 'red'
G.add_edge('good_app','drmserver')
G.edge['good_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][write read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read]'
G.edge['good_app']['good_app']['fill'] = 'red'
G.add_edge('good_app','good_app')
G.edge['good_app']['good_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','mediaserver')
G.edge['good_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read]'
G.edge['good_app']['mediaserver']['fill'] = 'red'
G.add_edge('good_app','mediaserver')
G.edge['good_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][open open][write read][append read]'
G.add_edge('good_app','nfc')
G.edge['good_app']['nfc']['write-read'] = '[open open][write read]'
G.edge['good_app']['nfc']['fill'] = 'red'
G.add_edge('good_app','nfc')
G.edge['good_app']['nfc']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['good_app']['radio']['fill'] = 'red'
G.add_edge('good_app','radio')
G.edge['good_app']['radio']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','sensorhubservice')
G.edge['good_app']['sensorhubservice']['write-read'] = '[open open][write read]'
G.edge['good_app']['sensorhubservice']['fill'] = 'red'
G.add_edge('good_app','sensorhubservice')
G.edge['good_app']['sensorhubservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['good_app']['surfaceflinger']['fill'] = 'red'
G.add_edge('good_app','surfaceflinger')
G.edge['good_app']['surfaceflinger']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['good_app']['system_server']['fill'] = 'red'
G.add_edge('good_app','system_server')
G.edge['good_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read]'
app = Viewer(G)
app.mainloop()