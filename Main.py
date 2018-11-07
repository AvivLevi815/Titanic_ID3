import Node
import Attr
import Tree
import Input

"""
Setting the attributes (features) and their optional values
"""
Attr_Sex = Attr.Attr("Sex", ["male", "female"])
Attr_Fare = Attr.Attr("Fare", [[150, 1000], [90, 150], [30, 90], [15, 30], [0, 15]])
Attr_Age = Attr.Attr("Age", [[70, 200], [60, 70], [50, 60], [35, 50],
                             [26, 35], [19, 26], [16, 19], [6, 16], [0, 6]])
Attr_Sib = Attr.Attr("Sib", [[0, 1], [1, 4], [4, 7], [7, 100]])
Attr_Pclass = Attr.Attr("Pclass", [1, 2, 3])


#  storing the test and train set in the memory
train_passengers = Input.Input.read_file(r"C:\Users\Owner\Desktop\kaggle_train.csv")
test_passengers = Input.Input.read_file(r"C:\Users\Owner\Desktop\kaggle_test.csv")

Root = Node.Node("", None, train_passengers, [], [Attr_Sex, Attr_Fare, Attr_Age, Attr_Pclass, Attr_Sib], "")
currTree = Tree.Tree(Root)

#  construct the tree.
currTree.id3(Root, train_passengers)
count_correct = 0
passenger_amount = len(test_passengers)

#  classify all the records in the train set.
for passenger in test_passengers:
    survival = currTree.find_survival(Root, passenger)
    p_id = '{0:g}'.format(float(passenger.get_id()))
    print(f"{p_id} ,{survival}")

print("done :)")