import csv

class GetData:

    def __init__(self, name):
        self.name = name

    def get_data_into_dict(self):

        with open(self.name, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print('file open')
            self._print_data(csv_reader)

    def _print_data(self, data):
        for row in data:
            print(row)