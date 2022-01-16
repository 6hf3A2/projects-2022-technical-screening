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
import json


# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()



def destruct(pre, courses_list):

    # if only consist of or || only have 1 presequite course
    if "AND" not in pre and "(" not in pre and "UNITS" not in pre:
        for course in courses_list:
            if course in pre:
                return True

        return False


    if "(" not in pre and "AND" in pre:
        index = pre.index("AND")

        part1 = pre[0: index]
        part2 = pre[index + 3: ] 

        res1,res2 = 100, 100
        if "OR" in part1 or "UNITS" in part1:
            res1 = destruct(part1, courses_list)
        else:
            for course in courses_list:
                if course in part1:
                    res1 = True
                    break
        if "OR" in part1 or "UNITS" in part2:
            res2 = destruct(part2, courses_list)
        else:
            for course in courses_list:
                if course in part2:
                    res2 = True
                    break
        if (res1 and res2) and (res1 != 100 and res2 != 100):
            return True
        else:
            return False
    
    if "UNITS" in pre and "(" not in pre:
        if "COMP" in pre and "COMPLETION" not in pre:
            if "LEVEL" in pre:

                level = int(pre[pre.index("LEVEL") + 5 : pre.index("LEVEL") + 8])
                check_string = "COMP" + str(level)
                num_course = int(pre[pre.index("UNITS") - 4:pre.index("UNITS")])
                num_course = num_course / 6
                count = 0
                for course in courses_list:
                    if check_string in course:
                        count += 1
                if count >= num_course:
                    return True
                else:
                    return False
            else:
                check_string = "COMP"
                if pre.index("UNITS") <= 5:
                    num_course = int(pre[0:pre.index("UNITS")])
                else:
                    num_course = int(pre[pre.index("UNITS") - 4:pre.index("UNITS")])
                num_course = num_course / 6
                count = 0
                for course in courses_list:
                    if check_string in course:
                        count += 1
                if count >= num_course:
                    return True
                else:
                    return False
        else:
                num_course = int(pre[pre.index("UNITS") - 4:pre.index("UNITS")])
                num_course = num_course / 6
                print(courses_list, len(courses_list))
                if len(courses_list) >= num_course:
                    return True
                else: 
                    return False

    if "(" in pre and pre.find("IN", 0, pre.index("(")) != -1 and "AND" not in pre:
        if pre.index("UNITS") <= 5:
            num_course = int(pre[0:pre.index("UNITS")])
        else:
            num_course = int(pre[pre.index("UNITS") - 4:pre.index("UNITS")])
        num_course = num_course / 6
        exists = 0
        for course in courses_list:
            if course in pre:
                exists += 1
            
        if exists >= num_course:
            return True
        else:
            return False


    # open the brackets
    elif "(" in pre:
        pre = pre.lstrip()
        if pre.index("(") == 0 and pre[-1] == ")" and pre.count(")") == 1:
            destruct(pre[1:-1], courses_list)
        elif pre.index("(") == 0:
            index = pre.index(")")
            
            if ((pre.find("OR", index) < pre.find("AND", index)) and pre.find("OR", index) != -1) or pre.find("AND", index) == -1:

                result1 = destruct(pre[1: index + 1], courses_list)
                result2 = destruct(pre[pre.find("OR", index) + 2 :], courses_list)
                if result1 or result2:
                    return True
                else: 
                    return False
            elif ((pre.find("AND", index) < pre.find("OR", index)) and pre.find("AND", index) != -1) or pre.find("OR", index) == -1:
                result1 = destruct(pre[1: index + 1], courses_list)
                result2 = destruct(pre[pre.find("AND", index) + 3 :], courses_list)
                if result1 and result2:
                    return True
                else:
                    return False
        else:
            index = pre.index("(")

            if pre.rfind("OR", 0, index - 1) > pre.rfind("AND", 0, index - 1):
                result1 = destruct(pre[0: pre.rfind("OR", 0, index - 1)], courses_list)
                result2 = destruct(pre[index + 1: ], courses_list)

                if result1 or result2:
                    return True
                else: 
                    return False
            elif pre.rfind("AND", 0, index - 1) > pre.rfind("OR", 0, index - 1):
                result1 = destruct(pre[0: pre.rfind("AND", 0, index - 1)], courses_list)
                result2 = destruct(pre[index + 1: ], courses_list)
                if result1 and result2:
                    return True
                else:
                    return False

            

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json
    You can assume all courses are worth 6 units of credit
    """
    
    
    # get the presequite for the target course
    pre = CONDITIONS[target_course]
    pre = pre.upper()

    # if pre is empty return true
    if not pre:
        return True
    elif courses_list == []:
        return False
    elif pre.isdigit():
        for course in courses_list:
            if pre in course and "COMP" in course:
                return True
        return False
    
    return destruct(pre, courses_list)

