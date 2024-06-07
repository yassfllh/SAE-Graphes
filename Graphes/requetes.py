import json
import networkx as nx

# Q1
def json_vers_nx(chemin):
    """
    Convertit un fichier JSON en un fichiers Networkx.
    
    Paramètres :
    chemin (str): Le chemin du fichier JSON.
    
    Retourne :
    nx.Graph: Le graphe des collaborations.
    """
    G = nx.Graph()
    with open(chemin, 'r', encoding='utf-8') as f:
        for line in f:
            film = json.loads(line)
            acteurs = film["cast"]
            title = film.get("title", "Unknown")
            year = film.get("year", "Unknown")
            for i in range(len(acteurs)):
                for j in range(i + 1, len(acteurs)):
                    acteur1 = acteurs[i].strip('[]')
                    acteur2 = acteurs[j].strip('[]')
                    G.add_edge(acteur1, acteur2, title=title, year=year)
    return G

# Q2
def collaborateurs_communs(G, u, v):
    """
    Trouve les collaborateurs communs de deux acteurs.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): Le premier acteur.
    v (str): Le deuxième acteur.
    
    Retourne :
    set: Ensemble des collaborateurs communs.
    """
    if u not in G.nodes or v not in G.nodes:
        return None
    voisins_u = set(G.neighbors(u))
    voisins_v = set(G.neighbors(v))
    return voisins_u.intersection(voisins_v)

# Q3
def collaborateurs_proches(G, u, k):
    """
    Trouve les collaborateurs proches d’un acteur jusqu’à une distance k.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): L'acteur de départ.
    k (int): La distance maximale.
    
    Retourne :
    set: Ensemble des collaborateurs proches.
    """
    return {v for v in G.nodes if nx.shortest_path_length(G, u, v) <= k}

def est_proche(G, u, v, k=1):
    """
    Vérifie si deux acteurs sont proches jusqu’à une distance k.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): Le premier acteur.
    v (str): Le deuxième acteur.
    k (int): La distance maximale.
    
    Retourne :
    bool: True si les acteurs sont proches, false sinon.
    """
    try:
        return nx.shortest_path_length(G, u, v) <= k
    except nx.NetworkXNoPath:
        return False

def distance_naive(G, u, v):
    """
    Calcule la distance entre deux acteurs.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): Le premier acteur.
    v (str): Le deuxième acteur.
    
    Retourne :
    int: La distance entre les deux acteurs.
    """
    try:
        return nx.shortest_path_length(G, u, v)
    except nx.NetworkXNoPath:
        return float('inf')

def distance(G, u, v):
    """
    Calcule la distance entre deux acteurs.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): Le premier acteur.
    v (str): Le deuxième acteur.
    
    Retourne :
    int: La distance entre les deux acteurs.
    """
    return distance_naive(G, u, v)

# Q4
def centralite(G, u):
    """
    Calcule la centralité d'un acteur dans le graphe.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    u (str): L'acteur dont on veut calculer la centralité.
    
    Retourne :
    int: La centralité de l'acteur.
    """
    return max(nx.single_source_shortest_path_length(G, u).values())

def centre_hollywood(G):
    """
    Trouve l'acteur le plus central d'Hollywood.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    
    Retourne :
    str: L'acteur le plus central.
    """
    centralite_min = float('inf')
    acteur_central = None
    for acteur in G.nodes:
        centralite_acteur = centralite(G, acteur)
        if centralite_acteur < centralite_min:
            centralite_min = centralite_acteur
            acteur_central = acteur
    return acteur_central

# Q5
def eloignement_max(G):
    """
    Détermine la distance maximale entre deux acteurs dans le graphe.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    
    Retourne :
    int: La distance maximale.
    """
    return nx.diameter(G)

# Bonus
def centralite_groupe(G, S):
    """
    Calcule la centralité d'un groupe d'acteurs.
    
    Paramètres :
    G (nx.Graph): Le graphe des collaborations.
    S (list): La liste des acteurs.
    
    Retourne :
    float: La centralité du groupe.
    """
    total_centralite = 0
    for s in S:
        chemins = nx.single_source_shortest_path_length(G, s)
        total_centralite += sum(chemins.values())
    return total_centralite / len(S)
