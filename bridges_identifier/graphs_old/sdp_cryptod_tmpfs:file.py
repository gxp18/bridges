import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('sdp_cryptod','sdp_cryptod')
G.edge['sdp_cryptod']['sdp_cryptod']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read]'
G.edge['sdp_cryptod']['sdp_cryptod']['fill'] = 'red'
app = Viewer(G)
app.mainloop()