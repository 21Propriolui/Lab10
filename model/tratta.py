from dataclasses import dataclass

@dataclass
class Tratta:
    hub_partenza : int
    hub_arrivo : int
    nome_partenza : str
    nome_arrivo : str
    valore : float

    def __str__(self):
        return f"{self.hub_partenza} {self.hub_arrivo} {self.valore}"

    def __repr__(self):
        return f"{self.hub_partenza} {self.hub_arrivo} {self.valore}"

    def __eq__(self, other):
        return isinstance(other, Tratta) and self.hub_partenza == other.hub_partenza and other.hub_arrivo == other.hub_arrivo

    def __hash__(self):
        return hash((self.hub_partenza, self.hub_arrivo))