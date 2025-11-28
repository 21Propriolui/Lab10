from database.dao import DAO
import networkx as nx

class Model:
    def __init__(self):
        self._nodes = None
        self._edges = None
        self.G = nx.Graph()

    def costruisci_grafo(self, threshold):
        """
        Costruisce il grafo (self.G) inserendo tutti gli Hub (i nodi) presenti e filtrando le Tratte con
        guadagno medio per spedizione >= threshold (euro)
        """
        # TODO
        self.G.clear()  # ripulisco il grafo ogni volta
        hubs = DAO.get_hubs()
        for hub in hubs:
            self.G.add_node(hub) # aggiungo tutti gli hub per far si che get_num_nodes funzioni correttamente
        hub_dizionario = {hub.id : hub for hub in hubs}  # creo un dizionario di hub da mettere come nodi
        tratte = DAO.get_tratta()
        for tratta in tratte:
            if tratta.valore >= float(threshold):  # se il valore è maggiore della soglia
                self.G.add_edge(hub_dizionario[tratta.hub_partenza], hub_dizionario[tratta.hub_arrivo], valore=tratta.valore)
                # creo arco tra i due hub con peso il valore

    def get_num_edges(self):
        """
        Restituisce il numero di Tratte (edges) del grafo
        :return: numero di edges del grafo
        """
        # TODO
        self._edges = self.G.number_of_edges()  # numero di edges
        return self._edges

    def get_num_nodes(self):
        """
        Restituisce il numero di Hub (nodi) del grafo
        :return: numero di nodi del grafo
        """
        # TODO
        self._nodes = self.G.number_of_nodes()  # numero di nodi
        return self._nodes

    def get_all_edges(self):
        """
        Restituisce tutte le Tratte (gli edges) con i corrispondenti pesi
        :return: gli edges del grafo con gli attributi (il weight)
        """
        # TODO
        return [(hub_1, hub_2, peso['valore']) for hub_1, hub_2, peso in self.G.edges(data=True)]
        # aggiungo a una lista hub partenza, hub arrivo e peso per ogni tratta con peso
