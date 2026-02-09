import csv
import io
from datetime import datetime, timedelta, timezone


class DataHandler:
    def __init__(self, csv1: str, csv2: str, decodeFiles: bool = True):
        
        if (decodeFiles):
            self.csvData1 = self.loadFile(csv1)
            self.csvData2 = self.loadFile(csv2)
        else:
            self.csvData1 = csv1
            self.csvData2 = csv2
        
        self.estTZ = timezone(-timedelta(hours=5))  # EST is 5 hours behind UTC
        self.dueDate1DT = datetime(2025, 11, 25, 0, 0, 0, 0, self.estTZ)
        self.dueDate2DT = datetime(2025, 12, 1, 0, 0, 0, 0, self.estTZ)

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

    def getListOfStudents(self):
        return [row[1] for row in self.csvData1]

    def createOutputFile(self, nSubmissions: bool = False, n: int = 5, submissionStreak: bool = False, streakWeeks: list[int] = [], dualComp: bool = False) -> io.StringIO:
        if nSubmissions:
            firstTenStudents = self.determineFirstNSubmissions(self.csvData1, 10, self.dueDate1DT)
            firstTenStudents2 = self.determineFirstNSubmissions(self.csvData2, 10, self.dueDate2DT)
        
        if submissionStreak:
           pass 

        if dualComp:
            dualCompStudents = self.getDualCompletionStudents(self.csvData1, self.csvData2)
        
        # write data
        csv_buff = io.StringIO()
        csv_writer = csv.writer(csv_buff, delimiter=',')

        for student in self.getListOfStudents():
            rowToWrite = []
            rowToWrite.append(student)

            points = 0

            if (student in firstTenStudents):
                points += 5
            if (student in firstTenStudents2):
                points += 5
            
            # TODO: submissionStreak points

            if (student in dualCompStudents):
                points += 15
            
            rowToWrite.append(points)
            
            csv_writer.writerow(rowToWrite)
        
        print(csv_buff)
        return csv_buff

    def convertCSVStrToDT(self, csvDateTime: str) -> datetime:
        # convert month, day, hour str datetime parts to be zero-padded for parsing with strptime
        splitDTStr = csvDateTime.split(', ')
        
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
        baseDateTime = baseDateTime.astimezone(self.estTZ)

        return baseDateTime

    def didStudentPassTests(self, csvRow: list[str]) -> bool:
        # "1 passed of 1"
        # parse Test Result column
        splitTestResult = csvRow[2].split(' ')

        if splitTestResult[0] == splitTestResult[3]:
            return True
        else:
            return False

    def calcTimeBetweenSubmissionDueDate(self, submissionDT: datetime, dueDateDT: datetime) -> timedelta | int:
        # determine if submissions occur after due date, helper func
        if (submissionDT < dueDateDT):
            return dueDateDT - submissionDT
        else:  # if the student submitted after due date
            return -1

    def didStudentSubmitOnTime(self, submissionDT: datetime, dueDateDT: datetime) -> bool:
        if (submissionDT < dueDateDT):
            return True
        else:
            return False

    def determineFirstNSubmissions(self, csvData: list[list[str]], n: int, dueDate: datetime) -> list[str]:
        allStudents = [[]]
        cleanedCsvData = [[]]

        # clean csvData to make sure we are only including students who have passed all test cases and submitted on time
        cleanedCsvData = self.determineCompletedStudents(csvData, dueDate)

        # populate allStudents with list of all student names and their timedelta due date datetime - submission datetime, (largest value will be considered more early)
        for row in cleanedCsvData:
            pass
            # allStudents.append([row[1], self.calcTimeBetweenSubmissionDueDate(self.convertCSVStrToDT(cleanedCsvData[4]), dueDate)])

        allStudents.pop(0)  # remove first index which is empty (header)

        sortedStudents = sorted(allStudents, key=lambda x: x[1], reverse=True)  # sort students by timedelta from due date datetime

        # put N for 10 in list slice below
        firstNStudents = [i[0] for i in sortedStudents[0:n]]  # create list of ten students without datetimes, just names sorted with first being the earliest completion

        return firstNStudents
    
    def determineCompletedStudents(self, csvData: list[list[str]], dueDateDT: datetime) -> list[list[str]]:
        completedStudents = []

        for row in csvData:
            if (self.didStudentPassTests(row) and self.didStudentSubmitOnTime(self.convertCSVStrToDT(row[4]), dueDateDT)):
                completedStudents.append(row)
        
        return completedStudents

    def getDualCompletionStudents(self, csvData1: list[list[str]], csvData2: list[list[str]]) -> list[str]:
        # Helper func for determining which students completed both DD versions for the week
        # create list of names for each csv file as there is one csv for each part of the DD
        # determine which names appear twice, append to return list

        # firstAssignmentNames = self.determineCompletedStudents(csvData1)
        # secondAssignmentNames = self.determineCompletedStudents(csvData2)

        completedBothNames = []

        # now compare which names are in both
        if (len(firstAssignmentNames) > len(secondAssignmentNames)):
            for name in firstAssignmentNames:
                if secondAssignmentNames.__contains__(name):
                    completedBothNames.append(name)
        else:
            for name in secondAssignmentNames:
                if firstAssignmentNames.__contains__(name):
                    completedBothNames.append(name)
        
        return completedBothNames
    
    def getStreakContinuationStudents(self, allCsvData: list[list[list[str]]]) -> list[str] | int:
        # TODO
        return -1


_datahandler = DataHandler('/home/r34_runna/Documents/projects/Prizeversity-Bits-Calculation-Integration/data/submission_done.csv', '/home/r34_runna/Documents/projects/Prizeversity-Bits-Calculation-Integration/data/submission_done2.csv')
_datahandler.createOutputFile(True, 5, False, [], True)
