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
        alteredGrade = False
        #Get Overall Comments/Deductions
        overallComments = line["Overall Comments"]
        overallDeductions = line["Overall Deductions"]
        if str(overallComments) != "":
          compiledFeedback += "[Overall] " + overallComments
          alteredGrade = True
        if overallDeductions != "" and float(overallDeductions) < 0:
          compiledGrade += float(overallDeductions)
          alteredGrade = True
          if str(overallComments) == "":
            compiledFeedback += "[Overall] "
          compiledFeedback += "({0} Marks)\n".format(overallDeductions)
        #Get Question Feedback
        for num in range(1, numOfQuestions + 1):
          questionHeader = "[Question {0}]".format(num)
          questionComments = line["Question {0} Comments".format(num)]
          questionDeductions = line["Question {0} Deductions".format(num)]
          if str(questionComments) != "":
            compiledFeedback += questionHeader + " " + questionComments
            alteredGrade = True
          if questionDeductions != "" and float(questionDeductions) < 0:
            compiledGrade += float(questionDeductions)
            alteredGrade = True
            if str(questionComments) == "":
              compiledFeedback += questionHeader
            compiledFeedback += "({0} Marks)\n".format(questionDeductions)
        #Get Bonus Question Feedback
        for bonusNum in range(1, numOfBonus + 1):
          bonusQuestionHeader = " [Bonus Question {0}]".format(bonusNum)
          bonusQuestionComments = line["Bonus {0} Comments".format(bonusNum)]
          bonusQuestionRewards = line["Bonus {0} Grades".format(bonusNum)]
          if str(bonusQuestionComments) != "":
            compiledFeedback += bonusQuestionHeader + " " + bonusQuestionComments
            alteredGrade = True
          if bonusQuestionRewards != "" and float(bonusQuestionRewards) > 0:
            compiledGrade += float(bonusQuestionRewards)
            alteredGrade = True
            compiledFeedback += "(+{0} Marks)\n".format(bonusQuestionRewards)
        if alteredGrade:
          if compiledGrade > maxGrade:
            line["Grade"] = maxGrade
          else:
            line["Grade"] = compiledGrade
        line["Feedback comments"] += (compiledFeedback)
        csvWriter.writerow(line)
      csvOutputFile.close()

if __name__ == "__main__":
  scan_and_write()
