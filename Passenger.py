class Passenger:

    """
    A passenger object that will be created by this class will
    contain all the features of a passenger.
    """

    def __init__(self, id, age, sib, fare, pclass, sex, survival):
        AVG_AGE = 29
        AVG_FARE = 21
        AVG_PCLASS = 2
        AVG_SIB = 1
        AVG_SEX = "male"

        self._Id=int(id)

        if age == "":
            self._Age=AVG_AGE
        else:
            self._Age=float(age)

        if fare == "":
            self._Fare = AVG_FARE
        else:
            self._Fare = float(fare)

        if pclass == "":
            self._Pclass = AVG_PCLASS
        else:
            self._Pclass = int(pclass)

        if sex == "":
            self._Sex = AVG_SEX
        else:
            self._Sex = sex

        if sib == "":
            self._Sib = AVG_SIB
        else:
            self._Sib = int(sib)
        if survival == "":
            self._Survival = ""
        else:
            self._Survival = int(survival)


    def print_me(self):
        print("passenger ID:",self._Id, " information:")
        print("Name:", self._Name,
              " Age: ", self._Age ,
              " Sib: ", self._Sib,
              " Fare:", self._Fare,
              " Pclass:", self._Pclass,
              " Sex: ", self._Sex,
              " Survival ", self._Survival, sep=",")

    def get_value_of(self, attr):
        if attr == "Age":
            return self.get_age()

        elif attr == "Sib":
            return self.get_sib()

        elif attr == "Fare":
            return self.get_fare()

        elif attr == "Pclass":
            return self.get_pclass()

        elif attr == "Sex":
            return self.get_sex()

        elif attr == "Survival":
            return self.get_survival()

        elif attr == "Name":
            return self.get_name()

        elif attr == "Id":
            return self.get_id()

        return ""

    def set_survival(self, value):
        self._Survival = value

    def get_age(self):
        return self._Age

    def get_sib(self):
        return self._Sib

    def get_fare(self):
        return self._Fare

    def get_pclass(self):
        return self._Pclass

    def get_sex(self):
        return self._Sex

    def get_survival(self):
        return self._Survival

    def get_name(self):
        return self._Name

    def get_id(self):
        return self._Id
