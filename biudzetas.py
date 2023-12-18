import pickle
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('biudzetas.log', encoding="UTF-8")
logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(stream_handler)

from models.islaidu_irasas import IslaiduIrasas
from models.pajamu_irasas import PajamuIrasas

# logging.basicConfig(filename="biudzetas.log", level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s', encoding="UTF-8")


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_is_failo()

    def nuskaityti_is_failo(self):
        try:
            with open("zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
                logger.info("Žurnalas nuskaitytas iš failo")
        except:
            zurnalas = []
            logger.info("Sukurtas naujas žurnalas")
        return zurnalas

    def irasyti_i_faila(self):
        with open("zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)
            logger.info("Žurnalas įrašytas į failą")

    def prideti_pajamu_irasa(self, suma, siuntejas, info):
        irasas = PajamuIrasas(suma, siuntejas, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def prideti_islaidu_irasa(self, suma, budas, isigyta, info):
        irasas = IslaiduIrasas(suma, budas, isigyta, info)
        self.zurnalas.append(irasas)
        self.irasyti_i_faila()

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if type(irasas) is PajamuIrasas:
                balansas += irasas.suma
            if type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        logger.info("Paskaičiuotas balansas")
        return balansas

    def istrinti_irasa(self, indeksas):
        logger.info(f"Ištrintas įrašas: {self.zurnalas[indeksas]}")
        self.zurnalas.pop(indeksas)
        self.irasyti_i_faila()
