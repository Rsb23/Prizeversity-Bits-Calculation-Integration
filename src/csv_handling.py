import csv
from datetime import datetime, timedelta, timezone


class DataHandler:
    def __init__(self, csvFilePath: str):
        self.csvData = self.loadFile(csvFilePath)
        self.determineFirstTenSubmissions(self.csvData)
        
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

    def determineFirstTenSubmissions(self, csvData: list[list[str]]) -> list[str]:
        firstTenStudents = []

        for row in csvData:
            # convert datetime column to datetime obj format for comparison
            pass
            
        # convert month, day, hour str datetime parts to be zero-padded for parsing with strptime
        splitDTStr = "2025-11-22, 11:23:15 p.m.".split(', ')
        
        dateStr = splitDTStr[0]
        newDateStr = ""
        
        timeStr = splitDTStr[1]
        newTimeStr = ""

        # converting month and day to be zero-padded
        for index, subDateStr in enumerate(dateStr.split('-')):
            if (index != 0):  # if year skip as year is the first index from the split
                if (len(subDateStr) != 2):  # check if already two digits long
                    subDateStr.zfill(2)  # zfill takes total length including what number(s) are already there, so we input length of two
                
                newDateStr += '-' + subDateStr
            else:
                newDateStr += subDateStr
                

        
        # next is converting hour to be zero-padded BUT we need to get rid of (convert) a.m. and p.m.
        splitTimeStr = timeStr.split(' ')  # 11:23:15 p.m. -> 11:23:15 + p.m.
        numbersTimeStr = splitTimeStr[0]
        newNumbersTimeStr = ""
        ampmTimeStr = splitTimeStr[1]
        newAmpmTimeStr = ampmTimeStr.replace('.', '')
        
        for index, subNumbersTimeStr in enumerate(numbersTimeStr.split(':')): 
            if (index == 0):  # we only care about making the hour zero-padded because minutes and seconds natively are already zero-padded
                subNumbersTimeStr.zfill(2)
                newNumbersTimeStr += subNumbersTimeStr
            else:
                newNumbersTimeStr += ':' + subNumbersTimeStr
        
        # combine everything we formatted before for parsing by strptime
        newDateTimeStr = ', '.join([newDateStr, ' '.join([newNumbersTimeStr, newAmpmTimeStr])])

        # convert str datetime to datetime obj with strptime
        baseDateTime = datetime.strptime(newDateTimeStr, "%Y-%m-%d, %I:%M:%S %p")

        # add timezone to datetime obj we just created with strptime
        estTZ = timezone(-timedelta(hours=5))  # EST is 5 hours behind UTC
        baseDateTime = baseDateTime.astimezone(estTZ)
        
        # calculate difference between datetime objs
        toCompareDateTime = datetime(2025, 11, 25, 10, 15, 15, 0, estTZ)
        diff = toCompareDateTime > baseDateTime

        print(diff)

_datahandler = DataHandler('/home/r34_runna/Documents/projects/Prizeversity-Bits-Calculation-Integration/data/submission_done.csv')
