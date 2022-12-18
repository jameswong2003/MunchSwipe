import csv

class CSV_Retrieve:
    def __init__(self, file) -> None:
        self.file = file

    def add_restaurant(self, restaurant_info=None):
        with open(self.file, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(restaurant_info)