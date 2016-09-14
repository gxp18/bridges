import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('bridged_platform_app','zygote')
G.edge['bridged_platform_app']['zygote']['write-read'] = '[open open]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('bridged_platform_app','zygote')
G.edge['bridged_platform_app']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['bridged_platform_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['createsystemfile']['fill'] = 'red'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['epmd']['fill'] = 'red'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['init_shell']['fill'] = 'red'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['installd']['fill'] = 'red'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['knox_system_app']['fill'] = 'red'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['mediaserver']['fill'] = 'red'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['system_server']['fill'] = 'red'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['vold']['fill'] = 'red'
G.add_edge('bridged_platform_app','zygote')
G.edge['bridged_platform_app']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bridged_platform_app']['zygote']['fill'] = 'red'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('bridged_platform_app','bridged_platform_app')
G.edge['bridged_platform_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','createsystemfile')
G.edge['bridged_platform_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','epmd')
G.edge['bridged_platform_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','init_shell')
G.edge['bridged_platform_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','installd')
G.edge['bridged_platform_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','knox_system_app')
G.edge['bridged_platform_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','mediaserver')
G.edge['bridged_platform_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','system_server')
G.edge['bridged_platform_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','vold')
G.edge['bridged_platform_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bridged_platform_app','zygote')
G.edge['bridged_platform_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bridged_platform_app','zygote')
G.edge['bridged_platform_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('createsystemfile','zygote')
G.edge['createsystemfile']['zygote']['write-read'] = '[open open]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('createsystemfile','zygote')
G.edge['createsystemfile']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['createsystemfile']['bridged_platform_app']['fill'] = 'red'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['createsystemfile']['fill'] = 'red'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['epmd']['fill'] = 'red'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['createsystemfile']['init_shell']['fill'] = 'red'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['installd']['fill'] = 'red'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['knox_system_app']['fill'] = 'red'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['mediaserver']['fill'] = 'red'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['system_server']['fill'] = 'red'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['createsystemfile']['vold']['fill'] = 'red'
G.add_edge('createsystemfile','zygote')
G.edge['createsystemfile']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['createsystemfile']['zygote']['fill'] = 'red'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('createsystemfile','bridged_platform_app')
G.edge['createsystemfile']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','createsystemfile')
G.edge['createsystemfile']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','epmd')
G.edge['createsystemfile']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','init_shell')
G.edge['createsystemfile']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','installd')
G.edge['createsystemfile']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','knox_system_app')
G.edge['createsystemfile']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','mediaserver')
G.edge['createsystemfile']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','system_server')
G.edge['createsystemfile']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','vold')
G.edge['createsystemfile']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('createsystemfile','zygote')
G.edge['createsystemfile']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('createsystemfile','zygote')
G.edge['createsystemfile']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('epmd','zygote')
G.edge['epmd']['zygote']['write-read'] = '[open open]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('epmd','zygote')
G.edge['epmd']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['epmd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['createsystemfile']['fill'] = 'red'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['epmd']['epmd']['fill'] = 'red'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['init_shell']['fill'] = 'red'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['epmd']['installd']['fill'] = 'red'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['knox_system_app']['fill'] = 'red'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['epmd']['mediaserver']['fill'] = 'red'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['epmd']['system_server']['fill'] = 'red'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['epmd']['vold']['fill'] = 'red'
G.add_edge('epmd','zygote')
G.edge['epmd']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['epmd']['zygote']['fill'] = 'red'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('epmd','bridged_platform_app')
G.edge['epmd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','createsystemfile')
G.edge['epmd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','epmd')
G.edge['epmd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','init_shell')
G.edge['epmd']['init_shell']['write-read'] = '[open open][open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','installd')
G.edge['epmd']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','knox_system_app')
G.edge['epmd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','mediaserver')
G.edge['epmd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','system_server')
G.edge['epmd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','vold')
G.edge['epmd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('epmd','zygote')
G.edge['epmd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('epmd','zygote')
G.edge['epmd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['init_shell']['bridged_platform_app']['fill'] = 'red'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['createsystemfile']['fill'] = 'red'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['epmd']['fill'] = 'red'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['init_shell']['fill'] = 'red'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['installd']['fill'] = 'red'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['knox_system_app']['fill'] = 'red'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['mediaserver']['fill'] = 'red'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['system_server']['fill'] = 'red'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['init_shell']['vold']['fill'] = 'red'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['init_shell']['zygote']['fill'] = 'red'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('init_shell','bridged_platform_app')
G.edge['init_shell']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','createsystemfile')
G.edge['init_shell']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','epmd')
G.edge['init_shell']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','init_shell')
G.edge['init_shell']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','installd')
G.edge['init_shell']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','knox_system_app')
G.edge['init_shell']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','mediaserver')
G.edge['init_shell']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','system_server')
G.edge['init_shell']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','vold')
G.edge['init_shell']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('init_shell','zygote')
G.edge['init_shell']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['installd']['bridged_platform_app']['fill'] = 'red'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['createsystemfile']['fill'] = 'red'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['epmd']['fill'] = 'red'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['init_shell']['fill'] = 'red'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['installd']['installd']['fill'] = 'red'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['knox_system_app']['fill'] = 'red'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['mediaserver']['fill'] = 'red'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['system_server']['fill'] = 'red'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['installd']['vold']['fill'] = 'red'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['installd']['zygote']['fill'] = 'red'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('installd','bridged_platform_app')
G.edge['installd']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','createsystemfile')
G.edge['installd']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','epmd')
G.edge['installd']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','init_shell')
G.edge['installd']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','installd')
G.edge['installd']['installd']['write-read'] = '[setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][append read][relabelto relabelfrom][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','knox_system_app')
G.edge['installd']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','mediaserver')
G.edge['installd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','system_server')
G.edge['installd']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','vold')
G.edge['installd']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('installd','zygote')
G.edge['installd']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['knox_system_app']['bridged_platform_app']['fill'] = 'red'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['createsystemfile']['fill'] = 'red'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['epmd']['fill'] = 'red'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read]'
G.edge['knox_system_app']['init_shell']['fill'] = 'red'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['installd']['fill'] = 'red'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['knox_system_app']['fill'] = 'red'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['mediaserver']['fill'] = 'red'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['system_server']['fill'] = 'red'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['knox_system_app']['vold']['fill'] = 'red'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['knox_system_app']['zygote']['fill'] = 'red'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('knox_system_app','bridged_platform_app')
G.edge['knox_system_app']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','createsystemfile')
G.edge['knox_system_app']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','epmd')
G.edge['knox_system_app']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','init_shell')
G.edge['knox_system_app']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','installd')
G.edge['knox_system_app']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','knox_system_app')
G.edge['knox_system_app']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','mediaserver')
G.edge['knox_system_app']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','system_server')
G.edge['knox_system_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','vold')
G.edge['knox_system_app']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('knox_system_app','zygote')
G.edge['knox_system_app']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read]'
G.edge['mediaserver']['bridged_platform_app']['fill'] = 'red'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['createsystemfile']['fill'] = 'red'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['epmd']['fill'] = 'red'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['init_shell']['fill'] = 'red'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['installd']['fill'] = 'red'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['knox_system_app']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['vold']['fill'] = 'red'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mediaserver']['zygote']['fill'] = 'red'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search]'
G.add_edge('mediaserver','bridged_platform_app')
G.edge['mediaserver']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','createsystemfile')
G.edge['mediaserver']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','epmd')
G.edge['mediaserver']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','init_shell')
G.edge['mediaserver']['init_shell']['write-read'] = '[open open][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','installd')
G.edge['mediaserver']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','knox_system_app')
G.edge['mediaserver']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','vold')
G.edge['mediaserver']['vold']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mediaserver','zygote')
G.edge['mediaserver']['zygote']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('radio','bridged_platform_app')
G.edge['radio']['bridged_platform_app']['write-read'] = '[add_name search]'
G.add_edge('radio','bridged_platform_app')
G.edge['radio']['bridged_platform_app']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','createsystemfile')
G.edge['radio']['createsystemfile']['write-read'] = '[add_name search]'
G.add_edge('radio','createsystemfile')
G.edge['radio']['createsystemfile']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','epmd')
G.edge['radio']['epmd']['write-read'] = '[add_name search]'
G.add_edge('radio','epmd')
G.edge['radio']['epmd']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search]'
G.add_edge('radio','init_shell')
G.edge['radio']['init_shell']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search]'
G.add_edge('radio','installd')
G.edge['radio']['installd']['write-read'] = '[setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][add_name search][remove_name search]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search]'
G.add_edge('radio','knox_system_app')
G.edge['radio']['knox_system_app']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','vold')
G.edge['radio']['vold']['write-read'] = '[add_name search]'
G.add_edge('radio','vold')
G.edge['radio']['vold']['write-read'] = '[add_name search][remove_name search]'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read][append read][add_name search]'
G.add_edge('radio','zygote')
G.edge['radio']['zygote']['write-read'] = '[open open][write read][append read][add_name search][remove_name search]'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['system_server']['bridged_platform_app']['fill'] = 'red'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['createsystemfile']['fill'] = 'red'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['epmd']['fill'] = 'red'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['init_shell']['fill'] = 'red'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['installd']['fill'] = 'red'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['knox_system_app']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['vold']['fill'] = 'red'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['system_server']['zygote']['fill'] = 'red'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('system_server','bridged_platform_app')
G.edge['system_server']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','createsystemfile')
G.edge['system_server']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','epmd')
G.edge['system_server']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','init_shell')
G.edge['system_server']['init_shell']['write-read'] = '[open open][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','knox_system_app')
G.edge['system_server']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','vold')
G.edge['system_server']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('system_server','zygote')
G.edge['system_server']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('system_server','installd')
G.edge['system_server']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom]'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['vold']['bridged_platform_app']['fill'] = 'red'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['createsystemfile']['fill'] = 'red'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['epmd']['fill'] = 'red'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['vold']['init_shell']['fill'] = 'red'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['installd']['fill'] = 'red'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['knox_system_app']['fill'] = 'red'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['mediaserver']['fill'] = 'red'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['system_server']['fill'] = 'red'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['vold']['vold']['fill'] = 'red'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vold']['zygote']['fill'] = 'red'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('vold','bridged_platform_app')
G.edge['vold']['bridged_platform_app']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','createsystemfile')
G.edge['vold']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','epmd')
G.edge['vold']['epmd']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','init_shell')
G.edge['vold']['init_shell']['write-read'] = '[open open][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','installd')
G.edge['vold']['installd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','knox_system_app')
G.edge['vold']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','mediaserver')
G.edge['vold']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','system_server')
G.edge['vold']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','vold')
G.edge['vold']['vold']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vold','zygote')
G.edge['vold']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','bridged_platform_app')
G.edge['zygote']['bridged_platform_app']['write-read'] = '[open open]'
G.add_edge('zygote','createsystemfile')
G.edge['zygote']['createsystemfile']['write-read'] = '[open open]'
G.add_edge('zygote','epmd')
G.edge['zygote']['epmd']['write-read'] = '[open open]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('zygote','knox_system_app')
G.edge['zygote']['knox_system_app']['write-read'] = '[open open]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open]'
G.add_edge('zygote','vold')
G.edge['zygote']['vold']['write-read'] = '[open open]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('zygote','createsystemfile')
G.edge['zygote']['createsystemfile']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','epmd')
G.edge['zygote']['epmd']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('zygote','knox_system_app')
G.edge['zygote']['knox_system_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr]'
G.add_edge('zygote','vold')
G.edge['zygote']['vold']['write-read'] = '[open open][setattr getattr]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('zygote','bridged_platform_app')
G.edge['zygote']['bridged_platform_app']['write-read'] = '[open open][write read]'
G.edge['zygote']['bridged_platform_app']['fill'] = 'red'
G.add_edge('zygote','createsystemfile')
G.edge['zygote']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['createsystemfile']['fill'] = 'red'
G.add_edge('zygote','epmd')
G.edge['zygote']['epmd']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['epmd']['fill'] = 'red'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['init_shell']['fill'] = 'red'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['zygote']['installd']['fill'] = 'red'
G.add_edge('zygote','knox_system_app')
G.edge['zygote']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['knox_system_app']['fill'] = 'red'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['mediaserver']['fill'] = 'red'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['zygote']['system_server']['fill'] = 'red'
G.add_edge('zygote','vold')
G.edge['zygote']['vold']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['zygote']['vold']['fill'] = 'red'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['zygote']['zygote']['fill'] = 'red'
G.add_edge('zygote','bridged_platform_app')
G.edge['zygote']['bridged_platform_app']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('zygote','bridged_platform_app')
G.edge['zygote']['bridged_platform_app']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('zygote','createsystemfile')
G.edge['zygote']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','createsystemfile')
G.edge['zygote']['createsystemfile']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','epmd')
G.edge['zygote']['epmd']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','epmd')
G.edge['zygote']['epmd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','init_shell')
G.edge['zygote']['init_shell']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','installd')
G.edge['zygote']['installd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','knox_system_app')
G.edge['zygote']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','knox_system_app')
G.edge['zygote']['knox_system_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','mediaserver')
G.edge['zygote']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','system_server')
G.edge['zygote']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','vold')
G.edge['zygote']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','vold')
G.edge['zygote']['vold']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('zygote','zygote')
G.edge['zygote']['zygote']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()