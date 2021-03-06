import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open]'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('apaservice','kernel')
G.edge['apaservice']['kernel']['write-read'] = '[open open]'
G.add_edge('apaservice','mm-qcamera-daemon')
G.edge['apaservice']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('apaservice','mobexdaemon')
G.edge['apaservice']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('apaservice','rild')
G.edge['apaservice']['rild']['write-read'] = '[open open]'
G.add_edge('apaservice','untrusteddomain')
G.edge['apaservice']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('apaservice','vmware_app')
G.edge['apaservice']['vmware_app']['write-read'] = '[open open]'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','mm-qcamera-daemon')
G.edge['apaservice']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','mobexdaemon')
G.edge['apaservice']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','rild')
G.edge['apaservice']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','untrusteddomain')
G.edge['apaservice']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','vmware_app')
G.edge['apaservice']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read]'
G.edge['apaservice']['apaservice']['fill'] = 'red'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['bluetooth']['fill'] = 'red'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['fixmo_app']['fill'] = 'red'
G.add_edge('apaservice','kernel')
G.edge['apaservice']['kernel']['write-read'] = '[open open][write read]'
G.edge['apaservice']['kernel']['fill'] = 'red'
G.add_edge('apaservice','mm-qcamera-daemon')
G.edge['apaservice']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('apaservice','mobexdaemon')
G.edge['apaservice']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['mobexdaemon']['fill'] = 'red'
G.add_edge('apaservice','rild')
G.edge['apaservice']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['rild']['fill'] = 'red'
G.add_edge('apaservice','untrusteddomain')
G.edge['apaservice']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['untrusteddomain']['fill'] = 'red'
G.add_edge('apaservice','vmware_app')
G.edge['apaservice']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['apaservice']['vmware_app']['fill'] = 'red'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search]'
G.add_edge('apaservice','apaservice')
G.edge['apaservice']['apaservice']['write-read'] = '[open open][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','bluetooth')
G.edge['apaservice']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','fixmo_app')
G.edge['apaservice']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','kernel')
G.edge['apaservice']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('apaservice','kernel')
G.edge['apaservice']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('apaservice','mm-qcamera-daemon')
G.edge['apaservice']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','mm-qcamera-daemon')
G.edge['apaservice']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','mobexdaemon')
G.edge['apaservice']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','mobexdaemon')
G.edge['apaservice']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','rild')
G.edge['apaservice']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','rild')
G.edge['apaservice']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','untrusteddomain')
G.edge['apaservice']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','untrusteddomain')
G.edge['apaservice']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('apaservice','vmware_app')
G.edge['apaservice']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('apaservice','vmware_app')
G.edge['apaservice']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','apaservice')
G.edge['bluetooth']['apaservice']['write-read'] = '[open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open]'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','kernel')
G.edge['bluetooth']['kernel']['write-read'] = '[open open]'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('bluetooth','mobexdaemon')
G.edge['bluetooth']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('bluetooth','vmware_app')
G.edge['bluetooth']['vmware_app']['write-read'] = '[open open]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr]'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','mobexdaemon')
G.edge['bluetooth']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','vmware_app')
G.edge['bluetooth']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('bluetooth','apaservice')
G.edge['bluetooth']['apaservice']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['apaservice']['fill'] = 'red'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read]'
G.edge['bluetooth']['bluetooth']['fill'] = 'red'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['fixmo_app']['fill'] = 'red'
G.add_edge('bluetooth','kernel')
G.edge['bluetooth']['kernel']['write-read'] = '[open open][write read]'
G.edge['bluetooth']['kernel']['fill'] = 'red'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('bluetooth','mobexdaemon')
G.edge['bluetooth']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['mobexdaemon']['fill'] = 'red'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['rild']['fill'] = 'red'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['untrusteddomain']['fill'] = 'red'
G.add_edge('bluetooth','vmware_app')
G.edge['bluetooth']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['bluetooth']['vmware_app']['fill'] = 'red'
G.add_edge('bluetooth','apaservice')
G.edge['bluetooth']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('bluetooth','apaservice')
G.edge['bluetooth']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','bluetooth')
G.edge['bluetooth']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read][append read][open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','fixmo_app')
G.edge['bluetooth']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','kernel')
G.edge['bluetooth']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('bluetooth','kernel')
G.edge['bluetooth']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','mm-qcamera-daemon')
G.edge['bluetooth']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','mobexdaemon')
G.edge['bluetooth']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','mobexdaemon')
G.edge['bluetooth']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','rild')
G.edge['bluetooth']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','untrusteddomain')
G.edge['bluetooth']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('bluetooth','vmware_app')
G.edge['bluetooth']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('bluetooth','vmware_app')
G.edge['bluetooth']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','apaservice')
G.edge['debuggerd']['apaservice']['write-read'] = '[open open]'
G.add_edge('debuggerd','bluetooth')
G.edge['debuggerd']['bluetooth']['write-read'] = '[open open]'
G.add_edge('debuggerd','fixmo_app')
G.edge['debuggerd']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open]'
G.add_edge('debuggerd','mm-qcamera-daemon')
G.edge['debuggerd']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('debuggerd','vmware_app')
G.edge['debuggerd']['vmware_app']['write-read'] = '[open open]'
G.add_edge('debuggerd','bluetooth')
G.edge['debuggerd']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','fixmo_app')
G.edge['debuggerd']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','mm-qcamera-daemon')
G.edge['debuggerd']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','vmware_app')
G.edge['debuggerd']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('debuggerd','apaservice')
G.edge['debuggerd']['apaservice']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['apaservice']['fill'] = 'red'
G.add_edge('debuggerd','bluetooth')
G.edge['debuggerd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['bluetooth']['fill'] = 'red'
G.add_edge('debuggerd','fixmo_app')
G.edge['debuggerd']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['fixmo_app']['fill'] = 'red'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read]'
G.edge['debuggerd']['kernel']['fill'] = 'red'
G.add_edge('debuggerd','mm-qcamera-daemon')
G.edge['debuggerd']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['mobexdaemon']['fill'] = 'red'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read]'
G.edge['debuggerd']['rild']['fill'] = 'red'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['untrusteddomain']['fill'] = 'red'
G.add_edge('debuggerd','vmware_app')
G.edge['debuggerd']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['debuggerd']['vmware_app']['fill'] = 'red'
G.add_edge('debuggerd','apaservice')
G.edge['debuggerd']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('debuggerd','apaservice')
G.edge['debuggerd']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','bluetooth')
G.edge['debuggerd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','bluetooth')
G.edge['debuggerd']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','fixmo_app')
G.edge['debuggerd']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','fixmo_app')
G.edge['debuggerd']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('debuggerd','kernel')
G.edge['debuggerd']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','mm-qcamera-daemon')
G.edge['debuggerd']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','mm-qcamera-daemon')
G.edge['debuggerd']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','mobexdaemon')
G.edge['debuggerd']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','rild')
G.edge['debuggerd']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','untrusteddomain')
G.edge['debuggerd']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('debuggerd','vmware_app')
G.edge['debuggerd']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('debuggerd','vmware_app')
G.edge['debuggerd']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','apaservice')
G.edge['fixmo_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('fixmo_app','kernel')
G.edge['fixmo_app']['kernel']['write-read'] = '[open open]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('fixmo_app','mobexdaemon')
G.edge['fixmo_app']['mobexdaemon']['write-read'] = '[write read][open open]'
G.add_edge('fixmo_app','rild')
G.edge['fixmo_app']['rild']['write-read'] = '[open open]'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('fixmo_app','mobexdaemon')
G.edge['fixmo_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('fixmo_app','rild')
G.edge['fixmo_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('fixmo_app','apaservice')
G.edge['fixmo_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['apaservice']['fill'] = 'red'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read]'
G.edge['fixmo_app']['bluetooth']['fill'] = 'red'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['fixmo_app']['fixmo_app']['fill'] = 'red'
G.add_edge('fixmo_app','kernel')
G.edge['fixmo_app']['kernel']['write-read'] = '[open open][write read]'
G.edge['fixmo_app']['kernel']['fill'] = 'red'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['fixmo_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('fixmo_app','mobexdaemon')
G.edge['fixmo_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['fixmo_app']['mobexdaemon']['fill'] = 'red'
G.add_edge('fixmo_app','rild')
G.edge['fixmo_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['rild']['fill'] = 'red'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['fixmo_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['fixmo_app']['vmware_app']['fill'] = 'red'
G.add_edge('fixmo_app','apaservice')
G.edge['fixmo_app']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('fixmo_app','apaservice')
G.edge['fixmo_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','bluetooth')
G.edge['fixmo_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','fixmo_app')
G.edge['fixmo_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','kernel')
G.edge['fixmo_app']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('fixmo_app','kernel')
G.edge['fixmo_app']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','mm-qcamera-daemon')
G.edge['fixmo_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','mobexdaemon')
G.edge['fixmo_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','mobexdaemon')
G.edge['fixmo_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','rild')
G.edge['fixmo_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','rild')
G.edge['fixmo_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','untrusteddomain')
G.edge['fixmo_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('fixmo_app','vmware_app')
G.edge['fixmo_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('good_app','kernel')
G.edge['good_app']['kernel']['write-read'] = '[open open]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('good_app','mobexdaemon')
G.edge['good_app']['mobexdaemon']['write-read'] = '[write read][open open]'
G.add_edge('good_app','rild')
G.edge['good_app']['rild']['write-read'] = '[open open]'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('good_app','mobexdaemon')
G.edge['good_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('good_app','rild')
G.edge['good_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['good_app']['apaservice']['fill'] = 'red'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read]'
G.edge['good_app']['bluetooth']['fill'] = 'red'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['good_app']['fixmo_app']['fill'] = 'red'
G.add_edge('good_app','kernel')
G.edge['good_app']['kernel']['write-read'] = '[open open][write read]'
G.edge['good_app']['kernel']['fill'] = 'red'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['good_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('good_app','mobexdaemon')
G.edge['good_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['good_app']['mobexdaemon']['fill'] = 'red'
G.add_edge('good_app','rild')
G.edge['good_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['rild']['fill'] = 'red'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['good_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['good_app']['vmware_app']['fill'] = 'red'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('good_app','apaservice')
G.edge['good_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','bluetooth')
G.edge['good_app']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','fixmo_app')
G.edge['good_app']['fixmo_app']['write-read'] = '[write read][setopt getopt][write read][setopt getopt][open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','kernel')
G.edge['good_app']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('good_app','kernel')
G.edge['good_app']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','mm-qcamera-daemon')
G.edge['good_app']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','mobexdaemon')
G.edge['good_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','mobexdaemon')
G.edge['good_app']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','rild')
G.edge['good_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','rild')
G.edge['good_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','untrusteddomain')
G.edge['good_app']['untrusteddomain']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('good_app','vmware_app')
G.edge['good_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','apaservice')
G.edge['kernel']['apaservice']['write-read'] = '[open open]'
G.add_edge('kernel','bluetooth')
G.edge['kernel']['bluetooth']['write-read'] = '[open open]'
G.add_edge('kernel','fixmo_app')
G.edge['kernel']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('kernel','mm-qcamera-daemon')
G.edge['kernel']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('kernel','rild')
G.edge['kernel']['rild']['write-read'] = '[open open]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('kernel','vmware_app')
G.edge['kernel']['vmware_app']['write-read'] = '[open open]'
G.add_edge('kernel','bluetooth')
G.edge['kernel']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','fixmo_app')
G.edge['kernel']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','mm-qcamera-daemon')
G.edge['kernel']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','rild')
G.edge['kernel']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','vmware_app')
G.edge['kernel']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kernel','apaservice')
G.edge['kernel']['apaservice']['write-read'] = '[open open][write read]'
G.edge['kernel']['apaservice']['fill'] = 'red'
G.add_edge('kernel','bluetooth')
G.edge['kernel']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['bluetooth']['fill'] = 'red'
G.add_edge('kernel','fixmo_app')
G.edge['kernel']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['fixmo_app']['fill'] = 'red'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read]'
G.edge['kernel']['kernel']['fill'] = 'red'
G.add_edge('kernel','mm-qcamera-daemon')
G.edge['kernel']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['mobexdaemon']['fill'] = 'red'
G.add_edge('kernel','rild')
G.edge['kernel']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['rild']['fill'] = 'red'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['untrusteddomain']['fill'] = 'red'
G.add_edge('kernel','vmware_app')
G.edge['kernel']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kernel']['vmware_app']['fill'] = 'red'
G.add_edge('kernel','apaservice')
G.edge['kernel']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kernel','apaservice')
G.edge['kernel']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kernel','bluetooth')
G.edge['kernel']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','bluetooth')
G.edge['kernel']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','fixmo_app')
G.edge['kernel']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','fixmo_app')
G.edge['kernel']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search]'
G.add_edge('kernel','kernel')
G.edge['kernel']['kernel']['write-read'] = '[open open][setattr getattr][write read][append read][open open][write read][add_name search][remove_name search]'
G.add_edge('kernel','mm-qcamera-daemon')
G.edge['kernel']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','mm-qcamera-daemon')
G.edge['kernel']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','mobexdaemon')
G.edge['kernel']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','rild')
G.edge['kernel']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','rild')
G.edge['kernel']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','untrusteddomain')
G.edge['kernel']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kernel','vmware_app')
G.edge['kernel']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kernel','vmware_app')
G.edge['kernel']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','apaservice')
G.edge['kiesexe']['apaservice']['write-read'] = '[open open]'
G.add_edge('kiesexe','bluetooth')
G.edge['kiesexe']['bluetooth']['write-read'] = '[open open]'
G.add_edge('kiesexe','fixmo_app')
G.edge['kiesexe']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('kiesexe','kernel')
G.edge['kiesexe']['kernel']['write-read'] = '[open open]'
G.add_edge('kiesexe','mm-qcamera-daemon')
G.edge['kiesexe']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('kiesexe','mobexdaemon')
G.edge['kiesexe']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open]'
G.add_edge('kiesexe','untrusteddomain')
G.edge['kiesexe']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('kiesexe','vmware_app')
G.edge['kiesexe']['vmware_app']['write-read'] = '[open open]'
G.add_edge('kiesexe','bluetooth')
G.edge['kiesexe']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','fixmo_app')
G.edge['kiesexe']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','mm-qcamera-daemon')
G.edge['kiesexe']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','mobexdaemon')
G.edge['kiesexe']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','untrusteddomain')
G.edge['kiesexe']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','vmware_app')
G.edge['kiesexe']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('kiesexe','apaservice')
G.edge['kiesexe']['apaservice']['write-read'] = '[open open][write read]'
G.edge['kiesexe']['apaservice']['fill'] = 'red'
G.add_edge('kiesexe','bluetooth')
G.edge['kiesexe']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['bluetooth']['fill'] = 'red'
G.add_edge('kiesexe','fixmo_app')
G.edge['kiesexe']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['fixmo_app']['fill'] = 'red'
G.add_edge('kiesexe','kernel')
G.edge['kiesexe']['kernel']['write-read'] = '[open open][write read]'
G.edge['kiesexe']['kernel']['fill'] = 'red'
G.add_edge('kiesexe','mm-qcamera-daemon')
G.edge['kiesexe']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('kiesexe','mobexdaemon')
G.edge['kiesexe']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['mobexdaemon']['fill'] = 'red'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['rild']['fill'] = 'red'
G.add_edge('kiesexe','untrusteddomain')
G.edge['kiesexe']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['untrusteddomain']['fill'] = 'red'
G.add_edge('kiesexe','vmware_app')
G.edge['kiesexe']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['kiesexe']['vmware_app']['fill'] = 'red'
G.add_edge('kiesexe','apaservice')
G.edge['kiesexe']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kiesexe','apaservice')
G.edge['kiesexe']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','bluetooth')
G.edge['kiesexe']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','bluetooth')
G.edge['kiesexe']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','fixmo_app')
G.edge['kiesexe']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','fixmo_app')
G.edge['kiesexe']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','kernel')
G.edge['kiesexe']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('kiesexe','kernel')
G.edge['kiesexe']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','mm-qcamera-daemon')
G.edge['kiesexe']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','mm-qcamera-daemon')
G.edge['kiesexe']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','mobexdaemon')
G.edge['kiesexe']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','mobexdaemon')
G.edge['kiesexe']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','rild')
G.edge['kiesexe']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','untrusteddomain')
G.edge['kiesexe']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','untrusteddomain')
G.edge['kiesexe']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('kiesexe','vmware_app')
G.edge['kiesexe']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('kiesexe','vmware_app')
G.edge['kiesexe']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','apaservice')
G.edge['mm-qcamera-daemon']['apaservice']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','kernel')
G.edge['mm-qcamera-daemon']['kernel']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open]'
G.add_edge('mm-qcamera-daemon','mobexdaemon')
G.edge['mm-qcamera-daemon']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','untrusteddomain')
G.edge['mm-qcamera-daemon']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','vmware_app')
G.edge['mm-qcamera-daemon']['vmware_app']['write-read'] = '[open open]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','mobexdaemon')
G.edge['mm-qcamera-daemon']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','untrusteddomain')
G.edge['mm-qcamera-daemon']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','vmware_app')
G.edge['mm-qcamera-daemon']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mm-qcamera-daemon','apaservice')
G.edge['mm-qcamera-daemon']['apaservice']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['apaservice']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['bluetooth']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['fixmo_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','kernel')
G.edge['mm-qcamera-daemon']['kernel']['write-read'] = '[open open][write read]'
G.edge['mm-qcamera-daemon']['kernel']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','mobexdaemon')
G.edge['mm-qcamera-daemon']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['mobexdaemon']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['rild']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','untrusteddomain')
G.edge['mm-qcamera-daemon']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['untrusteddomain']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','vmware_app')
G.edge['mm-qcamera-daemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mm-qcamera-daemon']['vmware_app']['fill'] = 'red'
G.add_edge('mm-qcamera-daemon','apaservice')
G.edge['mm-qcamera-daemon']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','apaservice')
G.edge['mm-qcamera-daemon']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','bluetooth')
G.edge['mm-qcamera-daemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','fixmo_app')
G.edge['mm-qcamera-daemon']['fixmo_app']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','kernel')
G.edge['mm-qcamera-daemon']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','kernel')
G.edge['mm-qcamera-daemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','mm-qcamera-daemon')
G.edge['mm-qcamera-daemon']['mm-qcamera-daemon']['write-read'] = '[open open][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','mobexdaemon')
G.edge['mm-qcamera-daemon']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','mobexdaemon')
G.edge['mm-qcamera-daemon']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','rild')
G.edge['mm-qcamera-daemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','untrusteddomain')
G.edge['mm-qcamera-daemon']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','untrusteddomain')
G.edge['mm-qcamera-daemon']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mm-qcamera-daemon','vmware_app')
G.edge['mm-qcamera-daemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mm-qcamera-daemon','vmware_app')
G.edge['mm-qcamera-daemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','apaservice')
G.edge['mobexdaemon']['apaservice']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','bluetooth')
G.edge['mobexdaemon']['bluetooth']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','fixmo_app')
G.edge['mobexdaemon']['fixmo_app']['write-read'] = '[write read][append read][open open]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','mm-qcamera-daemon')
G.edge['mobexdaemon']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open]'
G.add_edge('mobexdaemon','rild')
G.edge['mobexdaemon']['rild']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open]'
G.add_edge('mobexdaemon','vmware_app')
G.edge['mobexdaemon']['vmware_app']['write-read'] = '[open open]'
G.add_edge('mobexdaemon','bluetooth')
G.edge['mobexdaemon']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mobexdaemon','fixmo_app')
G.edge['mobexdaemon']['fixmo_app']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','mm-qcamera-daemon')
G.edge['mobexdaemon']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('mobexdaemon','rild')
G.edge['mobexdaemon']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr]'
G.add_edge('mobexdaemon','vmware_app')
G.edge['mobexdaemon']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('mobexdaemon','apaservice')
G.edge['mobexdaemon']['apaservice']['write-read'] = '[open open][write read]'
G.edge['mobexdaemon']['apaservice']['fill'] = 'red'
G.add_edge('mobexdaemon','bluetooth')
G.edge['mobexdaemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mobexdaemon']['bluetooth']['fill'] = 'red'
G.add_edge('mobexdaemon','fixmo_app')
G.edge['mobexdaemon']['fixmo_app']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['fixmo_app']['fill'] = 'red'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read]'
G.edge['mobexdaemon']['kernel']['fill'] = 'red'
G.add_edge('mobexdaemon','mm-qcamera-daemon')
G.edge['mobexdaemon']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mobexdaemon']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['mobexdaemon']['fill'] = 'red'
G.add_edge('mobexdaemon','rild')
G.edge['mobexdaemon']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mobexdaemon']['rild']['fill'] = 'red'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read]'
G.edge['mobexdaemon']['untrusteddomain']['fill'] = 'red'
G.add_edge('mobexdaemon','vmware_app')
G.edge['mobexdaemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['mobexdaemon']['vmware_app']['fill'] = 'red'
G.add_edge('mobexdaemon','apaservice')
G.edge['mobexdaemon']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mobexdaemon','apaservice')
G.edge['mobexdaemon']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','bluetooth')
G.edge['mobexdaemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','bluetooth')
G.edge['mobexdaemon']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','fixmo_app')
G.edge['mobexdaemon']['fixmo_app']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','fixmo_app')
G.edge['mobexdaemon']['fixmo_app']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('mobexdaemon','kernel')
G.edge['mobexdaemon']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','mm-qcamera-daemon')
G.edge['mobexdaemon']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','mm-qcamera-daemon')
G.edge['mobexdaemon']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','mobexdaemon')
G.edge['mobexdaemon']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','rild')
G.edge['mobexdaemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','rild')
G.edge['mobexdaemon']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','untrusteddomain')
G.edge['mobexdaemon']['untrusteddomain']['write-read'] = '[write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('mobexdaemon','vmware_app')
G.edge['mobexdaemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('mobexdaemon','vmware_app')
G.edge['mobexdaemon']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','apaservice')
G.edge['rild']['apaservice']['write-read'] = '[open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open]'
G.add_edge('rild','fixmo_app')
G.edge['rild']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('rild','kernel')
G.edge['rild']['kernel']['write-read'] = '[open open]'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('rild','mobexdaemon')
G.edge['rild']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('rild','vmware_app')
G.edge['rild']['vmware_app']['write-read'] = '[open open]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','fixmo_app')
G.edge['rild']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','mobexdaemon')
G.edge['rild']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','vmware_app')
G.edge['rild']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('rild','apaservice')
G.edge['rild']['apaservice']['write-read'] = '[open open][write read]'
G.edge['rild']['apaservice']['fill'] = 'red'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['bluetooth']['fill'] = 'red'
G.add_edge('rild','fixmo_app')
G.edge['rild']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['fixmo_app']['fill'] = 'red'
G.add_edge('rild','kernel')
G.edge['rild']['kernel']['write-read'] = '[open open][write read]'
G.edge['rild']['kernel']['fill'] = 'red'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('rild','mobexdaemon')
G.edge['rild']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['mobexdaemon']['fill'] = 'red'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['rild']['rild']['fill'] = 'red'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['untrusteddomain']['fill'] = 'red'
G.add_edge('rild','vmware_app')
G.edge['rild']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['rild']['vmware_app']['fill'] = 'red'
G.add_edge('rild','apaservice')
G.edge['rild']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','apaservice')
G.edge['rild']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','bluetooth')
G.edge['rild']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','fixmo_app')
G.edge['rild']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','fixmo_app')
G.edge['rild']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','kernel')
G.edge['rild']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('rild','kernel')
G.edge['rild']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','mm-qcamera-daemon')
G.edge['rild']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','mobexdaemon')
G.edge['rild']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','mobexdaemon')
G.edge['rild']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','rild')
G.edge['rild']['rild']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][setattr getattr][write read][append read][setopt getopt][write read][append read][open open][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','untrusteddomain')
G.edge['rild']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('rild','vmware_app')
G.edge['rild']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('rild','vmware_app')
G.edge['rild']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','apaservice')
G.edge['untrusteddomain']['apaservice']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open]'
G.add_edge('untrusteddomain','fixmo_app')
G.edge['untrusteddomain']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mm-qcamera-daemon')
G.edge['untrusteddomain']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open]'
G.add_edge('untrusteddomain','vmware_app')
G.edge['untrusteddomain']['vmware_app']['write-read'] = '[open open]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr]'
G.add_edge('untrusteddomain','fixmo_app')
G.edge['untrusteddomain']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('untrusteddomain','mm-qcamera-daemon')
G.edge['untrusteddomain']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr]'
G.add_edge('untrusteddomain','vmware_app')
G.edge['untrusteddomain']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('untrusteddomain','apaservice')
G.edge['untrusteddomain']['apaservice']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['apaservice']['fill'] = 'red'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['bluetooth']['fill'] = 'red'
G.add_edge('untrusteddomain','fixmo_app')
G.edge['untrusteddomain']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['fixmo_app']['fill'] = 'red'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read]'
G.edge['untrusteddomain']['kernel']['fill'] = 'red'
G.add_edge('untrusteddomain','mm-qcamera-daemon')
G.edge['untrusteddomain']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['mobexdaemon']['fill'] = 'red'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['rild']['fill'] = 'red'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read]'
G.edge['untrusteddomain']['untrusteddomain']['fill'] = 'red'
G.add_edge('untrusteddomain','vmware_app')
G.edge['untrusteddomain']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['untrusteddomain']['vmware_app']['fill'] = 'red'
G.add_edge('untrusteddomain','apaservice')
G.edge['untrusteddomain']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('untrusteddomain','apaservice')
G.edge['untrusteddomain']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','bluetooth')
G.edge['untrusteddomain']['bluetooth']['write-read'] = '[setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','fixmo_app')
G.edge['untrusteddomain']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','fixmo_app')
G.edge['untrusteddomain']['fixmo_app']['write-read'] = '[setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('untrusteddomain','kernel')
G.edge['untrusteddomain']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','mm-qcamera-daemon')
G.edge['untrusteddomain']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','mm-qcamera-daemon')
G.edge['untrusteddomain']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','mobexdaemon')
G.edge['untrusteddomain']['mobexdaemon']['write-read'] = '[write read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','rild')
G.edge['untrusteddomain']['rild']['write-read'] = '[open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','untrusteddomain')
G.edge['untrusteddomain']['untrusteddomain']['write-read'] = '[open open][write read][append read][setattr getattr][write read][append read][setopt getopt][open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('untrusteddomain','vmware_app')
G.edge['untrusteddomain']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('untrusteddomain','vmware_app')
G.edge['untrusteddomain']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','apaservice')
G.edge['vmware_app']['apaservice']['write-read'] = '[open open]'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open]'
G.add_edge('vmware_app','fixmo_app')
G.edge['vmware_app']['fixmo_app']['write-read'] = '[open open]'
G.add_edge('vmware_app','kernel')
G.edge['vmware_app']['kernel']['write-read'] = '[open open]'
G.add_edge('vmware_app','mm-qcamera-daemon')
G.edge['vmware_app']['mm-qcamera-daemon']['write-read'] = '[open open]'
G.add_edge('vmware_app','mobexdaemon')
G.edge['vmware_app']['mobexdaemon']['write-read'] = '[open open]'
G.add_edge('vmware_app','rild')
G.edge['vmware_app']['rild']['write-read'] = '[open open]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open]'
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open]'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','fixmo_app')
G.edge['vmware_app']['fixmo_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','mm-qcamera-daemon')
G.edge['vmware_app']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','mobexdaemon')
G.edge['vmware_app']['mobexdaemon']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','rild')
G.edge['vmware_app']['rild']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open][setattr getattr]'
G.add_edge('vmware_app','apaservice')
G.edge['vmware_app']['apaservice']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['apaservice']['fill'] = 'red'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['bluetooth']['fill'] = 'red'
G.add_edge('vmware_app','fixmo_app')
G.edge['vmware_app']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['fixmo_app']['fill'] = 'red'
G.add_edge('vmware_app','kernel')
G.edge['vmware_app']['kernel']['write-read'] = '[open open][write read]'
G.edge['vmware_app']['kernel']['fill'] = 'red'
G.add_edge('vmware_app','mm-qcamera-daemon')
G.edge['vmware_app']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['mm-qcamera-daemon']['fill'] = 'red'
G.add_edge('vmware_app','mobexdaemon')
G.edge['vmware_app']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['mobexdaemon']['fill'] = 'red'
G.add_edge('vmware_app','rild')
G.edge['vmware_app']['rild']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['rild']['fill'] = 'red'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['untrusteddomain']['fill'] = 'red'
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read]'
G.edge['vmware_app']['vmware_app']['fill'] = 'red'
G.add_edge('vmware_app','apaservice')
G.edge['vmware_app']['apaservice']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vmware_app','apaservice')
G.edge['vmware_app']['apaservice']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','bluetooth')
G.edge['vmware_app']['bluetooth']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','fixmo_app')
G.edge['vmware_app']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','fixmo_app')
G.edge['vmware_app']['fixmo_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','kernel')
G.edge['vmware_app']['kernel']['write-read'] = '[open open][write read][add_name search]'
G.add_edge('vmware_app','kernel')
G.edge['vmware_app']['kernel']['write-read'] = '[open open][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','mm-qcamera-daemon')
G.edge['vmware_app']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','mm-qcamera-daemon')
G.edge['vmware_app']['mm-qcamera-daemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','mobexdaemon')
G.edge['vmware_app']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','mobexdaemon')
G.edge['vmware_app']['mobexdaemon']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','rild')
G.edge['vmware_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','rild')
G.edge['vmware_app']['rild']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','untrusteddomain')
G.edge['vmware_app']['untrusteddomain']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search]'
G.add_edge('vmware_app','vmware_app')
G.edge['vmware_app']['vmware_app']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search]'
app = Viewer(G)
app.mainloop()