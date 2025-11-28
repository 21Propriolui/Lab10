from database.DB_connect import DBConnect
from model.hub import Hub
from model.tratta import Tratta

class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO

    @staticmethod
    def get_hubs():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """ 
                    SELECT *
                    FROM hub
                        """
        try:
            cursor.execute(query)
            for row in cursor:
                tratta = Hub(
                    id=row["id"],
                    codice=row["codice"],
                    nome=row["nome"],
                    citta=row["citta"],
                    stato=row["stato"],
                    latitudine=row["latitudine"],
                    longitudine=row["longitudine"],
                )
                result.append(tratta)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result

    @staticmethod
    def get_tratta():
        cnx = DBConnect.get_connection()
        result = []

        if cnx is None:
            print("❌ Errore di connessione al database.")
            return None

        cursor = cnx.cursor(dictionary=True)
        # nella query seleziono le spedizioni in modo che vengano considerate tutte in una sola direzione tramite least e greatest
        query = """ 
                SELECT LEAST(id_hub_origine, id_hub_destinazione) AS hub_partenza,
                       GREATEST(id_hub_origine, id_hub_destinazione) AS hub_arrivo,
                       AVG(valore_merce) AS valore,
                       hub1.nome AS nome_partenza, hub2.nome AS nome_arrivo
                FROM spedizione, hub AS hub1, hub AS hub2
                WHERE hub1.id = LEAST(id_hub_origine, id_hub_destinazione)
                AND hub2.id = GREATEST(id_hub_origine, id_hub_destinazione)
                GROUP BY hub_partenza, hub_arrivo
                    """
        try:
            cursor.execute(query)
            for row in cursor:
                tratta = Tratta(
                    hub_partenza=row["hub_partenza"],
                    hub_arrivo=row["hub_arrivo"],
                    nome_partenza=row["nome_partenza"],
                    nome_arrivo=row["nome_arrivo"],
                    valore=row["valore"],
                )
                result.append(tratta)
        except Exception as e:
            print(f"Errore durante la query: {e}")
            result = None
        finally:
            cursor.close()
            cnx.close()

        return result