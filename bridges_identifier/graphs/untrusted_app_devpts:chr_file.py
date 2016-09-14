import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('carrier_app','carrier_app')
G.edge['carrier_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['carrier_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_google_app')
G.edge['carrier_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('carrier_app','filtered_untrusted_app')
G.edge['carrier_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','gad_untrusted_app')
G.edge['carrier_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','irm_app')
G.edge['carrier_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['irm_app']['fill'] = 'red'
G.add_edge('carrier_app','knox_untrusted_app')
G.edge['carrier_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','llk_untrusted_app')
G.edge['carrier_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','trustonicpartner_app')
G.edge['carrier_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('carrier_app','umcagent_app')
G.edge['carrier_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['umcagent_app']['fill'] = 'red'
G.add_edge('carrier_app','untrusted_app')
G.edge['carrier_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['untrusted_app']['fill'] = 'red'
G.add_edge('carrier_app','vpn_untrusted_app')
G.edge['carrier_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['carrier_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_google_app','carrier_app')
G.edge['filtered_google_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_google_app')
G.edge['filtered_google_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_google_app','filtered_untrusted_app')
G.edge['filtered_google_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','gad_untrusted_app')
G.edge['filtered_google_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','irm_app')
G.edge['filtered_google_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_google_app','knox_untrusted_app')
G.edge['filtered_google_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','llk_untrusted_app')
G.edge['filtered_google_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','trustonicpartner_app')
G.edge['filtered_google_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_google_app','umcagent_app')
G.edge['filtered_google_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_google_app','untrusted_app')
G.edge['filtered_google_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_google_app','vpn_untrusted_app')
G.edge['filtered_google_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_google_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('filtered_untrusted_app','carrier_app')
G.edge['filtered_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_google_app')
G.edge['filtered_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','filtered_untrusted_app')
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','gad_untrusted_app')
G.edge['filtered_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','irm_app')
G.edge['filtered_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','knox_untrusted_app')
G.edge['filtered_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','llk_untrusted_app')
G.edge['filtered_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','trustonicpartner_app')
G.edge['filtered_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','umcagent_app')
G.edge['filtered_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','untrusted_app')
G.edge['filtered_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('filtered_untrusted_app','vpn_untrusted_app')
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['filtered_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('gad_untrusted_app','carrier_app')
G.edge['gad_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_google_app')
G.edge['gad_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','filtered_untrusted_app')
G.edge['gad_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','gad_untrusted_app')
G.edge['gad_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','irm_app')
G.edge['gad_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','knox_untrusted_app')
G.edge['gad_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','llk_untrusted_app')
G.edge['gad_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','trustonicpartner_app')
G.edge['gad_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','umcagent_app')
G.edge['gad_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','untrusted_app')
G.edge['gad_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('gad_untrusted_app','vpn_untrusted_app')
G.edge['gad_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['gad_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open]'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('irm_app','carrier_app')
G.edge['irm_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['carrier_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_google_app')
G.edge['irm_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('irm_app','filtered_untrusted_app')
G.edge['irm_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','gad_untrusted_app')
G.edge['irm_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','irm_app')
G.edge['irm_app']['irm_app']['write-read'] = '[open open][setattr getattr][setattr getattr][write read][append read][setopt getopt][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][write read]'
G.edge['irm_app']['irm_app']['fill'] = 'red'
G.add_edge('irm_app','knox_untrusted_app')
G.edge['irm_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','llk_untrusted_app')
G.edge['irm_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','trustonicpartner_app')
G.edge['irm_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('irm_app','umcagent_app')
G.edge['irm_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['umcagent_app']['fill'] = 'red'
G.add_edge('irm_app','untrusted_app')
G.edge['irm_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['untrusted_app']['fill'] = 'red'
G.add_edge('irm_app','vpn_untrusted_app')
G.edge['irm_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['irm_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('knox_untrusted_app','carrier_app')
G.edge['knox_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_google_app')
G.edge['knox_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','filtered_untrusted_app')
G.edge['knox_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','gad_untrusted_app')
G.edge['knox_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','irm_app')
G.edge['knox_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','knox_untrusted_app')
G.edge['knox_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][open open][setattr getattr][write read][append read][write read][open open][setattr getattr][write read][add_name search][remove_name search][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','llk_untrusted_app')
G.edge['knox_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','trustonicpartner_app')
G.edge['knox_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','umcagent_app')
G.edge['knox_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','untrusted_app')
G.edge['knox_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('knox_untrusted_app','vpn_untrusted_app')
G.edge['knox_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['knox_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('llk_untrusted_app','carrier_app')
G.edge['llk_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_google_app')
G.edge['llk_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','filtered_untrusted_app')
G.edge['llk_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','gad_untrusted_app')
G.edge['llk_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','irm_app')
G.edge['llk_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','knox_untrusted_app')
G.edge['llk_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','llk_untrusted_app')
G.edge['llk_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','trustonicpartner_app')
G.edge['llk_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','umcagent_app')
G.edge['llk_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','untrusted_app')
G.edge['llk_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('llk_untrusted_app','vpn_untrusted_app')
G.edge['llk_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['llk_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('trustonicpartner_app','carrier_app')
G.edge['trustonicpartner_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['carrier_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_google_app')
G.edge['trustonicpartner_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','filtered_untrusted_app')
G.edge['trustonicpartner_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','gad_untrusted_app')
G.edge['trustonicpartner_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','irm_app')
G.edge['trustonicpartner_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['irm_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','knox_untrusted_app')
G.edge['trustonicpartner_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','llk_untrusted_app')
G.edge['trustonicpartner_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','trustonicpartner_app')
G.edge['trustonicpartner_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','umcagent_app')
G.edge['trustonicpartner_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['umcagent_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','untrusted_app')
G.edge['trustonicpartner_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['untrusted_app']['fill'] = 'red'
G.add_edge('trustonicpartner_app','vpn_untrusted_app')
G.edge['trustonicpartner_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['trustonicpartner_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('umcagent_app','carrier_app')
G.edge['umcagent_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['carrier_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_google_app')
G.edge['umcagent_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('umcagent_app','filtered_untrusted_app')
G.edge['umcagent_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','gad_untrusted_app')
G.edge['umcagent_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','irm_app')
G.edge['umcagent_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['irm_app']['fill'] = 'red'
G.add_edge('umcagent_app','knox_untrusted_app')
G.edge['umcagent_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','llk_untrusted_app')
G.edge['umcagent_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','trustonicpartner_app')
G.edge['umcagent_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('umcagent_app','umcagent_app')
G.edge['umcagent_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['umcagent_app']['fill'] = 'red'
G.add_edge('umcagent_app','untrusted_app')
G.edge['umcagent_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['untrusted_app']['fill'] = 'red'
G.add_edge('umcagent_app','vpn_untrusted_app')
G.edge['umcagent_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['umcagent_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('untrusted_app','carrier_app')
G.edge['untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_google_app')
G.edge['untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('untrusted_app','filtered_untrusted_app')
G.edge['untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','gad_untrusted_app')
G.edge['untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','irm_app')
G.edge['untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('untrusted_app','knox_untrusted_app')
G.edge['untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','llk_untrusted_app')
G.edge['untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','trustonicpartner_app')
G.edge['untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('untrusted_app','umcagent_app')
G.edge['untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('untrusted_app','untrusted_app')
G.edge['untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('untrusted_app','vpn_untrusted_app')
G.edge['untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open]'
G.add_edge('vpn_untrusted_app','carrier_app')
G.edge['vpn_untrusted_app']['carrier_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['carrier_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_google_app')
G.edge['vpn_untrusted_app']['filtered_google_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['filtered_google_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','filtered_untrusted_app')
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['filtered_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','gad_untrusted_app')
G.edge['vpn_untrusted_app']['gad_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['gad_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','irm_app')
G.edge['vpn_untrusted_app']['irm_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['irm_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','knox_untrusted_app')
G.edge['vpn_untrusted_app']['knox_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['knox_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','llk_untrusted_app')
G.edge['vpn_untrusted_app']['llk_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['llk_untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','trustonicpartner_app')
G.edge['vpn_untrusted_app']['trustonicpartner_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['trustonicpartner_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','umcagent_app')
G.edge['vpn_untrusted_app']['umcagent_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['umcagent_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','untrusted_app')
G.edge['vpn_untrusted_app']['untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['untrusted_app']['fill'] = 'red'
G.add_edge('vpn_untrusted_app','vpn_untrusted_app')
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['write-read'] = '[open open][setattr getattr][write read][open open][setattr getattr][write read][append read][open open][setattr getattr][write read][add_name search][remove_name search][open open][write read]'
G.edge['vpn_untrusted_app']['vpn_untrusted_app']['fill'] = 'red'
app = Viewer(G)
app.mainloop()