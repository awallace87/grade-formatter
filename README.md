grade-formatter
===============

CSV Grading Worksheet Formatter for cuLearn

The grade-formatter toolset consists of 2 python scripts:
- AddQuestionFields.py
- GradeFormatter.py

---------------
AddQuestionFields.py:

This script will add the columns/headings for individual question grades and feedback. 
More importantly, the column headings will be named in a format that can be parsed by the GradeFormatter.py script

Upon running the script user will be asked how many "standard" questions are in the assignment?
There is no type checking on the input the user entered, so they should be sure to enter a proper integer.(TODO - Add input checking)

Afterwards, it will ask the user to enter the number of "Bonus" questions in the assignment.
Again, no type checking on input, so the user should be sure to use a proper integer. (TODO - Add input checking)

Upon entering the number of questions, the script will parse all CSV files in it's current directory which begin with "Grades-" (The standard naming prefix for cuLearn downloaded CSV worksheets). It will then create new worksheets with the added headings/columns in the "Output" subdirectory with an additional "-output" on the filename.

Notes for use:
- The script will parse ALL the CSV files with names that begin with "Grades-", and add the fixed question and bonus columns from the single input entry, so be sure to only have the single input CSV file you want parsed in the script directory. (Although, it is not destructive to the original file, so the worst case scenario is that you will have created some useless CSV output files)

Notes on the Output CSV:
- "Question # Deductions" fields should have the marks lost (if at all) entered as negative values (e.g. if a student lost 5 marks on a question, "-5" should be entered in it's Deductions column.
- "Bonus # Grades" fields should have the marks gained (if at all) entered as positive values (e.g. if a student got 2 marks on a specific bonus question, "2" should be entered in it's Grades column.

---------------
GradeFormatter.py:

This script will take a CSV file with the appropriate (AKA AddQuestionFields.py created) columns for individual questions and will compile the feedback and total grades into the "Feedback comments" and "Grade" fields, respectively (allowing them to be quickly uploaded to cuLearn and added into the Gradebook)

Just like the AddQuestionFields.py script, the user will be asked to input the number of standard and bonus questions in the assignment. It is important that this input match the number of columns present in the input CSV. (TODO - Add checks/handling for inaccurate question inputs)

After inputting the correct number of question fields, the script will they parse all the CSV files in the current directory (beginning with "Grades-")and create output CSV files in the "Output" subdirectory. Output files will have a "-formatted" suffix added to the filename.

Output files will have compiled grades and feedback according to the contents of the individual Question Grades and Comments fields.

Notes for Use:
- The script will parse ALL the CSV files with names that begin with "Grades-", and add the fixed question and bonus columns from the single input entry, so be sure to only have the single input CSV file you want parsed in the script directory. (Although, it is not destructive to the original file, so the worst case scenario is that you will have created some useless CSV output files, or caused an error to occur since some assignments will not have an identical number of standard/bonus questions)



