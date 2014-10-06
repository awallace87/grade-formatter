#Grade Formatter
#Compiles comments and deductions for individual questions
#Outputs formatted final comments and grades
import glob
import os
import sys
import csv

outputDir = "Output"
outputPath = "-formatted.csv"

questionSubstring = "Question"
deductionsFormat = " - Deductions"
commentsSubstring = " - Comments"


def scan_and_write():
  gradeCSVFiles = glob.glob("Grades-*.csv")

  if gradeCSVFiles.count <= 0:
    print "No Grade CSV files found in directory\nPress any key to exit"
    raw_input()
  else:
    print "How many questions are you grading for this assignment?"
    numOfQuestions = int(raw_input())

    print "How many bonus questions are in the assignment?"
    numOfBonus = int(raw_input())

    for name in gradeCSVFiles:
      print name
      csvFileObj = open(name, 'rb')
      reader = csv.DictReader(csvFileObj, delimiter=',')
      outputFilename = os.path.splitext(name)[0] + "-formatted.csv"
      outputPath = os.path.join(outputDir,outputFilename)
      csvOutputFile = open(outputPath, "wb")
      csvWriter = csv.DictWriter(csvOutputFile, delimiter=',' , fieldnames=reader.fieldnames)
      csvWriter.writeheader()
      for line in reader:
        compiledFeedback = ""
        maxGrade = float(line["Maximum Grade"])
        compiledGrade = maxGrade
        for num in range(1, numOfQuestions + 1):
          #try:
          questionHeader = "[Question {0}]".format(num)
          questionComments = line["Question {0} Comments".format(num)]
          questionDeductions = line["Question {0} Deductions".format(num)]
          if str(questionComments) != "" or questionDeductions != "":
            compiledFeedback += questionHeader
            if str(questionComments) != "":
              compiledFeedback += " " + questionComments	
            if questionDeductions != "" and float(questionDeductions) < 0:
              compiledGrade += float(questionDeductions)
              compiledFeedback += " ({0} Marks)".format(questionDeductions)
            compiledFeedback += "\n"				
          #except:
          #  print "Unable to find Question {0} information".format(num)
        for bonusNum in range(1, numOfBonus + 1):
          #try:
          bonusQuestionHeader = "[Bonus Question {0}]".format(bonusNum)
          bonusQuestionComments = line["Bonus {0} Comments".format(bonusNum)]
          bonusQuestionRewards = line["Bonus {0} Grades".format(bonusNum)]
          if str(bonusQuestionComments) != "" or bonusQuestionRewards != "":
            compiledFeedback += bonusQuestionHeader
            if str(bonusQuestionComments) != "":
              compiledFeedback += " " + bonusQuestionComments 
            if bonusQuestionRewards != "" and float(bonusQuestionRewards) > 0:
              compiledGrade += float(bonusQuestionRewards)
              compiledFeedback += " (+{0} Marks)".format(bonusQuestionRewards)
            compiledFeedback += "\n"      
          #except:
          #  print "Unable to find Bonus Question {0} information".format(bonusNum)
        if compiledGrade > maxGrade:
          line["Grade"] = maxGrade
        else:
          line["Grade"] = compiledGrade
        line["Feedback comments"] = (compiledFeedback)
        csvWriter.writerow(line)
      csvOutputFile.close()

if __name__ == "__main__":
  scan_and_write()
