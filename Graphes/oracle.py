# Importation

from requetes import json_vers_nx, collaborateurs_communs, collaborateurs_proches, est_proche, distance_naive, distance, centralite, centre_hollywood, eloignement_max, centralite_groupe

import matplotlib.pyplot as plt
import networkx as nx

def afficher_graphe(G):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, edge_color='gray', linewidths=1, font_size=10)
    plt.show()
    plt.title("Graphe des collab")


def tester_requetes():
    jeudeDonnees = ['data_100.txt']
    
    for chemin in jeudeDonnees:
        G = json_vers_nx(chemin)
        
        # Affichage
        print(nx.info(G))
        print(f"--------------------------------------------------------------------------")
        
        acteurs_communs = collaborateurs_communs(G, 'Al Pacino', 'Robert De Niro')
        print(f"Collaborateurs commun avec Al Pacino et Robert de Niro : {acteurs_communs}")
        print(f"--------------------------------------------------------------------------")
        
        collaborateurs = collaborateurs_proches(G, 'Al Pacino', 2)
        print(f"Collaborateurs proches de Al Pacino : {collaborateurs}")
        print(f"--------------------------------------------------------------------------")
        
        proches = est_proche(G, 'Al Pacino', 'Robert De Niro', 2)
        print(f"Robert de Niro et Al Pacino sont proches à distance = 2 ? {proches}")
        print(f"--------------------------------------------------------------------------")
        
        distance_naive_val = distance_naive(G, 'Al Pacino', 'Robert De Niro')
        print(f"Distance naïve entre Al Pacino et Robert De Niro : {distance_naive_val}")
        print(f"--------------------------------------------------------------------------")
        
        distance_val = distance(G, 'Al Pacino', 'Robert De Niro')
        print(f"Distance entre Al Pacino et Robert De Niro : {distance_val}")
        print(f"--------------------------------------------------------------------------")
        
        centralite_al_pacino = centralite(G, 'Al Pacino')
        print(f"Centralité de Al Pacino : {centralite_al_pacino}")
        print(f"--------------------------------------------------------------------------")
        
        centre = centre_hollywood(G)
        print(f"L'acteur le plus central de Hollywood : {centre}")
        print(f"--------------------------------------------------------------------------")
        
        distance_max = eloignement_max(G)
        print(f"Éloignement maximal dans le graphe : {distance_max}")
        print(f"--------------------------------------------------------------------------")
        
        # bonus
        groupe = ['Al Pacino', 'Robert De Niro']
        centralite_groupe_val = centralite_groupe(G, groupe)
        print(f"Centralité du groupe d'Al Pacino et Robert de Niro : {centralite_groupe_val}")
        print(f"--------------------------------------------------------------------------")
        
        print("\n" + "-"*50 + "\n")

        afficher_graphe(G)

if __name__ == "__main__":
    tester_requetes()
