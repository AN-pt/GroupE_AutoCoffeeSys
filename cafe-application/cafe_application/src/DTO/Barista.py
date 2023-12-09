from datetime import date


class Barista:
    def __init__(self, baristaID = "", name = "", gender = False, dateOfBirth = date(1, 1, 1), address = "", phone = "", email = "", salary = 0.0, dateOfEntry = date(1, 1, 1), deleted = False):
        self.__baristaID = baristaID
        self.__name = name
        self.__gender = gender
        self.__dateOfBirth = dateOfBirth
        self.__address = address
        self.__phone = phone
        self.__email = email
        self.__salary = salary
        self.__dateOfEntry = dateOfEntry
        self.__deleted = deleted

    def getBaristaID(self) -> str:
        return self.__baristaID

    def setBaristaID(self, baristaID) -> None:
        self.__baristaID = baristaID

    def getName(self) -> str:
        return self.__name

    def setName(self, name) -> None:
        self.__name = name

    def isGender(self) -> bool:
        return self.__gender

    def setGender(self, gender) -> None:
        self.__gender = gender

    def getDateOfBirth(self) -> date:
        return self.__dateOfBirth

    def setDateOfBirth(self, dateOfBirth) -> None:
        self.__dateOfBirth = dateOfBirth

    def getAddress(self) -> str:
        return self.__address

    def setAddress(self, address) -> None:
        self.__address = address

    def getPhone(self) -> str:
        return self.__phone

    def setPhone(self, phone) -> None:
        self.__phone = phone

    def getEmail(self) -> str:
        return self.__email

    def setEmail(self, email) -> None:
        self.__email = email

    def getSalary(self) -> float:
        return self.__salary

    def setSalary(self, salary) -> None:
        self.__salary = salary

    def getDateOfEntry(self) -> date:
        return self.__dateOfEntry

    def setDateOfEntry(self, dateOfEntry) -> None:
        self.__dateOfEntry = dateOfEntry

    def isDeleted(self) -> bool:
        return self.__deleted

    def setDeleted(self, deleted) -> None:
        self.__deleted = deleted

    def __str__(self):
        gender1 = "Nam" if self.__gender else "Nữ"
        return f"{self.__baristaID} | " \
            + f"{self.__name} | " \
            + f"{gender1} | " \
            + f"{self.__dateOfBirth} | " \
            + f"{self.__address} | " \
            + f"{self.__phone} | " \
            + f"{self.__email} | " \
            + f"{self.__salary} | " \
            + f"{self.__dateOfEntry}"
