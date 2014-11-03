import csv
import glob
import os

outputDir = "Output"
columnsToInclude = [    "Identifier"
                      , "Full name"
                      , "Status"
                      , "Grade"
                      , "Maximum Grade"
                      , "Feedback comments"]

#Ask how many question fields you would like to add
print "Add Question Columns Tool"
print "This script will add the appropriate columns to the CULearn CSV file for quick formatting"

#Find CSV Files beginning with Grades-
gradeCSVFiles = glob.glob("Grades-*.csv")

if gradeCSVFiles.count <= 0:
  print "No Grade CSV files found in directory\nPress any key to exit"
  raw_input()
else:
  print "How many questions are you grading for this assignment?"
  numOfQuestions = int(raw_input())
  print "Will add {0} Question Columns\n".format(numOfQuestions)

  print "How many bonus questions are in the assignment?"
  numOfBonus = int(raw_input())
  print "Will add {0} Bonus Columns\n".format(numOfBonus)

  for name in gradeCSVFiles:
    print "Analysing grade files"
    csvFileReader = csv.DictReader(open(name ,'rb'), delimiter=",")
    csvFileReader.fieldnames.append("Overall Comments")
    csvFileReader.fieldnames.append("Overall Deductions")
    print "Field Names Before: " + str(csvFileReader.fieldnames)
    for questionNum in range(1,numOfQuestions + 1):
      questionCommentString = "Question {0} Comments".format(questionNum)
      csvFileReader.fieldnames.append(questionCommentString)
      columnsToInclude.append(questionCommentString)
      questionDeductString = "Question {0} Deductions".format(questionNum)
      csvFileReader.fieldnames.append(questionDeductString)
      columnsToInclude.append(questionDeductString)
    for bonusNum in range(1,numOfBonus + 1):
      bonusCommentString = "Bonus {0} Comments".format(bonusNum)
      csvFileReader.fieldnames.append(bonusCommentString)
      columnsToInclude.append(bonusCommentString)
      bonusDeductString = "Bonus {0} Grades".format(bonusNum)
      csvFileReader.fieldnames.append(bonusDeductString)
      columnsToInclude.append(bonusDeductString)
    print "Field Names After: " + str(csvFileReader.fieldnames)
    print "Columns To Include: " + str(columnsToInclude)
    outputFilename = os.path.splitext(name)[0] + "-output.csv"
    outputFile = open(os.path.join(outputDir, outputFilename), "wb")
    csvFileWriter = csv.DictWriter(outputFile, delimiter=",", fieldnames=csvFileReader.fieldnames)
    csvFileWriter.writeheader()
    for row in csvFileReader:
      csvFileWriter.writerow(row) #[col] for col in columnsToInclude)
    outputFile.close()
