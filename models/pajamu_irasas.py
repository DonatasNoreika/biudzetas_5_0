from models.irasas import Irasas
from biudzetas import logger
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.info = info
        logger.info(f"Sukurtas pajamų įrašas: {self.suma}")

    def __str__(self):
        return f"Pajamos: {self.suma} ({self.siuntejas}, {self.info})"

    def __repr__(self):
        return f"Pajamos: {self.suma} ({self.siuntejas}, {self.info})"
