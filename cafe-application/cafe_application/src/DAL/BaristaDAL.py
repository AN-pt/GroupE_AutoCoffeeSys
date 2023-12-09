from typing import List

from DAL.Manager import Manager
from DTO.Barista import Barista


class BaristaDAL(Manager):
    def __init__(self):
        super().__init__("barista", [
            "BARISTA_ID",
            "NAME",
            "GENDER",
            "DOB",
            "ADDRESS",
            "PHONE",
            "EMAIL",
            "SALARY",
            "ENTRY_DATE",
            "DELETED"
        ])

    def convertToBaristas(self, data: List[List[object]]) -> List[Barista]:
        return self.convert(data, lambda row: Barista(
            row['BARISTA_ID'],
            row['NAME'],
            row['GENDER'],
            row['DOB'],
            row['ADDRESS'],
            row['PHONE'],
            row['EMAIL'],
            row['SALARY'],
            row['ENTRY_DATE'],
            bool(row['DELETED'])
        ))

    def addBarista(self, barista: Barista) -> int:
        try:
            return self.create(
                barista.getBaristaID(),
                barista.getName(),
                barista.isGender(),
                barista.getDateOfBirth(),
                barista.getAddress(),
                barista.getPhone(),
                barista.getEmail(),
                barista.getSalary(),
                barista.getDateOfEntry(),
                False
            ) # barista khi tạo mặc định deleted = 0
        except Exception as e:
            print(f"Error occurred in BaristaDAL.addBarista(): {e}")
        return 0

    def updateBarista(self, barista: Barista) -> int:
        try:
            updateValues = [
                barista.getBaristaID(),
                barista.getName(),
                barista.isGender(),
                barista.getDateOfBirth(),
                barista.getAddress(),
                barista.getPhone(),
                barista.getEmail(),
                barista.getSalary(),
                barista.getDateOfEntry(),
                barista.isDeleted()
            ]
            return self.update(updateValues, f"BARISTA_ID = '{barista.getBaristaID()}'")
        except Exception as e:
            print(f"Error occurred in BaristaDAL.updateBarista(): {e}")
        return 0

    def deleteBarista(self, *conditions: str) -> int:
        try:
            updateValues = [True]
            return self.update(updateValues, *conditions)
        except Exception as e:
            print(f"Error occurred in BaristaDAL.deleteBarista(): {e}")
        return 0

    def searchBaristas(self, *conditions: str) -> List[Barista]:
        try:
            return self.convertToBaristas(self.read(*conditions))
        except Exception as e:
            print(f"Error occurred in BaristaDAL.searchBaristas(): {e}")
        return []

    def getAutoID(self) -> str:
        try:
            return super().getAutoID("BA", 2)
        except Exception as e:
            print(f"Error occurred in BaristaDAL.getAutoID(): {e}")
        return ""
