import csv


class DataHandler:
    def __init__(self, csvFilePath: str):
        self.csvData = self.loadFile(csvFilePath)
        
    def loadFile(self, csvFilePath: str) -> list[list[str]]:
        with open(csvFilePath, newline='') as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))  # deduce CSV format and set the reader to use it
            csv_file.seek(0)

            reader = csv.reader(csv_file, dialect)

            data = []

            for index, row in enumerate(reader):
                if (index != 0):  # don't count the header row
                    data.append(row)
        
        return data


_datahandler = DataHandler('/home/r34_runna/Documents/projects/Prizeversity-Bits-Calculation-Integration/data/submission_done.csv')
