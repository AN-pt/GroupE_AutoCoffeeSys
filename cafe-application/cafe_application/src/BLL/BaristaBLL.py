from typing import List

from BLL.Manager import Manager
from DAL.BaristaDAL import BaristaDAL
from DTO.Barista import Barista


class BaristaBLL(Manager[Barista]):
    def __init__(self):
        try:
            self.__baristaDAL = BaristaDAL()
            self.__baristaList = self.searchBaristas("DELETED = 0", "BARISTA_ID != 'B00'")
        except Exception:
            pass

    def getBaristaDAL(self) -> BaristaDAL:
        return self.__baristaDAL

    def setBaristaDAL(self, baristaDAL: BaristaDAL) -> BaristaDAL:
        self.__baristaDAL = baristaDAL

    def getBaristaList(self) -> list:
        return self.__baristaList

    def setBaristaList(self, baristaList) -> list:
        self.__baristaList = baristaList

    def getData(self) -> list[list[object]]:
        return super().getData(self.__baristaList)

    def addBarista(self, barista: Barista) -> bool:
        if self.getIndex(barista, "PHONE", self.__baristaList) != -1:
            print("Can't add new barista. Phone already exists.")
            return False
        self.__baristaList.append(barista)
        return self.__baristaDAL.addBarista(barista) != 0

    def updateBarista(self, barista: Barista) -> bool:
        self.__baristaList[self.getIndex(barista, "BARISTA_ID", self.__baristaList)] = barista
        return self.__baristaDAL.updateBarista(barista) != 0

    def deleteBarista(self, barista: Barista) -> bool:
        self.__baristaList.pop(self.getIndex(barista, "BARISTA_ID", self.__baristaList))
        return self.__baristaDAL.deleteBarista(f"BARISTA_ID = '{barista.getBaristaID()}'") != 0

    def searchBaristas(self, *conditions: str) -> List[Barista]:
        return self.__baristaDAL.searchBaristas(*conditions)

    def findBaristasBy(self, conditions: dict) -> list[Barista]:
        baristas = self.__baristaList
        for key, value in conditions.items():
            baristas = super().findObjectsBy(key, value, baristas)
        return baristas

    def getAutoID(self) -> str:
        return super().getAutoID("B", 2, self.searchBaristas("BARISTA_ID != 'B00'"))

    def getValueByKey(self, barista: Barista, key: str) -> object:
        return {
            "BARISTA_ID": barista.getBaristaID(),
            "NAME": barista.getName(),
            "GENDER": barista.isGender(),
            "DOB": barista.getDateOfBirth(),
            "ADDRESS": barista.getAddress(),
            "PHONE": barista.getPhone(),
            "EMAIL": barista.getEmail(),
            "SALARY": barista.getSalary(),
            "DOENTRY": barista.getDateOfEntry()
        }.get(key, None)
