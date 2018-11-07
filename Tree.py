import Node
import copy
"""
In ID3 the main structure is a tree,
the tree will be constructed as the algorithm will go
in the end - given a record - the tree will flow it's way to a leaf.
The leaf will show the classification of the record.
"""


class Tree:

    def __init__(self, node):
        self._root = node

    """
    The ID3 algorithm itself is a recursive algorithm.
    The purpose of it is to construct a tree that given a record will sort it to a leaf -
    the leaf contains the final classification of the record.

    The heart of the algorithm is the entropy - a way of telling how much randomness 
    there is in a data set, with it - the ID3 can decide in what way to construct the tree
    so in the passage from one node to the next the population will be split in the most
    significant way.
    """
    def id3(self, node, population):
        split_attr = []
        MIN_POPULATION = 5

        if len(population) < MIN_POPULATION or self.same_survival(population):
            node.set_leaf(True)
            node.set_name(node.most_common_result())
            return

        else:

            best_split = node.best_split()
            node.set_name(best_split)

            new_attr = copy.deepcopy(node.get_attr())

            for attr in new_attr:
                if attr.get_name() == best_split:
                    split_attr = attr
                    new_attr.remove(attr)

            for option in split_attr.get_options():
                new_population = []
                for passenger in node.get_passengers():
                    """is the passenger's "best split" attribute's
                       value belongs to the range in option"""
                    if node.passenger_attr_option_check(passenger, best_split, option):
                        new_population.append(passenger)

                new_node = Node.Node(None, node, new_population, [], new_attr, option)
                node.add_son(new_node)

            for son in node.get_sons():
                self.id3(son, new_population)

    """
    Checks if a node has a population with the same classification -
    in that case - no splitting is needed.
    """
    def same_survival(self, population=[]):
        false_in_pop = False
        true_in_pop = True

        for person in population:
            if person.get_survival() == 0:  # 0 is false
                false_in_pop = True
            else:
                true_in_pop = True

            if false_in_pop and true_in_pop:    # the survival is not the same for all
                return False
        return True

    """
    Now that the tree is already constructed we are ready to classify an unseen 
    record, with this recursive function the new record will be sent to the correct leaf.
    """
    def find_survival(self, node, passenger):
        SURVIVAL = 1
        DEATH = 0

        attr_name = node.get_name()
        if attr_name == "survive":
            return SURVIVAL
        elif attr_name == "death":
            return DEATH

        for son in node.get_sons():
            if son.passenger_attr_option_check(passenger, attr_name, son.get_option()):
                return self.find_survival(son, passenger)

