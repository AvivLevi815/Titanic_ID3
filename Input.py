import csv
import Passenger
"""
This class is the gateway to the csv file that is our train set or test set,
the class reads and stores the records as passengers objects.
"""


class Input:

    @staticmethod
    def read_file(url=""):

        ELEMENTS_IN_TRAIN = 13
        ELEMENTS_IN_TEST = 12

        with open(url, newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',',quotechar='|')
            next(reader)  #  skip first line (titles)
            passengers = []
            for row in reader:
                if len(row) == ELEMENTS_IN_TRAIN:    # train based on Kaggle's csv.
                    new_passenger = Passenger.Passenger(row[0], row[6], row[7], row[10], row[2], row[5], row[1])

                elif len(row) == ELEMENTS_IN_TEST:   # test
                    new_passenger = Passenger.Passenger(row[0], row[5], row[6], row[9], row[1], row[4],"")
                passengers.append(new_passenger)

        return passengers


