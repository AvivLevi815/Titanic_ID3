import math

"""
The Node is the building block of the tree (see Tree class)
in it the population is stored in the training and in the test it represent
a value or a range of values for an attribute so a record will be able to sort its way
to the leaf Node, containing the final classification.
"""


class Node:
    def __init__(self, name=None, father=None, passengers=None, sons=[], attr=None, option=""):
        self._Name = name
        self._Father = father
        self._Passengers = passengers
        self._Sons = sons
        self._Attr = attr
        self._Index = 0
        self._leaf = False
        self._Option = option    # e.g "male" or "female" when father node is "sex"
    """
    best split is a function that returns the Name of the best feature to split on
    based on the entropy before and after the split
    the bigger the information gain - the better the split.
    """
    def best_split(self):
        """
        All the Passengers with value in Attr_option of attribute Attribute
        for example all the passengers that A=sex and V=mame
        """
        sub_group  = []

        current_entropy = self.entropy(self._Passengers)
        best_gain = 0  # holds the best entropy difference so far
        best_split = self._Attr[0].get_name()
        relative_entropy = 0  # entropy while taking account for the size of the population

        for Attribute in self._Attr:
            relative_entropy = 0
            print("Attr considered: " + Attribute.get_name())
            for Attr_option in Attribute.get_options():
                sub_group = []
                for Passenger in self._Passengers:
                    if self.passenger_attr_option_check(Passenger,
                                                        Attribute.get_name(),
                                                        Attr_option):  # if P.A = V
                        sub_group.append(Passenger)
                if len(sub_group) > 0 and len(self._Passengers) > 0:
                    relative_entropy += self.entropy(sub_group) * (len(sub_group)/len(self._Passengers))

            if current_entropy - relative_entropy > best_gain:
                best_gain = current_entropy - relative_entropy
                best_split = Attribute.get_name()

        print(f"best split:{best_split} \n with entropy gain of:\n {best_gain}")

        return best_split

    """
    this function checks if the passenger Passenger has an attribute attr with value in
    Attr_option.
    
    for example:
    Passenger = ("Aviv Levi", 313546186, 23, 1, 20, 1, "male", 1)
    attr = sex
    Attr_option = "male"
    
    Passenger: passenger
    attr: String
    Attr_option: String or list
    
    the output will be true because the passenger's sex is "male"
    """
    def passenger_attr_option_check(self, Passenger, attr, Attr_option):

        if attr == "Sex":
            if Passenger.get_sex() == Attr_option:
                return True

        elif attr == "Fare":
            fare = Passenger.get_fare()
            if fare == '':
                return True
            if Attr_option[0] <= math.floor(fare) <= Attr_option[1]:
                return True

        elif attr == "Age":
            age = Passenger.get_age()
            """ sending empty values to first son - not best"""
            if age == '' or Attr_option[0] <= age <= Attr_option[1]:
                return True

        elif attr == "Sib":
            sib = Passenger.get_sib()
            if sib == '' or Attr_option[0] <= Passenger.get_sib() <= Attr_option[1]:
                return True

        elif attr == "Pclass":
            pclass = Passenger.get_pclass()
            if pclass == '' or Passenger.get_pclass() == Attr_option:
                return True

    """
    this function calcultes the entropy of a population:
    -P(survived)*log(P(survived)) - P(died)*log(P(died)) 
    where P(X) is the probability of X.  
    """
    def entropy(self, population):
        if(len(population) == 0):
            return 0
        count_survival = 0
        count_dead = 0
        for passenger in population:
            if passenger.get_survival() == 1:
                count_survival += 1
            else:
                count_dead += 1

        p_survived = count_survival/len(population)
        p_dead = count_dead/len(population)
        if p_survived != 0 and p_dead != 0:
            return (-1*p_survived * math.log10(p_survived)) - (p_dead * math.log10(p_dead))
        else:
            return 0

    """
    this function is used to determined the classification of a leaf Node,
    it simply sets the majority result - death or survival as the Node's classification.
    """
    def most_common_result(self):
        count_survive = 0
        count_death = 0

        for passenger in self._Passengers:
            if passenger.get_survival() == 1:
                count_survive += 1

            else:
                count_death += 1

        if count_survive >= count_death:
            return "survive"
        else:
            return "death"

    def __iter__(self):
        try:
            return iter(self._Passengers[0])

        except IndexError:
            return None

    def __next__(self):
        try:
            self._Index += 1
            return self._Passengers[self._Index]

        except IndexError:
            self._Index = 0
            return None

    def set_name(self, name):
        self._Name = name

    def set_leaf(self, value):
        self._leaf = value

    def get_attr(self):
        return self._Attr

    def get_passengers(self):
        return self._Passengers

    def add_son(self, node):
        self._Sons.append(node)

    def get_sons(self):
        return self._Sons

    def get_name(self):
        return self._Name

    def get_option(self):
        return self._Option










