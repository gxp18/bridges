import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open]'
G.add_edge('apaservice','bridged_platform_app')
G.edge['apaservice']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('apaservice','createsystemfile')
G.edge['apaservice']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('apaservice','drmserver')
G.edge['apaservice']['drmserver']['write-read'] = '[open open]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('apaservice','init_shell')
G.edge['apaservice']['init_shell']['write-read'] = '[open open]'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open]'
G.add_edge('apaservice','irm_platform_app')
G.edge['apaservice']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('apaservice','knox_system_app')
G.edge['apaservice']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('apaservice','mediaserver')
G.edge['apaservice']['mediaserver']['write-read'] = '[open open]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open]'
G.add_edge('apaservice','sdcardd')
G.edge['apaservice']['sdcardd']['write-read'] = '[open open]'
G.add_edge('apaservice','system_server')
G.edge['apaservice']['system_server']['write-read'] = '[open open]'
G.add_edge('apaservice','vold')
G.edge['apaservice']['vold']['write-read'] = '[open open]'
G.add_edge('apaservice','createsystemfile')
G.edge['apaservice']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','drmserver')
G.edge['apaservice']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','irm_platform_app')
G.edge['apaservice']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','knox_system_app')
G.edge['apaservice']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','mediaserver')
G.edge['apaservice']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','sdcardd')
G.edge['apaservice']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','system_server')
G.edge['apaservice']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','vold')
G.edge['apaservice']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read]'
G.edge['apaservice']['apaservice']['fill'] = 'red'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('apaservice','bridged_platform_app')
G.edge['apaservice']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['apaservice']['bridged_platform_app']['fill'] = 'red'
G.add_edge('apaservice','bridged_platform_app')
G.edge['apaservice']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('apaservice','createsystemfile')
G.edge['apaservice']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['createsystemfile']['fill'] = 'red'
G.add_edge('apaservice','createsystemfile')
G.edge['apaservice']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','drmserver')
G.edge['apaservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['drmserver']['fill'] = 'red'
G.add_edge('apaservice','drmserver')
G.edge['apaservice']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['apaservice']['epmd']['fill'] = 'red'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['apaservice']['epmd']['fill'] = 'red'
G.add_edge('apaservice','epmd')
G.edge['apaservice']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['installd']['fill'] = 'red'
G.add_edge('apaservice','installd')
G.edge['apaservice']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','irm_platform_app')
G.edge['apaservice']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['irm_platform_app']['fill'] = 'red'
G.add_edge('apaservice','irm_platform_app')
G.edge['apaservice']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','knox_system_app')
G.edge['apaservice']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['knox_system_app']['fill'] = 'red'
G.add_edge('apaservice','knox_system_app')
G.edge['apaservice']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','mediaserver')
G.edge['apaservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['mediaserver']['fill'] = 'red'
G.add_edge('apaservice','mediaserver')
G.edge['apaservice']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['newAttr1']['fill'] = 'red'
G.add_edge('apaservice','newAttr1')
G.edge['apaservice']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','sdcardd')
G.edge['apaservice']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['sdcardd']['fill'] = 'red'
G.add_edge('apaservice','sdcardd')
G.edge['apaservice']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','system_server')
G.edge['apaservice']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['system_server']['fill'] = 'red'
G.add_edge('apaservice','system_server')
G.edge['apaservice']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('apaservice','vold')
G.edge['apaservice']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['vold']['fill'] = 'red'
G.add_edge('apaservice','vold')
G.edge['apaservice']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','apaservice')
G.edge['bridged_platform_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','drmserver')
G.edge['bridged_platform_app']['drmserver']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','irm_platform_app')
G.edge['bridged_platform_app']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','newAttr1')
G.edge['bridged_platform_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','sdcardd')
G.edge['bridged_platform_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','drmserver')
G.edge['bridged_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','irm_platform_app')
G.edge['bridged_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','newAttr1')
G.edge['bridged_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','sdcardd')
G.edge['bridged_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','apaservice')
G.edge['bridged_platform_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['apaservice']['fill'] = 'red'
G.add_edge('bridged_platform_app','apaservice')
G.edge['bridged_platform_app']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['createsystemfile']['fill'] = 'red'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','drmserver')
G.edge['bridged_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['drmserver']['fill'] = 'red'
G.add_edge('bridged_platform_app','drmserver')
G.edge['bridged_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['bridged_platform_app']['epmd']['fill'] = 'red'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['bridged_platform_app']['epmd']['fill'] = 'red'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['installd']['fill'] = 'red'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','irm_platform_app')
G.edge['bridged_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','irm_platform_app')
G.edge['bridged_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','newAttr1')
G.edge['bridged_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('bridged_platform_app','newAttr1')
G.edge['bridged_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','sdcardd')
G.edge['bridged_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['sdcardd']['fill'] = 'red'
G.add_edge('bridged_platform_app','sdcardd')
G.edge['bridged_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['system_server']['fill'] = 'red'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['vold']['fill'] = 'red'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','apaservice')
G.edge['createsystemfile']['apaservice']['write-read'] = '[open open]'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('createsystemfile','drmserver')
G.edge['createsystemfile']['drmserver']['write-read'] = '[open open]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open]'
G.add_edge('createsystemfile','irm_platform_app')
G.edge['createsystemfile']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open]'
G.add_edge('createsystemfile','newAttr1')
G.edge['createsystemfile']['newAttr1']['write-read'] = '[open open]'
G.add_edge('createsystemfile','sdcardd')
G.edge['createsystemfile']['sdcardd']['write-read'] = '[open open]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','drmserver')
G.edge['createsystemfile']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','irm_platform_app')
G.edge['createsystemfile']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','newAttr1')
G.edge['createsystemfile']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','sdcardd')
G.edge['createsystemfile']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','apaservice')
G.edge['createsystemfile']['apaservice']['write-read'] = '[open open][write read]'
G.edge['createsystemfile']['apaservice']['fill'] = 'red'
G.add_edge('createsystemfile','apaservice')
G.edge['createsystemfile']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['createsystemfile']['bridged_platform_app']['fill'] = 'red'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['createsystemfile']['fill'] = 'red'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','drmserver')
G.edge['createsystemfile']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['drmserver']['fill'] = 'red'
G.add_edge('createsystemfile','drmserver')
G.edge['createsystemfile']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['createsystemfile']['epmd']['fill'] = 'red'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['createsystemfile']['epmd']['fill'] = 'red'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['installd']['fill'] = 'red'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','irm_platform_app')
G.edge['createsystemfile']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['irm_platform_app']['fill'] = 'red'
G.add_edge('createsystemfile','irm_platform_app')
G.edge['createsystemfile']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['knox_system_app']['fill'] = 'red'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['mediaserver']['fill'] = 'red'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','newAttr1')
G.edge['createsystemfile']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['newAttr1']['fill'] = 'red'
G.add_edge('createsystemfile','newAttr1')
G.edge['createsystemfile']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','sdcardd')
G.edge['createsystemfile']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['sdcardd']['fill'] = 'red'
G.add_edge('createsystemfile','sdcardd')
G.edge['createsystemfile']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['system_server']['fill'] = 'red'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['vold']['fill'] = 'red'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open]'
G.add_edge('drmserver','bridged_platform_app')
G.edge['drmserver']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('drmserver','createsystemfile')
G.edge['drmserver']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('drmserver','init_shell')
G.edge['drmserver']['init_shell']['write-read'] = '[open open]'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open]'
G.add_edge('drmserver','irm_platform_app')
G.edge['drmserver']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('drmserver','knox_system_app')
G.edge['drmserver']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open]'
G.add_edge('drmserver','sdcardd')
G.edge['drmserver']['sdcardd']['write-read'] = '[open open]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open]'
G.add_edge('drmserver','createsystemfile')
G.edge['drmserver']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','irm_platform_app')
G.edge['drmserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','knox_system_app')
G.edge['drmserver']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','sdcardd')
G.edge['drmserver']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read]'
G.edge['drmserver']['apaservice']['fill'] = 'red'
G.add_edge('drmserver','apaservice')
G.edge['drmserver']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','bridged_platform_app')
G.edge['drmserver']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['drmserver']['bridged_platform_app']['fill'] = 'red'
G.add_edge('drmserver','bridged_platform_app')
G.edge['drmserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('drmserver','createsystemfile')
G.edge['drmserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['createsystemfile']['fill'] = 'red'
G.add_edge('drmserver','createsystemfile')
G.edge['drmserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['drmserver']['fill'] = 'red'
G.add_edge('drmserver','drmserver')
G.edge['drmserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['drmserver']['epmd']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['drmserver']['epmd']['fill'] = 'red'
G.add_edge('drmserver','epmd')
G.edge['drmserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['installd']['fill'] = 'red'
G.add_edge('drmserver','installd')
G.edge['drmserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','irm_platform_app')
G.edge['drmserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['irm_platform_app']['fill'] = 'red'
G.add_edge('drmserver','irm_platform_app')
G.edge['drmserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','knox_system_app')
G.edge['drmserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['knox_system_app']['fill'] = 'red'
G.add_edge('drmserver','knox_system_app')
G.edge['drmserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['mediaserver']['fill'] = 'red'
G.add_edge('drmserver','mediaserver')
G.edge['drmserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['newAttr1']['fill'] = 'red'
G.add_edge('drmserver','newAttr1')
G.edge['drmserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','sdcardd')
G.edge['drmserver']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['sdcardd']['fill'] = 'red'
G.add_edge('drmserver','sdcardd')
G.edge['drmserver']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['system_server']['fill'] = 'red'
G.add_edge('drmserver','system_server')
G.edge['drmserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['drmserver']['vold']['fill'] = 'red'
G.add_edge('drmserver','vold')
G.edge['drmserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open][write read]'
G.edge['epmd']['apaservice']['fill'] = 'red'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['epmd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['createsystemfile']['fill'] = 'red'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['drmserver']['fill'] = 'red'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['installd']['fill'] = 'red'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['irm_platform_app']['fill'] = 'red'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['knox_system_app']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['mediaserver']['fill'] = 'red'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['newAttr1']['fill'] = 'red'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['sdcardd']['fill'] = 'red'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['epmd']['apaservice']['fill'] = 'red'
G.add_edge('epmd','apaservice')
G.edge['epmd']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['epmd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['createsystemfile']['fill'] = 'red'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['drmserver']['fill'] = 'red'
G.add_edge('epmd','drmserver')
G.edge['epmd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['installd']['fill'] = 'red'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['irm_platform_app']['fill'] = 'red'
G.add_edge('epmd','irm_platform_app')
G.edge['epmd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['knox_system_app']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['mediaserver']['fill'] = 'red'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['newAttr1']['fill'] = 'red'
G.add_edge('epmd','newAttr1')
G.edge['epmd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['sdcardd']['fill'] = 'red'
G.add_edge('epmd','sdcardd')
G.edge['epmd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('init_shell','apaservice')
G.edge['init_shell']['apaservice']['write-read'] = '[open open]'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open]'
G.add_edge('init_shell','irm_platform_app')
G.edge['init_shell']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open]'
G.add_edge('init_shell','newAttr1')
G.edge['init_shell']['newAttr1']['write-read'] = '[open open]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','irm_platform_app')
G.edge['init_shell']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','newAttr1')
G.edge['init_shell']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('init_shell','apaservice')
G.edge['init_shell']['apaservice']['write-read'] = '[open open][write read]'
G.edge['init_shell']['apaservice']['fill'] = 'red'
G.add_edge('init_shell','apaservice')
G.edge['init_shell']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['init_shell']['bridged_platform_app']['fill'] = 'red'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['createsystemfile']['fill'] = 'red'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['drmserver']['fill'] = 'red'
G.add_edge('init_shell','drmserver')
G.edge['init_shell']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['init_shell']['epmd']['fill'] = 'red'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['init_shell']['epmd']['fill'] = 'red'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['installd']['fill'] = 'red'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','irm_platform_app')
G.edge['init_shell']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['irm_platform_app']['fill'] = 'red'
G.add_edge('init_shell','irm_platform_app')
G.edge['init_shell']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['knox_system_app']['fill'] = 'red'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','newAttr1')
G.edge['init_shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['newAttr1']['fill'] = 'red'
G.add_edge('init_shell','newAttr1')
G.edge['init_shell']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['sdcardd']['fill'] = 'red'
G.add_edge('init_shell','sdcardd')
G.edge['init_shell']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','apaservice')
G.edge['installd']['apaservice']['write-read'] = '[open open]'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('installd','drmserver')
G.edge['installd']['drmserver']['write-read'] = '[open open]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open]'
G.add_edge('installd','irm_platform_app')
G.edge['installd']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','drmserver')
G.edge['installd']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','irm_platform_app')
G.edge['installd']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('installd','apaservice')
G.edge['installd']['apaservice']['write-read'] = '[open open][write read]'
G.edge['installd']['apaservice']['fill'] = 'red'
G.add_edge('installd','apaservice')
G.edge['installd']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['installd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['createsystemfile']['fill'] = 'red'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','drmserver')
G.edge['installd']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['drmserver']['fill'] = 'red'
G.add_edge('installd','drmserver')
G.edge['installd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['installd']['epmd']['fill'] = 'red'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['installd']['epmd']['fill'] = 'red'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read]'
G.add_edge('installd','irm_platform_app')
G.edge['installd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['irm_platform_app']['fill'] = 'red'
G.add_edge('installd','irm_platform_app')
G.edge['installd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['knox_system_app']['fill'] = 'red'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['mediaserver']['fill'] = 'red'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['newAttr1']['fill'] = 'red'
G.add_edge('installd','newAttr1')
G.edge['installd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['sdcardd']['fill'] = 'red'
G.add_edge('installd','sdcardd')
G.edge['installd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['system_server']['fill'] = 'red'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['installd']['vold']['fill'] = 'red'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom]'
G.add_edge('irm_platform_app','apaservice')
G.edge['irm_platform_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','bridged_platform_app')
G.edge['irm_platform_app']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','createsystemfile')
G.edge['irm_platform_app']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','drmserver')
G.edge['irm_platform_app']['drmserver']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('irm_platform_app','init_shell')
G.edge['irm_platform_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','installd')
G.edge['irm_platform_app']['installd']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','sdcardd')
G.edge['irm_platform_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','system_server')
G.edge['irm_platform_app']['system_server']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','vold')
G.edge['irm_platform_app']['vold']['write-read'] = '[open open]'
G.add_edge('irm_platform_app','createsystemfile')
G.edge['irm_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','drmserver')
G.edge['irm_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('irm_platform_app','installd')
G.edge['irm_platform_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','sdcardd')
G.edge['irm_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','system_server')
G.edge['irm_platform_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','vold')
G.edge['irm_platform_app']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('irm_platform_app','apaservice')
G.edge['irm_platform_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['irm_platform_app']['apaservice']['fill'] = 'red'
G.add_edge('irm_platform_app','apaservice')
G.edge['irm_platform_app']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_platform_app','bridged_platform_app')
G.edge['irm_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['irm_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('irm_platform_app','bridged_platform_app')
G.edge['irm_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('irm_platform_app','createsystemfile')
G.edge['irm_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['createsystemfile']['fill'] = 'red'
G.add_edge('irm_platform_app','createsystemfile')
G.edge['irm_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','drmserver')
G.edge['irm_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['drmserver']['fill'] = 'red'
G.add_edge('irm_platform_app','drmserver')
G.edge['irm_platform_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['irm_platform_app']['epmd']['fill'] = 'red'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['irm_platform_app']['epmd']['fill'] = 'red'
G.add_edge('irm_platform_app','epmd')
G.edge['irm_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('irm_platform_app','installd')
G.edge['irm_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['installd']['fill'] = 'red'
G.add_edge('irm_platform_app','installd')
G.edge['irm_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('irm_platform_app','irm_platform_app')
G.edge['irm_platform_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('irm_platform_app','knox_system_app')
G.edge['irm_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('irm_platform_app','mediaserver')
G.edge['irm_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['newAttr1']['fill'] = 'red'
G.add_edge('irm_platform_app','newAttr1')
G.edge['irm_platform_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','sdcardd')
G.edge['irm_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['sdcardd']['fill'] = 'red'
G.add_edge('irm_platform_app','sdcardd')
G.edge['irm_platform_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','system_server')
G.edge['irm_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['system_server']['fill'] = 'red'
G.add_edge('irm_platform_app','system_server')
G.edge['irm_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('irm_platform_app','vold')
G.edge['irm_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['irm_platform_app']['vold']['fill'] = 'red'
G.add_edge('irm_platform_app','vold')
G.edge['irm_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','apaservice')
G.edge['knox_system_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','irm_platform_app')
G.edge['knox_system_app']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open]'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open]'
G.add_edge('knox_system_app','sdcardd')
G.edge['knox_system_app']['sdcardd']['write-read'] = '[open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','irm_platform_app')
G.edge['knox_system_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','sdcardd')
G.edge['knox_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','apaservice')
G.edge['knox_system_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['apaservice']['fill'] = 'red'
G.add_edge('knox_system_app','apaservice')
G.edge['knox_system_app']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['knox_system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['createsystemfile']['fill'] = 'red'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['drmserver']['fill'] = 'red'
G.add_edge('knox_system_app','drmserver')
G.edge['knox_system_app']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['knox_system_app']['epmd']['fill'] = 'red'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['knox_system_app']['epmd']['fill'] = 'red'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['installd']['fill'] = 'red'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','irm_platform_app')
G.edge['knox_system_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['irm_platform_app']['fill'] = 'red'
G.add_edge('knox_system_app','irm_platform_app')
G.edge['knox_system_app']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['newAttr1']['fill'] = 'red'
G.add_edge('knox_system_app','newAttr1')
G.edge['knox_system_app']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','sdcardd')
G.edge['knox_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['sdcardd']['fill'] = 'red'
G.add_edge('knox_system_app','sdcardd')
G.edge['knox_system_app']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['vold']['fill'] = 'red'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','apaservice')
G.edge['mediaserver']['apaservice']['write-read'] = '[open open]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open]'
G.add_edge('mediaserver','irm_platform_app')
G.edge['mediaserver']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open]'
G.add_edge('mediaserver','sdcardd')
G.edge['mediaserver']['sdcardd']['write-read'] = '[open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','irm_platform_app')
G.edge['mediaserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','sdcardd')
G.edge['mediaserver']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mediaserver','apaservice')
G.edge['mediaserver']['apaservice']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['apaservice']['fill'] = 'red'
G.add_edge('mediaserver','apaservice')
G.edge['mediaserver']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['mediaserver']['bridged_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['createsystemfile']['fill'] = 'red'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['drmserver']['fill'] = 'red'
G.add_edge('mediaserver','drmserver')
G.edge['mediaserver']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['installd']['fill'] = 'red'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','irm_platform_app')
G.edge['mediaserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['irm_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','irm_platform_app')
G.edge['mediaserver']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['newAttr1']['fill'] = 'red'
G.add_edge('mediaserver','newAttr1')
G.edge['mediaserver']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','sdcardd')
G.edge['mediaserver']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['sdcardd']['fill'] = 'red'
G.add_edge('mediaserver','sdcardd')
G.edge['mediaserver']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open]'
G.add_edge('newAttr1','bridged_platform_app')
G.edge['newAttr1']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('newAttr1','createsystemfile')
G.edge['newAttr1']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('newAttr1','drmserver')
G.edge['newAttr1']['drmserver']['write-read'] = '[open open]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('newAttr1','init_shell')
G.edge['newAttr1']['init_shell']['write-read'] = '[open open]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open]'
G.add_edge('newAttr1','irm_platform_app')
G.edge['newAttr1']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open]'
G.add_edge('newAttr1','sdcardd')
G.edge['newAttr1']['sdcardd']['write-read'] = '[open open]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open]'
G.add_edge('newAttr1','createsystemfile')
G.edge['newAttr1']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','drmserver')
G.edge['newAttr1']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','irm_platform_app')
G.edge['newAttr1']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','sdcardd')
G.edge['newAttr1']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open][write read]'
G.edge['newAttr1']['apaservice']['fill'] = 'red'
G.add_edge('newAttr1','apaservice')
G.edge['newAttr1']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr1','bridged_platform_app')
G.edge['newAttr1']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['newAttr1']['bridged_platform_app']['fill'] = 'red'
G.add_edge('newAttr1','bridged_platform_app')
G.edge['newAttr1']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('newAttr1','createsystemfile')
G.edge['newAttr1']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['createsystemfile']['fill'] = 'red'
G.add_edge('newAttr1','createsystemfile')
G.edge['newAttr1']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','drmserver')
G.edge['newAttr1']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['drmserver']['fill'] = 'red'
G.add_edge('newAttr1','drmserver')
G.edge['newAttr1']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['newAttr1']['epmd']['fill'] = 'red'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['newAttr1']['epmd']['fill'] = 'red'
G.add_edge('newAttr1','epmd')
G.edge['newAttr1']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['installd']['fill'] = 'red'
G.add_edge('newAttr1','installd')
G.edge['newAttr1']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','irm_platform_app')
G.edge['newAttr1']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['irm_platform_app']['fill'] = 'red'
G.add_edge('newAttr1','irm_platform_app')
G.edge['newAttr1']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['knox_system_app']['fill'] = 'red'
G.add_edge('newAttr1','knox_system_app')
G.edge['newAttr1']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['mediaserver']['fill'] = 'red'
G.add_edge('newAttr1','mediaserver')
G.edge['newAttr1']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['newAttr1']['fill'] = 'red'
G.add_edge('newAttr1','newAttr1')
G.edge['newAttr1']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','sdcardd')
G.edge['newAttr1']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['sdcardd']['fill'] = 'red'
G.add_edge('newAttr1','sdcardd')
G.edge['newAttr1']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['system_server']['fill'] = 'red'
G.add_edge('newAttr1','system_server')
G.edge['newAttr1']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['newAttr1']['vold']['fill'] = 'red'
G.add_edge('newAttr1','vold')
G.edge['newAttr1']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','apaservice')
G.edge['sdcardd']['apaservice']['write-read'] = '[open open]'
G.add_edge('sdcardd','bridged_platform_app')
G.edge['sdcardd']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','createsystemfile')
G.edge['sdcardd']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('sdcardd','drmserver')
G.edge['sdcardd']['drmserver']['write-read'] = '[open open]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('sdcardd','init_shell')
G.edge['sdcardd']['init_shell']['write-read'] = '[open open]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open]'
G.add_edge('sdcardd','irm_platform_app')
G.edge['sdcardd']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','knox_system_app')
G.edge['sdcardd']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('sdcardd','mediaserver')
G.edge['sdcardd']['mediaserver']['write-read'] = '[open open]'
G.add_edge('sdcardd','newAttr1')
G.edge['sdcardd']['newAttr1']['write-read'] = '[open open]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open]'
G.add_edge('sdcardd','createsystemfile')
G.edge['sdcardd']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','drmserver')
G.edge['sdcardd']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','irm_platform_app')
G.edge['sdcardd']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','knox_system_app')
G.edge['sdcardd']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','mediaserver')
G.edge['sdcardd']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','newAttr1')
G.edge['sdcardd']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('sdcardd','apaservice')
G.edge['sdcardd']['apaservice']['write-read'] = '[open open][write read]'
G.edge['sdcardd']['apaservice']['fill'] = 'red'
G.add_edge('sdcardd','apaservice')
G.edge['sdcardd']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('sdcardd','bridged_platform_app')
G.edge['sdcardd']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['sdcardd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('sdcardd','bridged_platform_app')
G.edge['sdcardd']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('sdcardd','createsystemfile')
G.edge['sdcardd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['createsystemfile']['fill'] = 'red'
G.add_edge('sdcardd','createsystemfile')
G.edge['sdcardd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','drmserver')
G.edge['sdcardd']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['drmserver']['fill'] = 'red'
G.add_edge('sdcardd','drmserver')
G.edge['sdcardd']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['sdcardd']['epmd']['fill'] = 'red'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['sdcardd']['epmd']['fill'] = 'red'
G.add_edge('sdcardd','epmd')
G.edge['sdcardd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['installd']['fill'] = 'red'
G.add_edge('sdcardd','installd')
G.edge['sdcardd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','irm_platform_app')
G.edge['sdcardd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['irm_platform_app']['fill'] = 'red'
G.add_edge('sdcardd','irm_platform_app')
G.edge['sdcardd']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','knox_system_app')
G.edge['sdcardd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['knox_system_app']['fill'] = 'red'
G.add_edge('sdcardd','knox_system_app')
G.edge['sdcardd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','mediaserver')
G.edge['sdcardd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['mediaserver']['fill'] = 'red'
G.add_edge('sdcardd','mediaserver')
G.edge['sdcardd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','newAttr1')
G.edge['sdcardd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['newAttr1']['fill'] = 'red'
G.add_edge('sdcardd','newAttr1')
G.edge['sdcardd']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['sdcardd']['fill'] = 'red'
G.add_edge('sdcardd','sdcardd')
G.edge['sdcardd']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['system_server']['fill'] = 'red'
G.add_edge('sdcardd','system_server')
G.edge['sdcardd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['sdcardd']['vold']['fill'] = 'red'
G.add_edge('sdcardd','vold')
G.edge['sdcardd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','apaservice')
G.edge['system_server']['apaservice']['write-read'] = '[open open]'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open]'
G.add_edge('system_server','irm_platform_app')
G.edge['system_server']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','irm_platform_app')
G.edge['system_server']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('system_server','apaservice')
G.edge['system_server']['apaservice']['write-read'] = '[open open][write read]'
G.edge['system_server']['apaservice']['fill'] = 'red'
G.add_edge('system_server','apaservice')
G.edge['system_server']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['system_server']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['createsystemfile']['fill'] = 'red'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['drmserver']['fill'] = 'red'
G.add_edge('system_server','drmserver')
G.edge['system_server']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','irm_platform_app')
G.edge['system_server']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['irm_platform_app']['fill'] = 'red'
G.add_edge('system_server','irm_platform_app')
G.edge['system_server']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['newAttr1']['fill'] = 'red'
G.add_edge('system_server','newAttr1')
G.edge['system_server']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['system_server']['sdcardd']['fill'] = 'red'
G.add_edge('system_server','sdcardd')
G.edge['system_server']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('vold','apaservice')
G.edge['vold']['apaservice']['write-read'] = '[open open]'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open]'
G.add_edge('vold','irm_platform_app')
G.edge['vold']['irm_platform_app']['write-read'] = '[open open]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','irm_platform_app')
G.edge['vold']['irm_platform_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('vold','apaservice')
G.edge['vold']['apaservice']['write-read'] = '[open open][write read]'
G.edge['vold']['apaservice']['fill'] = 'red'
G.add_edge('vold','apaservice')
G.edge['vold']['apaservice']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['vold']['bridged_platform_app']['fill'] = 'red'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read][append read]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['createsystemfile']['fill'] = 'red'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['drmserver']['fill'] = 'red'
G.add_edge('vold','drmserver')
G.edge['vold']['drmserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['installd']['fill'] = 'red'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','irm_platform_app')
G.edge['vold']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['irm_platform_app']['fill'] = 'red'
G.add_edge('vold','irm_platform_app')
G.edge['vold']['irm_platform_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['knox_system_app']['fill'] = 'red'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['newAttr1']['fill'] = 'red'
G.add_edge('vold','newAttr1')
G.edge['vold']['newAttr1']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['sdcardd']['fill'] = 'red'
G.add_edge('vold','sdcardd')
G.edge['vold']['sdcardd']['write-read'] = '[open open][setattr getattr][write read][append read]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read]'
app = Viewer(G)
app.mainloop()