from datetime import date


class Bill:
    def __init__(self, billID = "", customerID = "", baristaID = "", dateOfPurchase = date(1, 1, 1), total = 0, deleted = False):
        self.__billID = billID
        self.__customerID = customerID
        self.__baristaID = baristaID
        self.__dateOfPurchase = dateOfPurchase
        self.__total = total
        self.__deleted = deleted

    def getBillID(self) -> str:
        return self.__billID

    def setBillID(self, billID) -> None:
        self.__billID = billID

    def getCustomerID(self) -> str:
        return self.__customerID

    def setCustomerID(self, customerID) -> None:
        self.__customerID = customerID

    def getBaristaID(self) -> str:
        return self.__baristaID

    def setBaristaID(self, baristaID) -> None:
        self.__baristaID = baristaID

    def getDateOfPurchase(self) -> date:
        return self.__dateOfPurchase

    def setDateOfPurchase(self, dateOfPurchase) -> None:
        self.__dateOfPurchase = dateOfPurchase

    def getTotal(self) -> float:
        return self.__total

    def setTotal(self, total) -> None:
        self.__total = total

    def isDeleted(self):
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        return f"{self.__billID} | " \
            + f"{self.__customerID} | " \
            + f"{self.__baristaID} | " \
            + f"{self.__dateOfPurchase} | " \
            + f"{self.__total}"
