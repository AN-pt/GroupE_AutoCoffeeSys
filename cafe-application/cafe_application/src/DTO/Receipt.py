from datetime import date


class Receipt:
    def __init__(self, receiptID = "", baristaID = "", dor = date(1, 1, 1), grandTotal = 0.0, deleted = False):
        self.__receiptID = receiptID
        self.__baristaID = baristaID
        self.__dor = dor
        self.__grandTotal = grandTotal
        self.__deleted = deleted

    def getReceiptID(self) -> str:
        return self.__receiptID

    def setReceiptID(self, receiptID) -> None:
        self.__receiptID = receiptID

    def getBaristaID(self) -> str:
        return self.__baristaID

    def setBaristaID(self, baristaID) -> None:
        self.__baristaID = baristaID

    def getDor(self) -> date:
        return self.__dor

    def setDor(self, dor) -> None:
        self.__dor = dor

    def getGrandTotal(self) -> float:
        return self.__grandTotal

    def setGrandTotal(self, grandTotal) -> None:
        self.__grandTotal = grandTotal

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__receiptID} | " \
            + f"{self.__baristaID} | " \
            + f"{self.__dor} | " \
            + f"{self.__grandTotal}"
