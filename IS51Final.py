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