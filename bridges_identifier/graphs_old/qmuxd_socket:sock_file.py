import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('atfwd','atfwd')
G.edge['atfwd']['atfwd']['write-read'] = '[write read][setattr getattr]'
G.add_edge('atfwd','bluetooth')
G.edge['atfwd']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','cnd')
G.edge['atfwd']['cnd']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','DMM-daemon')
G.edge['atfwd']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','dpmd')
G.edge['atfwd']['dpmd']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','ims')
G.edge['atfwd']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','location_app')
G.edge['atfwd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','location')
G.edge['atfwd']['location']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','mediaserver')
G.edge['atfwd']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','netmgrd')
G.edge['atfwd']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','qmuxd')
G.edge['atfwd']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','qti')
G.edge['atfwd']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','radio')
G.edge['atfwd']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','rild')
G.edge['atfwd']['rild']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','system_server')
G.edge['atfwd']['system_server']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','thermal-engine')
G.edge['atfwd']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','wcnss_service')
G.edge['atfwd']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','wpa')
G.edge['atfwd']['wpa']['write-read'] = '[setattr getattr]'
G.add_edge('atfwd','atfwd')
G.edge['atfwd']['atfwd']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['atfwd']['atfwd']['fill'] = 'red'
G.add_edge('atfwd','atfwd')
G.edge['atfwd']['atfwd']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['atfwd']['atfwd']['fill'] = 'red'
G.add_edge('atfwd','bluetooth')
G.edge['atfwd']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['bluetooth']['fill'] = 'red'
G.add_edge('atfwd','bluetooth')
G.edge['atfwd']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['bluetooth']['fill'] = 'red'
G.add_edge('atfwd','cnd')
G.edge['atfwd']['cnd']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['cnd']['fill'] = 'red'
G.add_edge('atfwd','cnd')
G.edge['atfwd']['cnd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['cnd']['fill'] = 'red'
G.add_edge('atfwd','DMM-daemon')
G.edge['atfwd']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['DMM-daemon']['fill'] = 'red'
G.add_edge('atfwd','DMM-daemon')
G.edge['atfwd']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['DMM-daemon']['fill'] = 'red'
G.add_edge('atfwd','dpmd')
G.edge['atfwd']['dpmd']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['dpmd']['fill'] = 'red'
G.add_edge('atfwd','dpmd')
G.edge['atfwd']['dpmd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['dpmd']['fill'] = 'red'
G.add_edge('atfwd','ims')
G.edge['atfwd']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['ims']['fill'] = 'red'
G.add_edge('atfwd','ims')
G.edge['atfwd']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['ims']['fill'] = 'red'
G.add_edge('atfwd','location_app')
G.edge['atfwd']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['location_app']['fill'] = 'red'
G.add_edge('atfwd','location_app')
G.edge['atfwd']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['location_app']['fill'] = 'red'
G.add_edge('atfwd','location')
G.edge['atfwd']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['location']['fill'] = 'red'
G.add_edge('atfwd','location')
G.edge['atfwd']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['location']['fill'] = 'red'
G.add_edge('atfwd','mediaserver')
G.edge['atfwd']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['mediaserver']['fill'] = 'red'
G.add_edge('atfwd','mediaserver')
G.edge['atfwd']['mediaserver']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['mediaserver']['fill'] = 'red'
G.add_edge('atfwd','netmgrd')
G.edge['atfwd']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['netmgrd']['fill'] = 'red'
G.add_edge('atfwd','netmgrd')
G.edge['atfwd']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['netmgrd']['fill'] = 'red'
G.add_edge('atfwd','qmuxd')
G.edge['atfwd']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['qmuxd']['fill'] = 'red'
G.add_edge('atfwd','qmuxd')
G.edge['atfwd']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['qmuxd']['fill'] = 'red'
G.add_edge('atfwd','qti')
G.edge['atfwd']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['qti']['fill'] = 'red'
G.add_edge('atfwd','qti')
G.edge['atfwd']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['qti']['fill'] = 'red'
G.add_edge('atfwd','radio')
G.edge['atfwd']['radio']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['radio']['fill'] = 'red'
G.add_edge('atfwd','radio')
G.edge['atfwd']['radio']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['radio']['fill'] = 'red'
G.add_edge('atfwd','rild')
G.edge['atfwd']['rild']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['rild']['fill'] = 'red'
G.add_edge('atfwd','rild')
G.edge['atfwd']['rild']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['rild']['fill'] = 'red'
G.add_edge('atfwd','system_server')
G.edge['atfwd']['system_server']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['system_server']['fill'] = 'red'
G.add_edge('atfwd','system_server')
G.edge['atfwd']['system_server']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['system_server']['fill'] = 'red'
G.add_edge('atfwd','thermal-engine')
G.edge['atfwd']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['thermal-engine']['fill'] = 'red'
G.add_edge('atfwd','thermal-engine')
G.edge['atfwd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['thermal-engine']['fill'] = 'red'
G.add_edge('atfwd','wcnss_service')
G.edge['atfwd']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['wcnss_service']['fill'] = 'red'
G.add_edge('atfwd','wcnss_service')
G.edge['atfwd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['wcnss_service']['fill'] = 'red'
G.add_edge('atfwd','wpa')
G.edge['atfwd']['wpa']['write-read'] = '[setattr getattr][write read]'
G.edge['atfwd']['wpa']['fill'] = 'red'
G.add_edge('atfwd','wpa')
G.edge['atfwd']['wpa']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['atfwd']['wpa']['fill'] = 'red'
G.add_edge('bluetooth','atfwd')
G.edge['bluetooth']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('bluetooth','DMM-daemon')
G.edge['bluetooth']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','ims')
G.edge['bluetooth']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','location_app')
G.edge['bluetooth']['location_app']['write-read'] = '[open open][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','location')
G.edge['bluetooth']['location']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','netmgrd')
G.edge['bluetooth']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','wcnss_service')
G.edge['bluetooth']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('bluetooth','wpa')
G.edge['bluetooth']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('bluetooth','atfwd')
G.edge['bluetooth']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['atfwd']['fill'] = 'red'
G.add_edge('bluetooth','atfwd')
G.edge['bluetooth']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['bluetooth']['atfwd']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][write read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['cnd']['fill'] = 'red'
G.add_edge('bluetooth','cnd')
G.edge['bluetooth']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['cnd']['fill'] = 'red'
G.add_edge('bluetooth','DMM-daemon')
G.edge['bluetooth']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['DMM-daemon']['fill'] = 'red'
G.add_edge('bluetooth','DMM-daemon')
G.edge['bluetooth']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['bluetooth']['DMM-daemon']['fill'] = 'red'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['dpmd']['fill'] = 'red'
G.add_edge('bluetooth','dpmd')
G.edge['bluetooth']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['dpmd']['fill'] = 'red'
G.add_edge('bluetooth','ims')
G.edge['bluetooth']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['ims']['fill'] = 'red'
G.add_edge('bluetooth','ims')
G.edge['bluetooth']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['bluetooth']['ims']['fill'] = 'red'
G.add_edge('bluetooth','location_app')
G.edge['bluetooth']['location_app']['write-read'] = '[open open][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['location_app']['fill'] = 'red'
G.add_edge('bluetooth','location_app')
G.edge['bluetooth']['location_app']['write-read'] = '[open open][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['location_app']['fill'] = 'red'
G.add_edge('bluetooth','location')
G.edge['bluetooth']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['location']['fill'] = 'red'
G.add_edge('bluetooth','location')
G.edge['bluetooth']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['bluetooth']['location']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','mediaserver')
G.edge['bluetooth']['mediaserver']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['mediaserver']['fill'] = 'red'
G.add_edge('bluetooth','netmgrd')
G.edge['bluetooth']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['netmgrd']['fill'] = 'red'
G.add_edge('bluetooth','netmgrd')
G.edge['bluetooth']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['netmgrd']['fill'] = 'red'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['qmuxd']['fill'] = 'red'
G.add_edge('bluetooth','qmuxd')
G.edge['bluetooth']['qmuxd']['write-read'] = '[open open][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['qmuxd']['fill'] = 'red'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['qti']['fill'] = 'red'
G.add_edge('bluetooth','qti')
G.edge['bluetooth']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['qti']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['radio']['fill'] = 'red'
G.add_edge('bluetooth','radio')
G.edge['bluetooth']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['radio']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','system_server')
G.edge['bluetooth']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['bluetooth']['system_server']['fill'] = 'red'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['thermal-engine']['fill'] = 'red'
G.add_edge('bluetooth','thermal-engine')
G.edge['bluetooth']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['thermal-engine']['fill'] = 'red'
G.add_edge('bluetooth','wcnss_service')
G.edge['bluetooth']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['bluetooth']['wcnss_service']['fill'] = 'red'
G.add_edge('bluetooth','wcnss_service')
G.edge['bluetooth']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['bluetooth']['wcnss_service']['fill'] = 'red'
G.add_edge('bluetooth','wpa')
G.edge['bluetooth']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['bluetooth']['wpa']['fill'] = 'red'
G.add_edge('bluetooth','wpa')
G.edge['bluetooth']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['bluetooth']['wpa']['fill'] = 'red'
G.add_edge('cnd','atfwd')
G.edge['cnd']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('cnd','bluetooth')
G.edge['cnd']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr]'
G.add_edge('cnd','DMM-daemon')
G.edge['cnd']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','ims')
G.edge['cnd']['ims']['write-read'] = '[add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','location_app')
G.edge['cnd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('cnd','location')
G.edge['cnd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','mediaserver')
G.edge['cnd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][setattr getattr]'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr]'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('cnd','atfwd')
G.edge['cnd']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['cnd']['atfwd']['fill'] = 'red'
G.add_edge('cnd','atfwd')
G.edge['cnd']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['cnd']['atfwd']['fill'] = 'red'
G.add_edge('cnd','bluetooth')
G.edge['cnd']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['cnd']['bluetooth']['fill'] = 'red'
G.add_edge('cnd','bluetooth')
G.edge['cnd']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['cnd']['bluetooth']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','cnd')
G.edge['cnd']['cnd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][write read][append read][setopt getopt][setattr getattr][write read][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['cnd']['fill'] = 'red'
G.add_edge('cnd','DMM-daemon')
G.edge['cnd']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['cnd']['DMM-daemon']['fill'] = 'red'
G.add_edge('cnd','DMM-daemon')
G.edge['cnd']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['cnd']['DMM-daemon']['fill'] = 'red'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['dpmd']['fill'] = 'red'
G.add_edge('cnd','dpmd')
G.edge['cnd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['dpmd']['fill'] = 'red'
G.add_edge('cnd','ims')
G.edge['cnd']['ims']['write-read'] = '[add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['ims']['fill'] = 'red'
G.add_edge('cnd','ims')
G.edge['cnd']['ims']['write-read'] = '[add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['ims']['fill'] = 'red'
G.add_edge('cnd','location_app')
G.edge['cnd']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['cnd']['location_app']['fill'] = 'red'
G.add_edge('cnd','location_app')
G.edge['cnd']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['cnd']['location_app']['fill'] = 'red'
G.add_edge('cnd','location')
G.edge['cnd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['location']['fill'] = 'red'
G.add_edge('cnd','location')
G.edge['cnd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['location']['fill'] = 'red'
G.add_edge('cnd','mediaserver')
G.edge['cnd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][setattr getattr][write read]'
G.edge['cnd']['mediaserver']['fill'] = 'red'
G.add_edge('cnd','mediaserver')
G.edge['cnd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read]'
G.edge['cnd']['mediaserver']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read]'
G.edge['cnd']['netmgrd']['fill'] = 'red'
G.add_edge('cnd','netmgrd')
G.edge['cnd']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read]'
G.edge['cnd']['netmgrd']['fill'] = 'red'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['cnd']['qmuxd']['fill'] = 'red'
G.add_edge('cnd','qmuxd')
G.edge['cnd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['cnd']['qmuxd']['fill'] = 'red'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['cnd']['qti']['fill'] = 'red'
G.add_edge('cnd','qti')
G.edge['cnd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['cnd']['qti']['fill'] = 'red'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['cnd']['radio']['fill'] = 'red'
G.add_edge('cnd','radio')
G.edge['cnd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['cnd']['radio']['fill'] = 'red'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['rild']['fill'] = 'red'
G.add_edge('cnd','rild')
G.edge['cnd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['rild']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['system_server']['fill'] = 'red'
G.add_edge('cnd','system_server')
G.edge['cnd']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['system_server']['fill'] = 'red'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['cnd']['thermal-engine']['fill'] = 'red'
G.add_edge('cnd','thermal-engine')
G.edge['cnd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['cnd']['thermal-engine']['fill'] = 'red'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['wcnss_service']['fill'] = 'red'
G.add_edge('cnd','wcnss_service')
G.edge['cnd']['wcnss_service']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['wcnss_service']['fill'] = 'red'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['cnd']['wpa']['fill'] = 'red'
G.add_edge('cnd','wpa')
G.edge['cnd']['wpa']['write-read'] = '[add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['cnd']['wpa']['fill'] = 'red'
G.add_edge('DMM-daemon','atfwd')
G.edge['DMM-daemon']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','bluetooth')
G.edge['DMM-daemon']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','cnd')
G.edge['DMM-daemon']['cnd']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','DMM-daemon')
G.edge['DMM-daemon']['DMM-daemon']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('DMM-daemon','dpmd')
G.edge['DMM-daemon']['dpmd']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','ims')
G.edge['DMM-daemon']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','location_app')
G.edge['DMM-daemon']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','location')
G.edge['DMM-daemon']['location']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','mediaserver')
G.edge['DMM-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('DMM-daemon','netmgrd')
G.edge['DMM-daemon']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('DMM-daemon','qmuxd')
G.edge['DMM-daemon']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','qti')
G.edge['DMM-daemon']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','radio')
G.edge['DMM-daemon']['radio']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('DMM-daemon','rild')
G.edge['DMM-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('DMM-daemon','system_server')
G.edge['DMM-daemon']['system_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][setattr getattr]'
G.add_edge('DMM-daemon','thermal-engine')
G.edge['DMM-daemon']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','wcnss_service')
G.edge['DMM-daemon']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','wpa')
G.edge['DMM-daemon']['wpa']['write-read'] = '[setattr getattr]'
G.add_edge('DMM-daemon','atfwd')
G.edge['DMM-daemon']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['atfwd']['fill'] = 'red'
G.add_edge('DMM-daemon','atfwd')
G.edge['DMM-daemon']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['atfwd']['fill'] = 'red'
G.add_edge('DMM-daemon','bluetooth')
G.edge['DMM-daemon']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('DMM-daemon','bluetooth')
G.edge['DMM-daemon']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('DMM-daemon','cnd')
G.edge['DMM-daemon']['cnd']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['cnd']['fill'] = 'red'
G.add_edge('DMM-daemon','cnd')
G.edge['DMM-daemon']['cnd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['cnd']['fill'] = 'red'
G.add_edge('DMM-daemon','DMM-daemon')
G.edge['DMM-daemon']['DMM-daemon']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['DMM-daemon']['DMM-daemon']['fill'] = 'red'
G.add_edge('DMM-daemon','DMM-daemon')
G.edge['DMM-daemon']['DMM-daemon']['write-read'] = '[write read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['DMM-daemon']['fill'] = 'red'
G.add_edge('DMM-daemon','dpmd')
G.edge['DMM-daemon']['dpmd']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['dpmd']['fill'] = 'red'
G.add_edge('DMM-daemon','dpmd')
G.edge['DMM-daemon']['dpmd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['dpmd']['fill'] = 'red'
G.add_edge('DMM-daemon','ims')
G.edge['DMM-daemon']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['ims']['fill'] = 'red'
G.add_edge('DMM-daemon','ims')
G.edge['DMM-daemon']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['ims']['fill'] = 'red'
G.add_edge('DMM-daemon','location_app')
G.edge['DMM-daemon']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['location_app']['fill'] = 'red'
G.add_edge('DMM-daemon','location_app')
G.edge['DMM-daemon']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['location_app']['fill'] = 'red'
G.add_edge('DMM-daemon','location')
G.edge['DMM-daemon']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['location']['fill'] = 'red'
G.add_edge('DMM-daemon','location')
G.edge['DMM-daemon']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['location']['fill'] = 'red'
G.add_edge('DMM-daemon','mediaserver')
G.edge['DMM-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['DMM-daemon']['mediaserver']['fill'] = 'red'
G.add_edge('DMM-daemon','mediaserver')
G.edge['DMM-daemon']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['mediaserver']['fill'] = 'red'
G.add_edge('DMM-daemon','netmgrd')
G.edge['DMM-daemon']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['DMM-daemon']['netmgrd']['fill'] = 'red'
G.add_edge('DMM-daemon','netmgrd')
G.edge['DMM-daemon']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['netmgrd']['fill'] = 'red'
G.add_edge('DMM-daemon','qmuxd')
G.edge['DMM-daemon']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['qmuxd']['fill'] = 'red'
G.add_edge('DMM-daemon','qmuxd')
G.edge['DMM-daemon']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['qmuxd']['fill'] = 'red'
G.add_edge('DMM-daemon','qti')
G.edge['DMM-daemon']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['qti']['fill'] = 'red'
G.add_edge('DMM-daemon','qti')
G.edge['DMM-daemon']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['qti']['fill'] = 'red'
G.add_edge('DMM-daemon','radio')
G.edge['DMM-daemon']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['DMM-daemon']['radio']['fill'] = 'red'
G.add_edge('DMM-daemon','radio')
G.edge['DMM-daemon']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['radio']['fill'] = 'red'
G.add_edge('DMM-daemon','rild')
G.edge['DMM-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['DMM-daemon']['rild']['fill'] = 'red'
G.add_edge('DMM-daemon','rild')
G.edge['DMM-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['rild']['fill'] = 'red'
G.add_edge('DMM-daemon','system_server')
G.edge['DMM-daemon']['system_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read]'
G.edge['DMM-daemon']['system_server']['fill'] = 'red'
G.add_edge('DMM-daemon','system_server')
G.edge['DMM-daemon']['system_server']['write-read'] = '[write read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][write read]'
G.edge['DMM-daemon']['system_server']['fill'] = 'red'
G.add_edge('DMM-daemon','thermal-engine')
G.edge['DMM-daemon']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('DMM-daemon','thermal-engine')
G.edge['DMM-daemon']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['thermal-engine']['fill'] = 'red'
G.add_edge('DMM-daemon','wcnss_service')
G.edge['DMM-daemon']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['wcnss_service']['fill'] = 'red'
G.add_edge('DMM-daemon','wcnss_service')
G.edge['DMM-daemon']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['wcnss_service']['fill'] = 'red'
G.add_edge('DMM-daemon','wpa')
G.edge['DMM-daemon']['wpa']['write-read'] = '[setattr getattr][write read]'
G.edge['DMM-daemon']['wpa']['fill'] = 'red'
G.add_edge('DMM-daemon','wpa')
G.edge['DMM-daemon']['wpa']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['DMM-daemon']['wpa']['fill'] = 'red'
G.add_edge('dpmd','atfwd')
G.edge['dpmd']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','DMM-daemon')
G.edge['dpmd']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','ims')
G.edge['dpmd']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','location_app')
G.edge['dpmd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','location')
G.edge['dpmd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('dpmd','atfwd')
G.edge['dpmd']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['atfwd']['fill'] = 'red'
G.add_edge('dpmd','atfwd')
G.edge['dpmd']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['dpmd']['atfwd']['fill'] = 'red'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['bluetooth']['fill'] = 'red'
G.add_edge('dpmd','bluetooth')
G.edge['dpmd']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['dpmd']['bluetooth']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['cnd']['fill'] = 'red'
G.add_edge('dpmd','cnd')
G.edge['dpmd']['cnd']['write-read'] = '[open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['cnd']['fill'] = 'red'
G.add_edge('dpmd','DMM-daemon')
G.edge['dpmd']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['DMM-daemon']['fill'] = 'red'
G.add_edge('dpmd','DMM-daemon')
G.edge['dpmd']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['dpmd']['DMM-daemon']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','dpmd')
G.edge['dpmd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['dpmd']['fill'] = 'red'
G.add_edge('dpmd','ims')
G.edge['dpmd']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['ims']['fill'] = 'red'
G.add_edge('dpmd','ims')
G.edge['dpmd']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['ims']['fill'] = 'red'
G.add_edge('dpmd','location_app')
G.edge['dpmd']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['location_app']['fill'] = 'red'
G.add_edge('dpmd','location_app')
G.edge['dpmd']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['dpmd']['location_app']['fill'] = 'red'
G.add_edge('dpmd','location')
G.edge['dpmd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['location']['fill'] = 'red'
G.add_edge('dpmd','location')
G.edge['dpmd']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['location']['fill'] = 'red'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['mediaserver']['fill'] = 'red'
G.add_edge('dpmd','mediaserver')
G.edge['dpmd']['mediaserver']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['dpmd']['mediaserver']['fill'] = 'red'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['netmgrd']['fill'] = 'red'
G.add_edge('dpmd','netmgrd')
G.edge['dpmd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['dpmd']['netmgrd']['fill'] = 'red'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['qmuxd']['fill'] = 'red'
G.add_edge('dpmd','qmuxd')
G.edge['dpmd']['qmuxd']['write-read'] = '[open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['dpmd']['qmuxd']['fill'] = 'red'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['dpmd']['qti']['fill'] = 'red'
G.add_edge('dpmd','qti')
G.edge['dpmd']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['dpmd']['qti']['fill'] = 'red'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['dpmd']['radio']['fill'] = 'red'
G.add_edge('dpmd','radio')
G.edge['dpmd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['dpmd']['radio']['fill'] = 'red'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['rild']['fill'] = 'red'
G.add_edge('dpmd','rild')
G.edge['dpmd']['rild']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['rild']['fill'] = 'red'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['system_server']['fill'] = 'red'
G.add_edge('dpmd','system_server')
G.edge['dpmd']['system_server']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['system_server']['fill'] = 'red'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['dpmd']['thermal-engine']['fill'] = 'red'
G.add_edge('dpmd','thermal-engine')
G.edge['dpmd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['dpmd']['thermal-engine']['fill'] = 'red'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['wcnss_service']['fill'] = 'red'
G.add_edge('dpmd','wcnss_service')
G.edge['dpmd']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['wcnss_service']['fill'] = 'red'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['dpmd']['wpa']['fill'] = 'red'
G.add_edge('dpmd','wpa')
G.edge['dpmd']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['dpmd']['wpa']['fill'] = 'red'
G.add_edge('ims','atfwd')
G.edge['ims']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('ims','bluetooth')
G.edge['ims']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('ims','cnd')
G.edge['ims']['cnd']['write-read'] = '[add_name search][remove_name search][write read][setopt getopt][setattr getattr]'
G.add_edge('ims','DMM-daemon')
G.edge['ims']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('ims','dpmd')
G.edge['ims']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','ims')
G.edge['ims']['ims']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','location_app')
G.edge['ims']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('ims','location')
G.edge['ims']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','mediaserver')
G.edge['ims']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('ims','netmgrd')
G.edge['ims']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('ims','qmuxd')
G.edge['ims']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('ims','qti')
G.edge['ims']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('ims','radio')
G.edge['ims']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('ims','rild')
G.edge['ims']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','thermal-engine')
G.edge['ims']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('ims','atfwd')
G.edge['ims']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['atfwd']['fill'] = 'red'
G.add_edge('ims','atfwd')
G.edge['ims']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['atfwd']['fill'] = 'red'
G.add_edge('ims','bluetooth')
G.edge['ims']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['bluetooth']['fill'] = 'red'
G.add_edge('ims','bluetooth')
G.edge['ims']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['bluetooth']['fill'] = 'red'
G.add_edge('ims','cnd')
G.edge['ims']['cnd']['write-read'] = '[add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['cnd']['fill'] = 'red'
G.add_edge('ims','cnd')
G.edge['ims']['cnd']['write-read'] = '[add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['cnd']['fill'] = 'red'
G.add_edge('ims','DMM-daemon')
G.edge['ims']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['DMM-daemon']['fill'] = 'red'
G.add_edge('ims','DMM-daemon')
G.edge['ims']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['DMM-daemon']['fill'] = 'red'
G.add_edge('ims','dpmd')
G.edge['ims']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['dpmd']['fill'] = 'red'
G.add_edge('ims','dpmd')
G.edge['ims']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['dpmd']['fill'] = 'red'
G.add_edge('ims','ims')
G.edge['ims']['ims']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['ims']['fill'] = 'red'
G.add_edge('ims','ims')
G.edge['ims']['ims']['write-read'] = '[open open][add_name search][remove_name search][open open][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['ims']['fill'] = 'red'
G.add_edge('ims','location_app')
G.edge['ims']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['location_app']['fill'] = 'red'
G.add_edge('ims','location_app')
G.edge['ims']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['location_app']['fill'] = 'red'
G.add_edge('ims','location')
G.edge['ims']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['location']['fill'] = 'red'
G.add_edge('ims','location')
G.edge['ims']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['location']['fill'] = 'red'
G.add_edge('ims','mediaserver')
G.edge['ims']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['mediaserver']['fill'] = 'red'
G.add_edge('ims','mediaserver')
G.edge['ims']['mediaserver']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['mediaserver']['fill'] = 'red'
G.add_edge('ims','netmgrd')
G.edge['ims']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['netmgrd']['fill'] = 'red'
G.add_edge('ims','netmgrd')
G.edge['ims']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['netmgrd']['fill'] = 'red'
G.add_edge('ims','qmuxd')
G.edge['ims']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['qmuxd']['fill'] = 'red'
G.add_edge('ims','qmuxd')
G.edge['ims']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['qmuxd']['fill'] = 'red'
G.add_edge('ims','qti')
G.edge['ims']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['ims']['qti']['fill'] = 'red'
G.add_edge('ims','qti')
G.edge['ims']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['ims']['qti']['fill'] = 'red'
G.add_edge('ims','radio')
G.edge['ims']['radio']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['radio']['fill'] = 'red'
G.add_edge('ims','radio')
G.edge['ims']['radio']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['radio']['fill'] = 'red'
G.add_edge('ims','rild')
G.edge['ims']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['ims']['rild']['fill'] = 'red'
G.add_edge('ims','rild')
G.edge['ims']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['rild']['fill'] = 'red'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['system_server']['fill'] = 'red'
G.add_edge('ims','system_server')
G.edge['ims']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['system_server']['fill'] = 'red'
G.add_edge('ims','thermal-engine')
G.edge['ims']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['ims']['thermal-engine']['fill'] = 'red'
G.add_edge('ims','thermal-engine')
G.edge['ims']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['ims']['thermal-engine']['fill'] = 'red'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['wcnss_service']['fill'] = 'red'
G.add_edge('ims','wcnss_service')
G.edge['ims']['wcnss_service']['write-read'] = '[open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['wcnss_service']['fill'] = 'red'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['ims']['wpa']['fill'] = 'red'
G.add_edge('ims','wpa')
G.edge['ims']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['ims']['wpa']['fill'] = 'red'
G.add_edge('location_app','atfwd')
G.edge['location_app']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','bluetooth')
G.edge['location_app']['bluetooth']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location_app','cnd')
G.edge['location_app']['cnd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','DMM-daemon')
G.edge['location_app']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','dpmd')
G.edge['location_app']['dpmd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','ims')
G.edge['location_app']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('location_app','netmgrd')
G.edge['location_app']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','qmuxd')
G.edge['location_app']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','qti')
G.edge['location_app']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','radio')
G.edge['location_app']['radio']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location_app','thermal-engine')
G.edge['location_app']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','wcnss_service')
G.edge['location_app']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','wpa')
G.edge['location_app']['wpa']['write-read'] = '[setattr getattr]'
G.add_edge('location_app','atfwd')
G.edge['location_app']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['atfwd']['fill'] = 'red'
G.add_edge('location_app','atfwd')
G.edge['location_app']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['atfwd']['fill'] = 'red'
G.add_edge('location_app','bluetooth')
G.edge['location_app']['bluetooth']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location_app']['bluetooth']['fill'] = 'red'
G.add_edge('location_app','bluetooth')
G.edge['location_app']['bluetooth']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location_app']['bluetooth']['fill'] = 'red'
G.add_edge('location_app','cnd')
G.edge['location_app']['cnd']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['cnd']['fill'] = 'red'
G.add_edge('location_app','cnd')
G.edge['location_app']['cnd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['cnd']['fill'] = 'red'
G.add_edge('location_app','DMM-daemon')
G.edge['location_app']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['DMM-daemon']['fill'] = 'red'
G.add_edge('location_app','DMM-daemon')
G.edge['location_app']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['DMM-daemon']['fill'] = 'red'
G.add_edge('location_app','dpmd')
G.edge['location_app']['dpmd']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['dpmd']['fill'] = 'red'
G.add_edge('location_app','dpmd')
G.edge['location_app']['dpmd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['dpmd']['fill'] = 'red'
G.add_edge('location_app','ims')
G.edge['location_app']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['ims']['fill'] = 'red'
G.add_edge('location_app','ims')
G.edge['location_app']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['ims']['fill'] = 'red'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location_app']['location_app']['fill'] = 'red'
G.add_edge('location_app','location_app')
G.edge['location_app']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location_app']['location_app']['fill'] = 'red'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location_app']['location']['fill'] = 'red'
G.add_edge('location_app','location')
G.edge['location_app']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location_app']['location']['fill'] = 'red'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['location_app']['mediaserver']['fill'] = 'red'
G.add_edge('location_app','mediaserver')
G.edge['location_app']['mediaserver']['write-read'] = '[open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][write read]'
G.edge['location_app']['mediaserver']['fill'] = 'red'
G.add_edge('location_app','netmgrd')
G.edge['location_app']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['netmgrd']['fill'] = 'red'
G.add_edge('location_app','netmgrd')
G.edge['location_app']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['netmgrd']['fill'] = 'red'
G.add_edge('location_app','qmuxd')
G.edge['location_app']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['qmuxd']['fill'] = 'red'
G.add_edge('location_app','qmuxd')
G.edge['location_app']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['qmuxd']['fill'] = 'red'
G.add_edge('location_app','qti')
G.edge['location_app']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['qti']['fill'] = 'red'
G.add_edge('location_app','qti')
G.edge['location_app']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['qti']['fill'] = 'red'
G.add_edge('location_app','radio')
G.edge['location_app']['radio']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['location_app']['radio']['fill'] = 'red'
G.add_edge('location_app','radio')
G.edge['location_app']['radio']['write-read'] = '[setattr getattr][setattr getattr][write read][write read]'
G.edge['location_app']['radio']['fill'] = 'red'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location_app']['rild']['fill'] = 'red'
G.add_edge('location_app','rild')
G.edge['location_app']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location_app']['rild']['fill'] = 'red'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location_app']['system_server']['fill'] = 'red'
G.add_edge('location_app','system_server')
G.edge['location_app']['system_server']['write-read'] = '[open open][setattr getattr][write read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location_app']['system_server']['fill'] = 'red'
G.add_edge('location_app','thermal-engine')
G.edge['location_app']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['thermal-engine']['fill'] = 'red'
G.add_edge('location_app','thermal-engine')
G.edge['location_app']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['thermal-engine']['fill'] = 'red'
G.add_edge('location_app','wcnss_service')
G.edge['location_app']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['wcnss_service']['fill'] = 'red'
G.add_edge('location_app','wcnss_service')
G.edge['location_app']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['wcnss_service']['fill'] = 'red'
G.add_edge('location_app','wpa')
G.edge['location_app']['wpa']['write-read'] = '[setattr getattr][write read]'
G.edge['location_app']['wpa']['fill'] = 'red'
G.add_edge('location_app','wpa')
G.edge['location_app']['wpa']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location_app']['wpa']['fill'] = 'red'
G.add_edge('location','atfwd')
G.edge['location']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('location','bluetooth')
G.edge['location']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('location','cnd')
G.edge['location']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr]'
G.add_edge('location','DMM-daemon')
G.edge['location']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('location','dpmd')
G.edge['location']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','ims')
G.edge['location']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','mediaserver')
G.edge['location']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('location','netmgrd')
G.edge['location']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('location','qmuxd')
G.edge['location']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('location','qti')
G.edge['location']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('location','radio')
G.edge['location']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('location','rild')
G.edge['location']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','thermal-engine')
G.edge['location']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('location','wcnss_service')
G.edge['location']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','wpa')
G.edge['location']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('location','atfwd')
G.edge['location']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['atfwd']['fill'] = 'red'
G.add_edge('location','atfwd')
G.edge['location']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['atfwd']['fill'] = 'red'
G.add_edge('location','bluetooth')
G.edge['location']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['bluetooth']['fill'] = 'red'
G.add_edge('location','bluetooth')
G.edge['location']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['bluetooth']['fill'] = 'red'
G.add_edge('location','cnd')
G.edge['location']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read]'
G.edge['location']['cnd']['fill'] = 'red'
G.add_edge('location','cnd')
G.edge['location']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['cnd']['fill'] = 'red'
G.add_edge('location','DMM-daemon')
G.edge['location']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['DMM-daemon']['fill'] = 'red'
G.add_edge('location','DMM-daemon')
G.edge['location']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['DMM-daemon']['fill'] = 'red'
G.add_edge('location','dpmd')
G.edge['location']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['dpmd']['fill'] = 'red'
G.add_edge('location','dpmd')
G.edge['location']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['dpmd']['fill'] = 'red'
G.add_edge('location','ims')
G.edge['location']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['ims']['fill'] = 'red'
G.add_edge('location','ims')
G.edge['location']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['ims']['fill'] = 'red'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['location']['location_app']['fill'] = 'red'
G.add_edge('location','location_app')
G.edge['location']['location_app']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['location']['location_app']['fill'] = 'red'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['location']['fill'] = 'red'
G.add_edge('location','location')
G.edge['location']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['location']['fill'] = 'red'
G.add_edge('location','mediaserver')
G.edge['location']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['mediaserver']['fill'] = 'red'
G.add_edge('location','mediaserver')
G.edge['location']['mediaserver']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['mediaserver']['fill'] = 'red'
G.add_edge('location','netmgrd')
G.edge['location']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['netmgrd']['fill'] = 'red'
G.add_edge('location','netmgrd')
G.edge['location']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['netmgrd']['fill'] = 'red'
G.add_edge('location','qmuxd')
G.edge['location']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['qmuxd']['fill'] = 'red'
G.add_edge('location','qmuxd')
G.edge['location']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['qmuxd']['fill'] = 'red'
G.add_edge('location','qti')
G.edge['location']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['location']['qti']['fill'] = 'red'
G.add_edge('location','qti')
G.edge['location']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['location']['qti']['fill'] = 'red'
G.add_edge('location','radio')
G.edge['location']['radio']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['radio']['fill'] = 'red'
G.add_edge('location','radio')
G.edge['location']['radio']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['radio']['fill'] = 'red'
G.add_edge('location','rild')
G.edge['location']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['location']['rild']['fill'] = 'red'
G.add_edge('location','rild')
G.edge['location']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['rild']['fill'] = 'red'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['system_server']['fill'] = 'red'
G.add_edge('location','system_server')
G.edge['location']['system_server']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['system_server']['fill'] = 'red'
G.add_edge('location','thermal-engine')
G.edge['location']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['location']['thermal-engine']['fill'] = 'red'
G.add_edge('location','thermal-engine')
G.edge['location']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['location']['thermal-engine']['fill'] = 'red'
G.add_edge('location','wcnss_service')
G.edge['location']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['wcnss_service']['fill'] = 'red'
G.add_edge('location','wcnss_service')
G.edge['location']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['wcnss_service']['fill'] = 'red'
G.add_edge('location','wpa')
G.edge['location']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['location']['wpa']['fill'] = 'red'
G.add_edge('location','wpa')
G.edge['location']['wpa']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['location']['wpa']['fill'] = 'red'
G.add_edge('mediaserver','atfwd')
G.edge['mediaserver']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','DMM-daemon')
G.edge['mediaserver']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('mediaserver','ims')
G.edge['mediaserver']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('mediaserver','location')
G.edge['mediaserver']['location']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][setattr getattr]'
G.add_edge('mediaserver','netmgrd')
G.edge['mediaserver']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','qti')
G.edge['mediaserver']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read][setattr getattr]'
G.add_edge('mediaserver','wcnss_service')
G.edge['mediaserver']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('mediaserver','wpa')
G.edge['mediaserver']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('mediaserver','atfwd')
G.edge['mediaserver']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['atfwd']['fill'] = 'red'
G.add_edge('mediaserver','atfwd')
G.edge['mediaserver']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['mediaserver']['atfwd']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','bluetooth')
G.edge['mediaserver']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['mediaserver']['bluetooth']['fill'] = 'red'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['cnd']['fill'] = 'red'
G.add_edge('mediaserver','cnd')
G.edge['mediaserver']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['cnd']['fill'] = 'red'
G.add_edge('mediaserver','DMM-daemon')
G.edge['mediaserver']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['DMM-daemon']['fill'] = 'red'
G.add_edge('mediaserver','DMM-daemon')
G.edge['mediaserver']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['DMM-daemon']['fill'] = 'red'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['dpmd']['fill'] = 'red'
G.add_edge('mediaserver','dpmd')
G.edge['mediaserver']['dpmd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['dpmd']['fill'] = 'red'
G.add_edge('mediaserver','ims')
G.edge['mediaserver']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['ims']['fill'] = 'red'
G.add_edge('mediaserver','ims')
G.edge['mediaserver']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['mediaserver']['ims']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['location_app']['fill'] = 'red'
G.add_edge('mediaserver','location_app')
G.edge['mediaserver']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['location_app']['fill'] = 'red'
G.add_edge('mediaserver','location')
G.edge['mediaserver']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['location']['fill'] = 'red'
G.add_edge('mediaserver','location')
G.edge['mediaserver']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['mediaserver']['location']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','mediaserver')
G.edge['mediaserver']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['mediaserver']['fill'] = 'red'
G.add_edge('mediaserver','netmgrd')
G.edge['mediaserver']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mediaserver']['netmgrd']['fill'] = 'red'
G.add_edge('mediaserver','netmgrd')
G.edge['mediaserver']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['mediaserver']['netmgrd']['fill'] = 'red'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mediaserver']['qmuxd']['fill'] = 'red'
G.add_edge('mediaserver','qmuxd')
G.edge['mediaserver']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['mediaserver']['qmuxd']['fill'] = 'red'
G.add_edge('mediaserver','qti')
G.edge['mediaserver']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['qti']['fill'] = 'red'
G.add_edge('mediaserver','qti')
G.edge['mediaserver']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['mediaserver']['qti']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mediaserver']['radio']['fill'] = 'red'
G.add_edge('mediaserver','radio')
G.edge['mediaserver']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][write read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['mediaserver']['radio']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','rild')
G.edge['mediaserver']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['mediaserver']['rild']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','system_server')
G.edge['mediaserver']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][append read][write read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][open open][write read][append read][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['system_server']['fill'] = 'red'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read][setattr getattr][write read]'
G.edge['mediaserver']['thermal-engine']['fill'] = 'red'
G.add_edge('mediaserver','thermal-engine')
G.edge['mediaserver']['thermal-engine']['write-read'] = '[open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read][setattr getattr][write read][write read]'
G.edge['mediaserver']['thermal-engine']['fill'] = 'red'
G.add_edge('mediaserver','wcnss_service')
G.edge['mediaserver']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['mediaserver']['wcnss_service']['fill'] = 'red'
G.add_edge('mediaserver','wcnss_service')
G.edge['mediaserver']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['mediaserver']['wcnss_service']['fill'] = 'red'
G.add_edge('mediaserver','wpa')
G.edge['mediaserver']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['mediaserver']['wpa']['fill'] = 'red'
G.add_edge('mediaserver','wpa')
G.edge['mediaserver']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['mediaserver']['wpa']['fill'] = 'red'
G.add_edge('netmgrd','atfwd')
G.edge['netmgrd']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','bluetooth')
G.edge['netmgrd']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('netmgrd','DMM-daemon')
G.edge['netmgrd']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('netmgrd','ims')
G.edge['netmgrd']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','location_app')
G.edge['netmgrd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','location')
G.edge['netmgrd']['location']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','mediaserver')
G.edge['netmgrd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr]'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('netmgrd','atfwd')
G.edge['netmgrd']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['atfwd']['fill'] = 'red'
G.add_edge('netmgrd','atfwd')
G.edge['netmgrd']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['atfwd']['fill'] = 'red'
G.add_edge('netmgrd','bluetooth')
G.edge['netmgrd']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['bluetooth']['fill'] = 'red'
G.add_edge('netmgrd','bluetooth')
G.edge['netmgrd']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['bluetooth']['fill'] = 'red'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['netmgrd']['cnd']['fill'] = 'red'
G.add_edge('netmgrd','cnd')
G.edge['netmgrd']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['netmgrd']['cnd']['fill'] = 'red'
G.add_edge('netmgrd','DMM-daemon')
G.edge['netmgrd']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['DMM-daemon']['fill'] = 'red'
G.add_edge('netmgrd','DMM-daemon')
G.edge['netmgrd']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['DMM-daemon']['fill'] = 'red'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['netmgrd']['dpmd']['fill'] = 'red'
G.add_edge('netmgrd','dpmd')
G.edge['netmgrd']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['netmgrd']['dpmd']['fill'] = 'red'
G.add_edge('netmgrd','ims')
G.edge['netmgrd']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['ims']['fill'] = 'red'
G.add_edge('netmgrd','ims')
G.edge['netmgrd']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['ims']['fill'] = 'red'
G.add_edge('netmgrd','location_app')
G.edge['netmgrd']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['location_app']['fill'] = 'red'
G.add_edge('netmgrd','location_app')
G.edge['netmgrd']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['location_app']['fill'] = 'red'
G.add_edge('netmgrd','location')
G.edge['netmgrd']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['location']['fill'] = 'red'
G.add_edge('netmgrd','location')
G.edge['netmgrd']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['location']['fill'] = 'red'
G.add_edge('netmgrd','mediaserver')
G.edge['netmgrd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['netmgrd']['mediaserver']['fill'] = 'red'
G.add_edge('netmgrd','mediaserver')
G.edge['netmgrd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][write read]'
G.edge['netmgrd']['mediaserver']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
G.add_edge('netmgrd','netmgrd')
G.edge['netmgrd']['netmgrd']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][write read][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['netmgrd']['netmgrd']['fill'] = 'red'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['netmgrd']['qmuxd']['fill'] = 'red'
G.add_edge('netmgrd','qmuxd')
G.edge['netmgrd']['qmuxd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['netmgrd']['qmuxd']['fill'] = 'red'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['qti']['fill'] = 'red'
G.add_edge('netmgrd','qti')
G.edge['netmgrd']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['qti']['fill'] = 'red'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netmgrd']['radio']['fill'] = 'red'
G.add_edge('netmgrd','radio')
G.edge['netmgrd']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['netmgrd']['radio']['fill'] = 'red'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netmgrd']['rild']['fill'] = 'red'
G.add_edge('netmgrd','rild')
G.edge['netmgrd']['rild']['write-read'] = '[open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['netmgrd']['rild']['fill'] = 'red'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['netmgrd']['system_server']['fill'] = 'red'
G.add_edge('netmgrd','system_server')
G.edge['netmgrd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['netmgrd']['system_server']['fill'] = 'red'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['thermal-engine']['fill'] = 'red'
G.add_edge('netmgrd','thermal-engine')
G.edge['netmgrd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['thermal-engine']['fill'] = 'red'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['netmgrd']['wcnss_service']['fill'] = 'red'
G.add_edge('netmgrd','wcnss_service')
G.edge['netmgrd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['netmgrd']['wcnss_service']['fill'] = 'red'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['netmgrd']['wpa']['fill'] = 'red'
G.add_edge('netmgrd','wpa')
G.edge['netmgrd']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['netmgrd']['wpa']['fill'] = 'red'
G.add_edge('qmuxd','atfwd')
G.edge['qmuxd']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','DMM-daemon')
G.edge['qmuxd']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','ims')
G.edge['qmuxd']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','location_app')
G.edge['qmuxd']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','location')
G.edge['qmuxd']['location']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','thermal-engine')
G.edge['qmuxd']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','wcnss_service')
G.edge['qmuxd']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('qmuxd','atfwd')
G.edge['qmuxd']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['atfwd']['fill'] = 'red'
G.add_edge('qmuxd','atfwd')
G.edge['qmuxd']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['atfwd']['fill'] = 'red'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['bluetooth']['fill'] = 'red'
G.add_edge('qmuxd','bluetooth')
G.edge['qmuxd']['bluetooth']['write-read'] = '[open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['bluetooth']['fill'] = 'red'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['cnd']['fill'] = 'red'
G.add_edge('qmuxd','cnd')
G.edge['qmuxd']['cnd']['write-read'] = '[open open][add_name search][remove_name search][open open][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['qmuxd']['cnd']['fill'] = 'red'
G.add_edge('qmuxd','DMM-daemon')
G.edge['qmuxd']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['DMM-daemon']['fill'] = 'red'
G.add_edge('qmuxd','DMM-daemon')
G.edge['qmuxd']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['DMM-daemon']['fill'] = 'red'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['dpmd']['fill'] = 'red'
G.add_edge('qmuxd','dpmd')
G.edge['qmuxd']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['qmuxd']['dpmd']['fill'] = 'red'
G.add_edge('qmuxd','ims')
G.edge['qmuxd']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['ims']['fill'] = 'red'
G.add_edge('qmuxd','ims')
G.edge['qmuxd']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['ims']['fill'] = 'red'
G.add_edge('qmuxd','location_app')
G.edge['qmuxd']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['location_app']['fill'] = 'red'
G.add_edge('qmuxd','location_app')
G.edge['qmuxd']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['location_app']['fill'] = 'red'
G.add_edge('qmuxd','location')
G.edge['qmuxd']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['location']['fill'] = 'red'
G.add_edge('qmuxd','location')
G.edge['qmuxd']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['location']['fill'] = 'red'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['mediaserver']['fill'] = 'red'
G.add_edge('qmuxd','mediaserver')
G.edge['qmuxd']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['mediaserver']['fill'] = 'red'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['netmgrd']['fill'] = 'red'
G.add_edge('qmuxd','netmgrd')
G.edge['qmuxd']['netmgrd']['write-read'] = '[open open][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['qmuxd']['netmgrd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qmuxd')
G.edge['qmuxd']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][add_name search][remove_name search][open open][add_name search][remove_name search][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['qmuxd']['fill'] = 'red'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['qmuxd']['qti']['fill'] = 'red'
G.add_edge('qmuxd','qti')
G.edge['qmuxd']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['qmuxd']['qti']['fill'] = 'red'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['radio']['fill'] = 'red'
G.add_edge('qmuxd','radio')
G.edge['qmuxd']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['radio']['fill'] = 'red'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['rild']['fill'] = 'red'
G.add_edge('qmuxd','rild')
G.edge['qmuxd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['rild']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','system_server')
G.edge['qmuxd']['system_server']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['system_server']['fill'] = 'red'
G.add_edge('qmuxd','thermal-engine')
G.edge['qmuxd']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['thermal-engine']['fill'] = 'red'
G.add_edge('qmuxd','thermal-engine')
G.edge['qmuxd']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['thermal-engine']['fill'] = 'red'
G.add_edge('qmuxd','wcnss_service')
G.edge['qmuxd']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['qmuxd']['wcnss_service']['fill'] = 'red'
G.add_edge('qmuxd','wcnss_service')
G.edge['qmuxd']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qmuxd']['wcnss_service']['fill'] = 'red'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['qmuxd']['wpa']['fill'] = 'red'
G.add_edge('qmuxd','wpa')
G.edge['qmuxd']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['qmuxd']['wpa']['fill'] = 'red'
G.add_edge('qti','atfwd')
G.edge['qti']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr]'
G.add_edge('qti','DMM-daemon')
G.edge['qti']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr]'
G.add_edge('qti','ims')
G.edge['qti']['ims']['write-read'] = '[write read][append read][setattr getattr]'
G.add_edge('qti','location_app')
G.edge['qti']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('qti','location')
G.edge['qti']['location']['write-read'] = '[write read][append read][setattr getattr]'
G.add_edge('qti','mediaserver')
G.edge['qti']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr]'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('qti','rild')
G.edge['qti']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr]'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open][write read][append read][write read][append read][setattr getattr]'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr]'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr]'
G.add_edge('qti','atfwd')
G.edge['qti']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['atfwd']['fill'] = 'red'
G.add_edge('qti','atfwd')
G.edge['qti']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['atfwd']['fill'] = 'red'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['qti']['bluetooth']['fill'] = 'red'
G.add_edge('qti','bluetooth')
G.edge['qti']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['bluetooth']['fill'] = 'red'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['qti']['cnd']['fill'] = 'red'
G.add_edge('qti','cnd')
G.edge['qti']['cnd']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['qti']['cnd']['fill'] = 'red'
G.add_edge('qti','DMM-daemon')
G.edge['qti']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['DMM-daemon']['fill'] = 'red'
G.add_edge('qti','DMM-daemon')
G.edge['qti']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['DMM-daemon']['fill'] = 'red'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr][write read]'
G.edge['qti']['dpmd']['fill'] = 'red'
G.add_edge('qti','dpmd')
G.edge['qti']['dpmd']['write-read'] = '[write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['dpmd']['fill'] = 'red'
G.add_edge('qti','ims')
G.edge['qti']['ims']['write-read'] = '[write read][append read][setattr getattr][write read]'
G.edge['qti']['ims']['fill'] = 'red'
G.add_edge('qti','ims')
G.edge['qti']['ims']['write-read'] = '[write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['ims']['fill'] = 'red'
G.add_edge('qti','location_app')
G.edge['qti']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['location_app']['fill'] = 'red'
G.add_edge('qti','location_app')
G.edge['qti']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['location_app']['fill'] = 'red'
G.add_edge('qti','location')
G.edge['qti']['location']['write-read'] = '[write read][append read][setattr getattr][write read]'
G.edge['qti']['location']['fill'] = 'red'
G.add_edge('qti','location')
G.edge['qti']['location']['write-read'] = '[write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['location']['fill'] = 'red'
G.add_edge('qti','mediaserver')
G.edge['qti']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['mediaserver']['fill'] = 'red'
G.add_edge('qti','mediaserver')
G.edge['qti']['mediaserver']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['mediaserver']['fill'] = 'red'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['netmgrd']['fill'] = 'red'
G.add_edge('qti','netmgrd')
G.edge['qti']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['netmgrd']['fill'] = 'red'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['qti']['qmuxd']['fill'] = 'red'
G.add_edge('qti','qmuxd')
G.edge['qti']['qmuxd']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['qmuxd']['fill'] = 'red'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read]'
G.edge['qti']['qti']['fill'] = 'red'
G.add_edge('qti','qti')
G.edge['qti']['qti']['write-read'] = '[open open][write read][append read][open open][write read][append read][write read][write read][setattr getattr][write read][write read]'
G.edge['qti']['qti']['fill'] = 'red'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['qti']['radio']['fill'] = 'red'
G.add_edge('qti','radio')
G.edge['qti']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['radio']['fill'] = 'red'
G.add_edge('qti','rild')
G.edge['qti']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read]'
G.edge['qti']['rild']['fill'] = 'red'
G.add_edge('qti','rild')
G.edge['qti']['rild']['write-read'] = '[write read][append read][write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['rild']['fill'] = 'red'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open][write read][append read][write read][append read][setattr getattr][write read]'
G.edge['qti']['system_server']['fill'] = 'red'
G.add_edge('qti','system_server')
G.edge['qti']['system_server']['write-read'] = '[open open][write read][append read][write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['system_server']['fill'] = 'red'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['qti']['thermal-engine']['fill'] = 'red'
G.add_edge('qti','thermal-engine')
G.edge['qti']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['qti']['thermal-engine']['fill'] = 'red'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr][write read]'
G.edge['qti']['wcnss_service']['fill'] = 'red'
G.add_edge('qti','wcnss_service')
G.edge['qti']['wcnss_service']['write-read'] = '[write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['wcnss_service']['fill'] = 'red'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr][write read]'
G.edge['qti']['wpa']['fill'] = 'red'
G.add_edge('qti','wpa')
G.edge['qti']['wpa']['write-read'] = '[write read][append read][setattr getattr][write read][write read]'
G.edge['qti']['wpa']['fill'] = 'red'
G.add_edge('radio','atfwd')
G.edge['radio']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('radio','DMM-daemon')
G.edge['radio']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('radio','ims')
G.edge['radio']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('radio','location_app')
G.edge['radio']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('radio','location')
G.edge['radio']['location']['write-read'] = '[setattr getattr]'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('radio','thermal-engine')
G.edge['radio']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('radio','wcnss_service')
G.edge['radio']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('radio','wpa')
G.edge['radio']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('radio','atfwd')
G.edge['radio']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['atfwd']['fill'] = 'red'
G.add_edge('radio','atfwd')
G.edge['radio']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['atfwd']['fill'] = 'red'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['bluetooth']['fill'] = 'red'
G.add_edge('radio','bluetooth')
G.edge['radio']['bluetooth']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['bluetooth']['fill'] = 'red'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['radio']['cnd']['fill'] = 'red'
G.add_edge('radio','cnd')
G.edge['radio']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['radio']['cnd']['fill'] = 'red'
G.add_edge('radio','DMM-daemon')
G.edge['radio']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['DMM-daemon']['fill'] = 'red'
G.add_edge('radio','DMM-daemon')
G.edge['radio']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['DMM-daemon']['fill'] = 'red'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['radio']['dpmd']['fill'] = 'red'
G.add_edge('radio','dpmd')
G.edge['radio']['dpmd']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['radio']['dpmd']['fill'] = 'red'
G.add_edge('radio','ims')
G.edge['radio']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['ims']['fill'] = 'red'
G.add_edge('radio','ims')
G.edge['radio']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['ims']['fill'] = 'red'
G.add_edge('radio','location_app')
G.edge['radio']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['location_app']['fill'] = 'red'
G.add_edge('radio','location_app')
G.edge['radio']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['location_app']['fill'] = 'red'
G.add_edge('radio','location')
G.edge['radio']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['location']['fill'] = 'red'
G.add_edge('radio','location')
G.edge['radio']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['location']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','mediaserver')
G.edge['radio']['mediaserver']['write-read'] = '[add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['mediaserver']['fill'] = 'red'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['netmgrd']['fill'] = 'red'
G.add_edge('radio','netmgrd')
G.edge['radio']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['netmgrd']['fill'] = 'red'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['qmuxd']['fill'] = 'red'
G.add_edge('radio','qmuxd')
G.edge['radio']['qmuxd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['qmuxd']['fill'] = 'red'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['qti']['fill'] = 'red'
G.add_edge('radio','qti')
G.edge['radio']['qti']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['radio']['qti']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','radio')
G.edge['radio']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['radio']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','rild')
G.edge['radio']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['rild']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','system_server')
G.edge['radio']['system_server']['write-read'] = '[add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][append read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['radio']['system_server']['fill'] = 'red'
G.add_edge('radio','thermal-engine')
G.edge['radio']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['thermal-engine']['fill'] = 'red'
G.add_edge('radio','thermal-engine')
G.edge['radio']['thermal-engine']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['radio']['thermal-engine']['fill'] = 'red'
G.add_edge('radio','wcnss_service')
G.edge['radio']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['radio']['wcnss_service']['fill'] = 'red'
G.add_edge('radio','wcnss_service')
G.edge['radio']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['radio']['wcnss_service']['fill'] = 'red'
G.add_edge('radio','wpa')
G.edge['radio']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['radio']['wpa']['fill'] = 'red'
G.add_edge('radio','wpa')
G.edge['radio']['wpa']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['radio']['wpa']['fill'] = 'red'
G.add_edge('rild','atfwd')
G.edge['rild']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr]'
G.add_edge('rild','DMM-daemon')
G.edge['rild']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr]'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('rild','ims')
G.edge['rild']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','location')
G.edge['rild']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','qti')
G.edge['rild']['qti']['write-read'] = '[write read][write read][setattr getattr]'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read][open open][write read][append read][setattr getattr]'
G.add_edge('rild','wcnss_service')
G.edge['rild']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('rild','atfwd')
G.edge['rild']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['rild']['atfwd']['fill'] = 'red'
G.add_edge('rild','atfwd')
G.edge['rild']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['rild']['atfwd']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['cnd']['fill'] = 'red'
G.add_edge('rild','cnd')
G.edge['rild']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['cnd']['fill'] = 'red'
G.add_edge('rild','DMM-daemon')
G.edge['rild']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['rild']['DMM-daemon']['fill'] = 'red'
G.add_edge('rild','DMM-daemon')
G.edge['rild']['DMM-daemon']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['rild']['DMM-daemon']['fill'] = 'red'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['dpmd']['fill'] = 'red'
G.add_edge('rild','dpmd')
G.edge['rild']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['dpmd']['fill'] = 'red'
G.add_edge('rild','ims')
G.edge['rild']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['ims']['fill'] = 'red'
G.add_edge('rild','ims')
G.edge['rild']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['ims']['fill'] = 'red'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['location_app']['fill'] = 'red'
G.add_edge('rild','location_app')
G.edge['rild']['location_app']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['location_app']['fill'] = 'red'
G.add_edge('rild','location')
G.edge['rild']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['location']['fill'] = 'red'
G.add_edge('rild','location')
G.edge['rild']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['location']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','mediaserver')
G.edge['rild']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['mediaserver']['fill'] = 'red'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['netmgrd']['fill'] = 'red'
G.add_edge('rild','netmgrd')
G.edge['rild']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][open open][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['netmgrd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','qmuxd')
G.edge['rild']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['qmuxd']['fill'] = 'red'
G.add_edge('rild','qti')
G.edge['rild']['qti']['write-read'] = '[write read][write read][setattr getattr][write read]'
G.edge['rild']['qti']['fill'] = 'red'
G.add_edge('rild','qti')
G.edge['rild']['qti']['write-read'] = '[write read][write read][setattr getattr][write read][write read]'
G.edge['rild']['qti']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','radio')
G.edge['rild']['radio']['write-read'] = '[open open][setattr getattr][write read][append read][setattr getattr][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['radio']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][open open][open open][setattr getattr][write read][append read][write read][append read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][write read][append read][write read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','system_server')
G.edge['rild']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['rild']['system_server']['fill'] = 'red'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read]'
G.edge['rild']['thermal-engine']['fill'] = 'red'
G.add_edge('rild','thermal-engine')
G.edge['rild']['thermal-engine']['write-read'] = '[setopt getopt][open open][write read][append read][write read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['rild']['thermal-engine']['fill'] = 'red'
G.add_edge('rild','wcnss_service')
G.edge['rild']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['wcnss_service']['fill'] = 'red'
G.add_edge('rild','wcnss_service')
G.edge['rild']['wcnss_service']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['wcnss_service']['fill'] = 'red'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['rild']['wpa']['fill'] = 'red'
G.add_edge('rild','wpa')
G.edge['rild']['wpa']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['rild']['wpa']['fill'] = 'red'
G.add_edge('system_server','atfwd')
G.edge['system_server']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr]'
G.add_edge('system_server','DMM-daemon')
G.edge['system_server']['DMM-daemon']['write-read'] = '[setattr getattr][write read][append read][setattr getattr]'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','ims')
G.edge['system_server']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open][write read][append read][write read][setattr getattr]'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][setattr getattr][write read][open open][write read][append read][setattr getattr]'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('system_server','atfwd')
G.edge['system_server']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['system_server']['atfwd']['fill'] = 'red'
G.add_edge('system_server','atfwd')
G.edge['system_server']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['system_server']['atfwd']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','bluetooth')
G.edge['system_server']['bluetooth']['write-read'] = '[setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][setattr getattr][write read][append read][setopt getopt][open open][open open][write read][append read][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['bluetooth']['fill'] = 'red'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['cnd']['fill'] = 'red'
G.add_edge('system_server','cnd')
G.edge['system_server']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['cnd']['fill'] = 'red'
G.add_edge('system_server','DMM-daemon')
G.edge['system_server']['DMM-daemon']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read]'
G.edge['system_server']['DMM-daemon']['fill'] = 'red'
G.add_edge('system_server','DMM-daemon')
G.edge['system_server']['DMM-daemon']['write-read'] = '[setattr getattr][write read][append read][setattr getattr][write read][write read]'
G.edge['system_server']['DMM-daemon']['fill'] = 'red'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['dpmd']['fill'] = 'red'
G.add_edge('system_server','dpmd')
G.edge['system_server']['dpmd']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['dpmd']['fill'] = 'red'
G.add_edge('system_server','ims')
G.edge['system_server']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['ims']['fill'] = 'red'
G.add_edge('system_server','ims')
G.edge['system_server']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['ims']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['location_app']['fill'] = 'red'
G.add_edge('system_server','location_app')
G.edge['system_server']['location_app']['write-read'] = '[setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['location_app']['fill'] = 'red'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['location']['fill'] = 'red'
G.add_edge('system_server','location')
G.edge['system_server']['location']['write-read'] = '[open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['location']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','mediaserver')
G.edge['system_server']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][write read][write read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][write read][append read][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['system_server']['mediaserver']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['netmgrd']['fill'] = 'red'
G.add_edge('system_server','netmgrd')
G.edge['system_server']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['netmgrd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qmuxd')
G.edge['system_server']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][open open][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['qmuxd']['fill'] = 'red'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open][write read][append read][write read][setattr getattr][write read]'
G.edge['system_server']['qti']['fill'] = 'red'
G.add_edge('system_server','qti')
G.edge['system_server']['qti']['write-read'] = '[open open][write read][append read][write read][setattr getattr][write read][write read]'
G.edge['system_server']['qti']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','radio')
G.edge['system_server']['radio']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][append read][open open][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['radio']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','rild')
G.edge['system_server']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['system_server']['rild']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','system_server')
G.edge['system_server']['system_server']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][open open][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][open open][write read][append read][open open][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setattr getattr][write read][write read][append read][open open][setattr getattr][write read][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][add_name search][remove_name search][setsched getsched][open open][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][open open][write read][append read][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search][write read][open open][write read][add_name search][remove_name search][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][write read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][setopt getopt][write read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][open open][setattr getattr][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][append read][setopt getopt][open open][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setsched getsched][open open][setattr getattr][write read][append read][open open][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][write read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][write read][open open][write read][append read][open open][write read][append read][open open][write read][append read][write read][write read][append read][write read][open open][write read][append read][write read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][append read][write read][setattr getattr][write read][append read][write read][open open][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][setattr getattr][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][add_name search][remove_name search][write read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][write read][setopt getopt][open open][open open][write read][append read][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][write read][remove_name search][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][write read][append read][setopt getopt][setsched getsched][setsched getsched][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][relabelto relabelfrom][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][add_name search][remove_name search][open open][write read][append read][setsched getsched][setsched getsched][open open][write read][append read][relabelto relabelfrom][open open][open open][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][write read][append read][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['system_server']['system_server']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][setattr getattr][write read][open open][write read][append read][setattr getattr][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','thermal-engine')
G.edge['system_server']['thermal-engine']['write-read'] = '[setopt getopt][write read][open open][write read][append read][write read][open open][write read][append read][write read][open open][write read][append read][open open][setattr getattr][write read][setattr getattr][write read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['system_server']['thermal-engine']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wcnss_service')
G.edge['system_server']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['wcnss_service']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('system_server','wpa')
G.edge['system_server']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['system_server']['wpa']['fill'] = 'red'
G.add_edge('thermal-engine','atfwd')
G.edge['thermal-engine']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','bluetooth')
G.edge['thermal-engine']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','DMM-daemon')
G.edge['thermal-engine']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','ims')
G.edge['thermal-engine']['ims']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','location_app')
G.edge['thermal-engine']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','location')
G.edge['thermal-engine']['location']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','mediaserver')
G.edge['thermal-engine']['mediaserver']['write-read'] = '[open open][write read][append read][write read][setattr getattr]'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','qmuxd')
G.edge['thermal-engine']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','radio')
G.edge['thermal-engine']['radio']['write-read'] = '[open open][write read][append read][setattr getattr]'
G.add_edge('thermal-engine','rild')
G.edge['thermal-engine']['rild']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('thermal-engine','system_server')
G.edge['thermal-engine']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr]'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr]'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr]'
G.add_edge('thermal-engine','atfwd')
G.edge['thermal-engine']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['atfwd']['fill'] = 'red'
G.add_edge('thermal-engine','atfwd')
G.edge['thermal-engine']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['atfwd']['fill'] = 'red'
G.add_edge('thermal-engine','bluetooth')
G.edge['thermal-engine']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['thermal-engine']['bluetooth']['fill'] = 'red'
G.add_edge('thermal-engine','bluetooth')
G.edge['thermal-engine']['bluetooth']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['bluetooth']['fill'] = 'red'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['cnd']['fill'] = 'red'
G.add_edge('thermal-engine','cnd')
G.edge['thermal-engine']['cnd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['cnd']['fill'] = 'red'
G.add_edge('thermal-engine','DMM-daemon')
G.edge['thermal-engine']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['DMM-daemon']['fill'] = 'red'
G.add_edge('thermal-engine','DMM-daemon')
G.edge['thermal-engine']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['DMM-daemon']['fill'] = 'red'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['dpmd']['fill'] = 'red'
G.add_edge('thermal-engine','dpmd')
G.edge['thermal-engine']['dpmd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['dpmd']['fill'] = 'red'
G.add_edge('thermal-engine','ims')
G.edge['thermal-engine']['ims']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['ims']['fill'] = 'red'
G.add_edge('thermal-engine','ims')
G.edge['thermal-engine']['ims']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['ims']['fill'] = 'red'
G.add_edge('thermal-engine','location_app')
G.edge['thermal-engine']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['location_app']['fill'] = 'red'
G.add_edge('thermal-engine','location_app')
G.edge['thermal-engine']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['location_app']['fill'] = 'red'
G.add_edge('thermal-engine','location')
G.edge['thermal-engine']['location']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['location']['fill'] = 'red'
G.add_edge('thermal-engine','location')
G.edge['thermal-engine']['location']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['location']['fill'] = 'red'
G.add_edge('thermal-engine','mediaserver')
G.edge['thermal-engine']['mediaserver']['write-read'] = '[open open][write read][append read][write read][setattr getattr][write read]'
G.edge['thermal-engine']['mediaserver']['fill'] = 'red'
G.add_edge('thermal-engine','mediaserver')
G.edge['thermal-engine']['mediaserver']['write-read'] = '[open open][write read][append read][write read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['mediaserver']['fill'] = 'red'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['netmgrd']['fill'] = 'red'
G.add_edge('thermal-engine','netmgrd')
G.edge['thermal-engine']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['netmgrd']['fill'] = 'red'
G.add_edge('thermal-engine','qmuxd')
G.edge['thermal-engine']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['qmuxd']['fill'] = 'red'
G.add_edge('thermal-engine','qmuxd')
G.edge['thermal-engine']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['qmuxd']['fill'] = 'red'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['qti']['fill'] = 'red'
G.add_edge('thermal-engine','qti')
G.edge['thermal-engine']['qti']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['qti']['fill'] = 'red'
G.add_edge('thermal-engine','radio')
G.edge['thermal-engine']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read]'
G.edge['thermal-engine']['radio']['fill'] = 'red'
G.add_edge('thermal-engine','radio')
G.edge['thermal-engine']['radio']['write-read'] = '[open open][write read][append read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['radio']['fill'] = 'red'
G.add_edge('thermal-engine','rild')
G.edge['thermal-engine']['rild']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['thermal-engine']['rild']['fill'] = 'red'
G.add_edge('thermal-engine','rild')
G.edge['thermal-engine']['rild']['write-read'] = '[write read][append read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['rild']['fill'] = 'red'
G.add_edge('thermal-engine','system_server')
G.edge['thermal-engine']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read]'
G.edge['thermal-engine']['system_server']['fill'] = 'red'
G.add_edge('thermal-engine','system_server')
G.edge['thermal-engine']['system_server']['write-read'] = '[write read][append read][open open][write read][append read][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['system_server']['fill'] = 'red'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read]'
G.edge['thermal-engine']['thermal-engine']['fill'] = 'red'
G.add_edge('thermal-engine','thermal-engine')
G.edge['thermal-engine']['thermal-engine']['write-read'] = '[write read][open open][write read][append read][open open][write read][append read][open open][write read][open open][write read][append read][open open][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][write read]'
G.edge['thermal-engine']['thermal-engine']['fill'] = 'red'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['wcnss_service']['fill'] = 'red'
G.add_edge('thermal-engine','wcnss_service')
G.edge['thermal-engine']['wcnss_service']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['wcnss_service']['fill'] = 'red'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr][write read]'
G.edge['thermal-engine']['wpa']['fill'] = 'red'
G.add_edge('thermal-engine','wpa')
G.edge['thermal-engine']['wpa']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['thermal-engine']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','atfwd')
G.edge['wcnss_service']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','bluetooth')
G.edge['wcnss_service']['bluetooth']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','DMM-daemon')
G.edge['wcnss_service']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','ims')
G.edge['wcnss_service']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','location_app')
G.edge['wcnss_service']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','location')
G.edge['wcnss_service']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','mediaserver')
G.edge['wcnss_service']['mediaserver']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','qmuxd')
G.edge['wcnss_service']['qmuxd']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('wcnss_service','radio')
G.edge['wcnss_service']['radio']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','rild')
G.edge['wcnss_service']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wcnss_service','atfwd')
G.edge['wcnss_service']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['atfwd']['fill'] = 'red'
G.add_edge('wcnss_service','atfwd')
G.edge['wcnss_service']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['atfwd']['fill'] = 'red'
G.add_edge('wcnss_service','bluetooth')
G.edge['wcnss_service']['bluetooth']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['bluetooth']['fill'] = 'red'
G.add_edge('wcnss_service','bluetooth')
G.edge['wcnss_service']['bluetooth']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['bluetooth']['fill'] = 'red'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['cnd']['fill'] = 'red'
G.add_edge('wcnss_service','cnd')
G.edge['wcnss_service']['cnd']['write-read'] = '[write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['cnd']['fill'] = 'red'
G.add_edge('wcnss_service','DMM-daemon')
G.edge['wcnss_service']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['DMM-daemon']['fill'] = 'red'
G.add_edge('wcnss_service','DMM-daemon')
G.edge['wcnss_service']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['DMM-daemon']['fill'] = 'red'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['dpmd']['fill'] = 'red'
G.add_edge('wcnss_service','dpmd')
G.edge['wcnss_service']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['dpmd']['fill'] = 'red'
G.add_edge('wcnss_service','ims')
G.edge['wcnss_service']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['ims']['fill'] = 'red'
G.add_edge('wcnss_service','ims')
G.edge['wcnss_service']['ims']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['ims']['fill'] = 'red'
G.add_edge('wcnss_service','location_app')
G.edge['wcnss_service']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['location_app']['fill'] = 'red'
G.add_edge('wcnss_service','location_app')
G.edge['wcnss_service']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['location_app']['fill'] = 'red'
G.add_edge('wcnss_service','location')
G.edge['wcnss_service']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['location']['fill'] = 'red'
G.add_edge('wcnss_service','location')
G.edge['wcnss_service']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['location']['fill'] = 'red'
G.add_edge('wcnss_service','mediaserver')
G.edge['wcnss_service']['mediaserver']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['mediaserver']['fill'] = 'red'
G.add_edge('wcnss_service','mediaserver')
G.edge['wcnss_service']['mediaserver']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['mediaserver']['fill'] = 'red'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['netmgrd']['fill'] = 'red'
G.add_edge('wcnss_service','netmgrd')
G.edge['wcnss_service']['netmgrd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['netmgrd']['fill'] = 'red'
G.add_edge('wcnss_service','qmuxd')
G.edge['wcnss_service']['qmuxd']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['qmuxd']['fill'] = 'red'
G.add_edge('wcnss_service','qmuxd')
G.edge['wcnss_service']['qmuxd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['qmuxd']['fill'] = 'red'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['wcnss_service']['qti']['fill'] = 'red'
G.add_edge('wcnss_service','qti')
G.edge['wcnss_service']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['wcnss_service']['qti']['fill'] = 'red'
G.add_edge('wcnss_service','radio')
G.edge['wcnss_service']['radio']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['radio']['fill'] = 'red'
G.add_edge('wcnss_service','radio')
G.edge['wcnss_service']['radio']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['radio']['fill'] = 'red'
G.add_edge('wcnss_service','rild')
G.edge['wcnss_service']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['rild']['fill'] = 'red'
G.add_edge('wcnss_service','rild')
G.edge['wcnss_service']['rild']['write-read'] = '[setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['rild']['fill'] = 'red'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['system_server']['fill'] = 'red'
G.add_edge('wcnss_service','system_server')
G.edge['wcnss_service']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['system_server']['fill'] = 'red'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['wcnss_service']['thermal-engine']['fill'] = 'red'
G.add_edge('wcnss_service','thermal-engine')
G.edge['wcnss_service']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wcnss_service']['thermal-engine']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wcnss_service')
G.edge['wcnss_service']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][write read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][open open][add_name search][remove_name search][add_name search][remove_name search][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['wcnss_service']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wcnss_service','wpa')
G.edge['wcnss_service']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wcnss_service']['wpa']['fill'] = 'red'
G.add_edge('wpa','atfwd')
G.edge['wpa']['atfwd']['write-read'] = '[setattr getattr]'
G.add_edge('wpa','bluetooth')
G.edge['wpa']['bluetooth']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr]'
G.add_edge('wpa','DMM-daemon')
G.edge['wpa']['DMM-daemon']['write-read'] = '[setattr getattr]'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','ims')
G.edge['wpa']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','location_app')
G.edge['wpa']['location_app']['write-read'] = '[setattr getattr]'
G.add_edge('wpa','location')
G.edge['wpa']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','mediaserver')
G.edge['wpa']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr]'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr]'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr]'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr]'
G.add_edge('wpa','radio')
G.edge['wpa']['radio']['write-read'] = '[setattr getattr][setattr getattr]'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr]'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr]'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr]'
G.add_edge('wpa','atfwd')
G.edge['wpa']['atfwd']['write-read'] = '[setattr getattr][write read]'
G.edge['wpa']['atfwd']['fill'] = 'red'
G.add_edge('wpa','atfwd')
G.edge['wpa']['atfwd']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wpa']['atfwd']['fill'] = 'red'
G.add_edge('wpa','bluetooth')
G.edge['wpa']['bluetooth']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['wpa']['bluetooth']['fill'] = 'red'
G.add_edge('wpa','bluetooth')
G.edge['wpa']['bluetooth']['write-read'] = '[setattr getattr][setattr getattr][write read][write read]'
G.edge['wpa']['bluetooth']['fill'] = 'red'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['cnd']['fill'] = 'red'
G.add_edge('wpa','cnd')
G.edge['wpa']['cnd']['write-read'] = '[open open][write read][add_name search][remove_name search][write read][add_name search][remove_name search][write read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['cnd']['fill'] = 'red'
G.add_edge('wpa','DMM-daemon')
G.edge['wpa']['DMM-daemon']['write-read'] = '[setattr getattr][write read]'
G.edge['wpa']['DMM-daemon']['fill'] = 'red'
G.add_edge('wpa','DMM-daemon')
G.edge['wpa']['DMM-daemon']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wpa']['DMM-daemon']['fill'] = 'red'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['dpmd']['fill'] = 'red'
G.add_edge('wpa','dpmd')
G.edge['wpa']['dpmd']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['dpmd']['fill'] = 'red'
G.add_edge('wpa','ims')
G.edge['wpa']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['ims']['fill'] = 'red'
G.add_edge('wpa','ims')
G.edge['wpa']['ims']['write-read'] = '[open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['ims']['fill'] = 'red'
G.add_edge('wpa','location_app')
G.edge['wpa']['location_app']['write-read'] = '[setattr getattr][write read]'
G.edge['wpa']['location_app']['fill'] = 'red'
G.add_edge('wpa','location_app')
G.edge['wpa']['location_app']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wpa']['location_app']['fill'] = 'red'
G.add_edge('wpa','location')
G.edge['wpa']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['location']['fill'] = 'red'
G.add_edge('wpa','location')
G.edge['wpa']['location']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['location']['fill'] = 'red'
G.add_edge('wpa','mediaserver')
G.edge['wpa']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read]'
G.edge['wpa']['mediaserver']['fill'] = 'red'
G.add_edge('wpa','mediaserver')
G.edge['wpa']['mediaserver']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][setattr getattr][write read][write read]'
G.edge['wpa']['mediaserver']['fill'] = 'red'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read]'
G.edge['wpa']['netmgrd']['fill'] = 'red'
G.add_edge('wpa','netmgrd')
G.edge['wpa']['netmgrd']['write-read'] = '[open open][open open][write read][write read][add_name search][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['wpa']['netmgrd']['fill'] = 'red'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read]'
G.edge['wpa']['qmuxd']['fill'] = 'red'
G.add_edge('wpa','qmuxd')
G.edge['wpa']['qmuxd']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][write read]'
G.edge['wpa']['qmuxd']['fill'] = 'red'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr][write read]'
G.edge['wpa']['qti']['fill'] = 'red'
G.add_edge('wpa','qti')
G.edge['wpa']['qti']['write-read'] = '[write read][setattr getattr][write read][write read]'
G.edge['wpa']['qti']['fill'] = 'red'
G.add_edge('wpa','radio')
G.edge['wpa']['radio']['write-read'] = '[setattr getattr][setattr getattr][write read]'
G.edge['wpa']['radio']['fill'] = 'red'
G.add_edge('wpa','radio')
G.edge['wpa']['radio']['write-read'] = '[setattr getattr][setattr getattr][write read][write read]'
G.edge['wpa']['radio']['fill'] = 'red'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['rild']['fill'] = 'red'
G.add_edge('wpa','rild')
G.edge['wpa']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][open open][setattr getattr][write read][write read][add_name search][remove_name search][add_name search][remove_name search][open open][setattr getattr][write read][append read][setattr getattr][setattr getattr][write read][append read][write read][append read][setopt getopt][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['rild']['fill'] = 'red'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['system_server']['fill'] = 'red'
G.add_edge('wpa','system_server')
G.edge['wpa']['system_server']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['system_server']['fill'] = 'red'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr][write read]'
G.edge['wpa']['thermal-engine']['fill'] = 'red'
G.add_edge('wpa','thermal-engine')
G.edge['wpa']['thermal-engine']['write-read'] = '[setattr getattr][write read][write read]'
G.edge['wpa']['thermal-engine']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wcnss_service')
G.edge['wpa']['wcnss_service']['write-read'] = '[open open][open open][setattr getattr][setattr getattr][write read][append read][write read][append read][open open][open open][write read][write read][add_name search][remove_name search][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['wcnss_service']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
G.add_edge('wpa','wpa')
G.edge['wpa']['wpa']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][write read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][setattr getattr][write read][write read]'
G.edge['wpa']['wpa']['fill'] = 'red'
app = Viewer(G)
app.mainloop()