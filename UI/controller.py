import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def mostra_tratte(self, e):
        """
        Funzione che controlla prima se il valore del costo inserito sia valido (es. non deve essere una stringa) e poi
        popola "self._view.lista_visualizzazione" con le seguenti info
        * Numero di Hub presenti
        * Numero di Tratte
        * Lista di Tratte che superano il costo indicato come soglia
        """
        # TODO
        # controllo che il textfield sia un numero
        try:
            threshold = float(self._view.guadagno_medio_minimo.value)
        except ValueError:
            self._view.show_alert('Inserire un guadagno medio minimo valido')
        else:
            self._model.costruisci_grafo(threshold)
            num_nodes = self._model.get_num_nodes()
            num_edges = self._model.get_num_edges()
            tratte = self._model.get_all_edges() # ottengo num nodi, num tratte e tratte

            self._view.lista_visualizzazione.clean()   # ripulisco la listview
            self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di Hubs: {num_nodes}'))
            self._view.lista_visualizzazione.controls.append(ft.Text(f'Numero di Tratte: {num_edges}'))
            for lista in tratte:
                self._view.lista_visualizzazione.controls.append(ft.Text(f'{lista[0]} --> {lista[1]} -- Guadagno medio per spedizione: {lista[2]}€'))
            self._view.update()
