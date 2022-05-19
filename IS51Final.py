"""
This program opens a file Final.txt with the grades of students, stores the grades
to an empty list of integers, displays the number of grades,
the average grade, and the percent of grades that are above the average grade.

These are the expectec outcomes
Number of grades: 24 
Average grade: 83.25 
Percentage of grades above average: 54.17%
"""


"""
main
    calculate_percent_above_average

calculate_percent_above_average:
    grades
    open file
    for loop
        append each number to grades list
    close file

    number of grades = length of grades
    average grade = sum of all the grades / number of grades
    
    set above average counter to 0
    for loop in grades:
        if grades[index] > average grade:
            above average counter + above average counter + 1
        
    above average percentage = (above average counter / number of grades) * 100

    print number of grades (24)
    print average grade (83.25)
    print percentage of grades before average (54.17)

call main
"""


# This method kickstarts the program
# Calls for the calculator function
def main():
    calculate_percent_above_average("Final.txt")

# This method reads the text file, store the grades in a list
# Once it has the list, it calculates the number of grades, the average grade, and the percentage of numbers avobe the average
def calculate_percent_above_average(text_file):
    grades = []
    infile = open(text_file, 'r')
    for grade in infile:
        grades.append(int(grade))
    infile.close()

    number_of_grades = len(grades)
    average_grade = float(sum(grades) / len(grades))
    
    above_average_counter = 0
    for i in grades:
        if i > average_grade:
            above_average_counter += 1
        
    above_average_percentage = round((above_average_counter / number_of_grades) * 100, 2)

    print("Number of grades:", number_of_grades)
    print("Average grade:", average_grade)
    print("Percentage of grades before average:", above_average_percentage, "%")

main()