import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('vm_bms','vm_bms')
G.edge['vm_bms']['vm_bms']['write-read'] = '[write read]'
G.edge['vm_bms']['vm_bms']['fill'] = 'red'
app = Viewer(G)
app.mainloop()