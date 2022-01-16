"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.
Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 
We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.
NOTE: This challenge is EXTREMELY hard and we are not expecting anyone to pass all
our tests. In fact, we are not expecting many people to even attempt this.
For complete transparency, this is worth more than the easy challenge. 
A good solution is favourable but does not guarantee a spot in Projects because
we will also consider many other criteria.
"""
from calendar import c
import json


# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()



# check if the course is in prerequisite
def check_course(pre, courses_list):
    for course in courses_list:
            if course in pre:
                return True
    return False



# return the number of course in unit of credit case
def num_course_req(pre):

    # find the string in front of unit
    # which state the number of units required
    if pre.index("UNITS") <= 5:
        num_course = int(pre[0:pre.index("UNITS")])
    else:
        num_course = int(pre[pre.index("UNITS") - 4:pre.index("UNITS")])

    num_course = num_course / 6

    return num_course



# count the number of satisfy (prerequisite) course in courses list
def course_num_enought(check_string, num_course, courses_list):

    count = 0
    for course in courses_list:
        # course satisfy the specific requirement
        if check_string in course:
            count += 1
    if count >= num_course:
        return True
    else:
        return False



# check if part of prerequisite that contains "AND" is
# true or false
def separate_by_and(pre, courses_list):
    index = pre.index("AND")

    # separate the string into 2 part (separator = "AND")
    part1 = pre[0: index]
    part2 = pre[index + 3: ] 

    # delcare result of part1 and part2 to 100 first
    res1,res2 = 100, 100

    # if contains "OR" or "UNITS" destruct further
    if "OR" in part1 or "UNITS" in part1:
        res1 = destruct(part1, courses_list)
    else:
        res1 = check_course(part1, courses_list)
        
    if "OR" in part1 or "UNITS" in part2:
        res2 = destruct(part2, courses_list)
    else:
        res2 = check_course(part2, courses_list)

    # if both part1 and part2 of the prerequisite is true return true
    if (res1 and res2) and (res1 != 100 and res2 != 100):
        return True
    else:
        return False



def check_unit_credit_general(pre, courses_list):

    # if units of credit required in COMP course 
    # (exclude the case when prerequisite contains completion)
    if "COMP" in pre and "COMPLETION" not in pre:

        # if it specify the levels
        if "LEVEL" in pre:

            # find the level required
            level = int(pre[pre.index("LEVEL") + 5 : pre.index("LEVEL") + 8])

            # restrict the level of comp
            check_string = "COMP" + str(level)

            # find the number of course required
            num_course = num_course_req(pre)

            return course_num_enought(check_string, num_course, courses_list)
        else:
            check_string = "COMP"
            # find the number of course required
            num_course = num_course_req(pre)

            return course_num_enought(check_string, num_course, courses_list)

    # when it's unit of credit of all course
    else:
            # find the number of course required
            num_course = num_course_req(pre)

            if len(courses_list) >= num_course:
                return True
            else: 
                return False



# check unit of credit (when given specific list of course)
def check_unit_credit_special(pre, courses_list):
    # find the number of course required
    num_course = num_course_req(pre)

    exists = 0
    for course in courses_list:
        if course in pre:
            exists += 1
        
    if exists >= num_course:
        return True
    else:
        return False



# check result when the brackets at the start
def check_bracket_start(pre, courses_list):
    index = pre.index(")")

    # if the linking word is "or"
    if ((pre.find("OR", index) < pre.find("AND", index)) and \
        pre.find("OR", index) != -1) or pre.find("AND", index) == -1:

        # separate by "or" and destruct further and check the result
        result1 = destruct(pre[1: index + 1], courses_list)
        result2 = destruct(pre[pre.find("OR", index) + 2 :], courses_list)

        if result1 or result2:
            return True
        else: 
            return False

    # if the linking word is "and"
    elif ((pre.find("AND", index) < pre.find("OR", index)) and \
            pre.find("AND", index) != -1) or pre.find("OR", index) == -1:

        # separate by "and" and destruct further and check the result
        result1 = destruct(pre[1: index + 1], courses_list)
        result2 = destruct(pre[pre.find("AND", index) + 3 :], courses_list)

        if result1 and result2:
            return True
        else:
            return False



# check result when the brackets is in the middle
def check_brackets_middle(pre, courses_list):

    index = pre.index("(")

    # if the linking word is "or"
    if pre.rfind("OR", 0, index - 1) > pre.rfind("AND", 0, index - 1):

        # separate by "or" and destruct further and check the result
        result1 = destruct(pre[0: pre.rfind("OR", 0, index - 1)], courses_list)
        result2 = destruct(pre[index + 1: ], courses_list)

        if result1 or result2:
            return True
        else: 
            return False

    # if the linking word is "and"
    elif pre.rfind("AND", 0, index - 1) > pre.rfind("OR", 0, index - 1):

        # separate by "and" and destruct further and check the result
        result1 = destruct(pre[0: pre.rfind("AND", 0, index - 1)], courses_list)
        result2 = destruct(pre[index + 1: ], courses_list)

        if result1 and result2:
            return True
        else:
            return False



# destruct the prerequisite
def destruct(pre, courses_list):

    # if only consist of or || only have 1 presequite course
    if "AND" not in pre and "(" not in pre and "UNITS" not in pre:
        return check_course(pre, courses_list)

    # if contains AND but does not contain brackets
    if "(" not in pre and "AND" in pre:
        return separate_by_and(pre, courses_list)
    
    # if prerequisite contains units of credit but not brackets
    if "UNITS" in pre and "(" not in pre:
        return check_unit_credit_general(pre, courses_list)
        
    # cases when ask credit of unit in a specific list of courses
    if "(" in pre and pre.find("IN", 0, pre.index("(")) != -1 and "AND" not in pre:
        
        return check_unit_credit_special(pre, courses_list)

    # open the brackets
    elif "(" in pre:
        # remove the space at the start and end 
        pre = pre.strip()

        # when the prerequisite contains a simple brackets destruct as normal
        if pre.index("(") == 0 and pre[-1] == ")" and pre.count(")") == 1:
            destruct(pre[1:-1], courses_list)
        
        # when the prerequisite contains brackets at the start
        elif pre.index("(") == 0:
            return check_bracket_start(pre, courses_list)
        
        # when the brackets is in the middle or end of prerequisite 
        else:
            return check_brackets_middle(pre, courses_list)

            

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json
    You can assume all courses are worth 6 units of credit
    """

    # get the prerequisite for the target course
    pre = CONDITIONS[target_course]
    pre = pre.upper()

    # if prerequisite is empty return true
    if not pre:
        return True
    # if the prerequisite is not empty but the 
    # course list is empty return false
    elif courses_list == []:
        return False
    elif pre.isdigit():
        # for special cases (comp4952 comp4953) when it contains number only
        for course in courses_list:
            if pre in course and "COMP" in course:
                return True
        return False
    
    # for all other complex prerequisite, separate in simpler terms
    return destruct(pre, courses_list)

