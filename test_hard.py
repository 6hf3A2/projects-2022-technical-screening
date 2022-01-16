"""
====================TESTS====================
You may add your own tests if you would like. We will run our much more extensive
hidden tests on your submission.
"""
from re import T
from hard import is_unlocked

def test_empty():
    assert is_unlocked([], "COMP1511") == True
    assert is_unlocked([], "COMP9301") == False

def test_single():
    assert is_unlocked(["MATH1081"], "COMP3153") == True
    assert is_unlocked(["ELEC2141"], "COMP3211") == True
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531"], "COMP3153") == False

def test_compound():
    assert is_unlocked(["MATH1081", "COMP1511"], "COMP2111") == True
    assert is_unlocked(["COMP1521", "COMP2521"], "COMP3151") == True
    assert is_unlocked(["COMP1917", "DPST1092"], "COMP3151") == False

def test_simple_uoc():
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521"], "COMP4161") == True
    assert is_unlocked(["COMP1511", "COMP1521"], "COMP4161") == False

def test_annoying_uoc():
    assert is_unlocked(["COMP9417", "COMP9418", "COMP9447"], "COMP9491") == True
    assert is_unlocked(["COMP6441"], "COMP9302") == False
    assert is_unlocked(["COMP6441", "COMP64443", "COMP6843", "COMP6445"], "COMP9302") == True
    assert is_unlocked(["COMP1234", "COMP5634", "COMP4834"], "COMP9491") == False
    assert is_unlocked(["COMP3901"], "COMP3902") == False
    assert is_unlocked(["COMP3901", "COMP6441", "COMP6443"], "COMP3902") == False
    assert is_unlocked(["COMP3901", "COMP3441", "COMP3443"], "COMP3902") == True

def test_cross_discipline():
    assert is_unlocked(["COMP1911", "MTRN2500"], "COMP2121") == True
    assert is_unlocked(["COMP1521"], "COMP2121") == True

def test_1511():
    assert is_unlocked(["MATH1081", "COMP1511"], "COMP1511") == True
    assert is_unlocked([], "COMP1511") == True

def test_1521():
    assert is_unlocked([], "COMP1521") == False
    assert is_unlocked(["COMP1511"], "COMP1521") == True
    assert is_unlocked(["DPST1091", "COMP1511"], "COMP1521") == True
    assert is_unlocked(["DPST1091"], "COMP1521") == True
    assert is_unlocked(["COMP1911"], "COMP1521") == True
    assert is_unlocked(["COMP1917"], "COMP1521") == True
    assert is_unlocked(["DPST1091", "COMP1511", "COMP1911", "COMP1917"], "COMP1521") == True
    assert is_unlocked(["DPST1092"], "COMP1521") == False
    assert is_unlocked(["COMP1531"], "COMP1521") == False
    assert is_unlocked(["DPST1092", "COMP1511"], "COMP1521") == True

def test_1531():
    assert is_unlocked([], "COMP1531") == False
    assert is_unlocked(["COMP1511"], "COMP1531") == True
    assert is_unlocked(["DPST1091", "COMP1511"], "COMP1531") == True
    assert is_unlocked(["DPST1091"], "COMP1531") == True
    assert is_unlocked(["COMP1921"], "COMP1531") == True
    assert is_unlocked(["COMP1911"], "COMP1531") == False
    assert is_unlocked(["COMP1917"], "COMP1531") == True
    assert is_unlocked(["DPST1091", "COMP1511", "COMP1911", "COMP1917"], "COMP1531") == True
    assert is_unlocked(["DPST1091", "COMP1511", "COMP1921", "COMP1917"], "COMP1531") == True

def test_2041():
    assert is_unlocked([], "COMP2041") == False
    assert is_unlocked(["COMP1511"], "COMP2041") == True
    assert is_unlocked(["DPST1091", "COMP1511"], "COMP2041") == True
    assert is_unlocked(["DPST1091"], "COMP2041") == True
    assert is_unlocked(["COMP1921"], "COMP2041") == True
    assert is_unlocked(["COMP1911"], "COMP2041") == False
    assert is_unlocked(["COMP1917"], "COMP2041") == True
    assert is_unlocked(["DPST1091", "COMP1511", "COMP1911", "COMP1917"], "COMP2041") == True
    assert is_unlocked(["DPST1091", "COMP1511", "COMP1921", "COMP1917"], "COMP2041") == True

# MATH1081 AND    (COMP1511 OR DPST1091 OR COMP1917 OR COMP1921)
def test_2111():
    assert is_unlocked([], "COMP2111") == False
    assert is_unlocked(["COMP1511"], "COMP2111") == False
    assert is_unlocked(["COMP1511", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["DPST1091", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["COMP1917", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["COMP1921", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["COMP1511", "DPST1091","COMP1917","COMP1921", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["COMP1511", "DPST1091","COMP1917","COMP1921", "MATH1024"], "COMP2111") == False
    assert is_unlocked(["COMP1511", "DPST1091","COMP1917","COMP1921"], "COMP2111") == False
    assert is_unlocked(["COMP1511", "DPST1091","COMP1917"], "COMP2111") == False
    assert is_unlocked(["COMP1511", "DPST1091", "MATH1081"], "COMP2111") == True
    assert is_unlocked(["COMP1521", "MATH1081"], "COMP2111") == False

# "COMP1917 OR COMP1921 OR COMP1511 OR DPST1091 OR COMP1521 OR DPST1092 OR (COMP1911 AND MTRN2500)",
def test_2121():
    assert is_unlocked([], "COMP2121") == False
    assert is_unlocked(["COMP1911"], "COMP2121") == False
    assert is_unlocked(["MTRN2500"], "COMP2121") == False
    assert is_unlocked(["COMP1911", "MTRN2500"], "COMP2121") == True
    assert is_unlocked(["COMP1911", "COMP2500"], "COMP2121") == False
    assert is_unlocked(["MTRN2500", "MATH1911"], "COMP2121") == False
    assert is_unlocked(["COMP1911", "COMP1917"], "COMP2121") == True
    assert is_unlocked(["COMP1917"], "COMP2121") == True
    assert is_unlocked(["COMP1921"], "COMP2121") == True
    assert is_unlocked(["COMP1511", "COMP1911"], "COMP2121") == True
    assert is_unlocked(["COMP1511"], "COMP2121") == True
    assert is_unlocked(["COMP1521"], "COMP2121") == True
    assert is_unlocked(["DPST1091", "MTRN2500"], "COMP2121") == True
    assert is_unlocked(["DPST1092"], "COMP2121") == True
    assert is_unlocked(["COMP1917", "COMP1921", "COMP1511", "DPST1091","COMP1521","DPST1092", "COMP1911", "MTRN2500"], "COMP2121") == True

# "COMP2511": "COMP1531 AND (COMP2521 OR COMP1927)"
def test_2511():
    assert is_unlocked([], "COMP2511") == False
    assert is_unlocked(["COMP1531"], "COMP2511") == False
    assert is_unlocked(["COMP2521"], "COMP2511") == False
    assert is_unlocked(["COMP1927"], "COMP2511") == False
    assert is_unlocked(["COMP1927","COMP2521"], "COMP2511") == False
    assert is_unlocked(["COMP1531", "COMP2521"], "COMP2511") == True
    assert is_unlocked(["COMP1531", "COMP1927"], "COMP2511") == True
    assert is_unlocked(["COMP1531", "COMP1927", "COMP2521"], "COMP2511") == True
    assert is_unlocked(["COMP1521"], "COMP2511") == False
    assert is_unlocked(["COMP1531", "MATH2521"], "COMP2511") == False

# "COMP2521": "COMP1511    OR DPST1091 OR COMP1917 OR COMP1921",
def test_2521():
    assert is_unlocked([], "COMP2521") == False
    assert is_unlocked(["COMP1531"], "COMP2521") == False
    assert is_unlocked(["COMP1511"], "COMP2521") == True
    assert is_unlocked(["DPST1091"], "COMP2521") == True
    assert is_unlocked(["COMP1917"], "COMP2521") == True
    assert is_unlocked(["COMP1921"], "COMP2521") == True
    assert is_unlocked(["COMP1921", "COMP1511"], "COMP2521") == True
    assert is_unlocked(["COMP1921", "COMP1521"], "COMP2521") == True
    assert is_unlocked(["COMP1921", "COMP1511", "DPST1091", "COMP1917"], "COMP2521") == True

# 'COMP3121': 'COMP1927 or    COMP2521.', 
def test_3121():
    assert is_unlocked([], "COMP3121") == False
    assert is_unlocked(["COMP1927"], "COMP3121") == True
    assert is_unlocked(["COMP2521"], "COMP3121") == True
    assert is_unlocked(["COMP1511", "COMP2521"], "COMP3121") == True
    assert is_unlocked(["COMP1511"], "COMP3121") == False
    assert is_unlocked(["COMP1927","COMP2521"], "COMP3121") == True

# 'COMP3131': 'COMP2511 or COMP2911', 
def test_3131():
    assert is_unlocked([], "COMP3131") == False
    assert is_unlocked(["COMP2511"], "COMP3131") == True
    assert is_unlocked(["COMP2911"], "COMP3131") == True
    assert is_unlocked(["COMP2911", "COMP2511"], "COMP3131") == True
    assert is_unlocked(["COMP1511"], "COMP3131") == False
    assert is_unlocked(["COMP1511","COMP2511"], "COMP3131") == True


# 'COMP3141': 'COMP1927 or COMP2521.'
def test_3141():
    assert is_unlocked([], "COMP3141") == False
    assert is_unlocked(["COMP2521"], "COMP3141") == True
    assert is_unlocked(["COMP1927"], "COMP3141") == True
    assert is_unlocked(["COMP1927", "COMP2521"], "COMP3141") == True
    assert is_unlocked(["COMP1511"], "COMP3141") == False
    assert is_unlocked(["COMP1511","COMP2521"], "COMP3141") == True

# 'COMP3151': 'COMP1927    OR ((COMP1521 or DPST1092) AND COMP2521)', 
def test_3151():
    assert is_unlocked([], "COMP3151") == False
    assert is_unlocked(["COMP1927"], "COMP3151") == True
    assert is_unlocked(["COMP1521", "COMP2521"], "COMP3151") == True
    assert is_unlocked(["DPST1092", "COMP2521"], "COMP3151") == True
    assert is_unlocked(["COMP1521", "DPSR1092"], "COMP3151") == False
    assert is_unlocked(["COMP2521"], "COMP3151") == False
    assert is_unlocked(["COMP1927", "COMP1521","DPST1092","COMP2521"], "COMP3151") == True

# 'COMP3153': 'MATH1081', 
def test_3153():
    assert is_unlocked([], "COMP3153") == False
    assert is_unlocked(["MATH1081"], "COMP3153") == True

# 'COMP3161': 'COMP2521 or COMP1927', 
def test_3161():
    assert is_unlocked([], "COMP3161") == False
    assert is_unlocked(["COMP2521"], "COMP3161") == True
    assert is_unlocked(["COMP1927"], "COMP3161") == True
    assert is_unlocked(["COMP2521", "COMP1927"], "COMP3161") == True
    assert is_unlocked(["MATH2521"], "COMP3161") == False
    assert is_unlocked(["COMP1521"], "COMP3161") == False

# 'COMP3211': 'COMP3222 or ELEC2141', 
def test_3211():
    assert is_unlocked([], "COMP3211") == False
    assert is_unlocked(["COMP3222"], "COMP3211") == True
    assert is_unlocked(["ELEC2141"], "COMP3211") == True
    assert is_unlocked(["COMP3222", "ELEC2141"], "COMP3211") == True
    assert is_unlocked(["MATH3222"], "COMP3211") == False
    assert is_unlocked(["COMP1521"], "COMP3211") == False

#'COMP3900': 'COMP1531 and (COMP2521 or COMP1927) and 102 units of credit', 
def test_3900():
    assert is_unlocked([], "COMP3900") == False
    assert is_unlocked(["COMP1531"], "COMP3900") == False
    assert is_unlocked(["COMP2521"], "COMP3900") == False
    assert is_unlocked(["COMP1927"], "COMP3900") == False
    assert is_unlocked(["COMP1511"], "COMP3900") == False
    assert is_unlocked(["COMP1531", "COMP2521"], "COMP3900") == False
    assert is_unlocked(["COMP1531", "COMP1927"], "COMP3900") == False
    assert is_unlocked(["COMP1531", "COMP1927", "COMP2521", "COMP1511", "COMP1521", "COMP1531", "MATH1141", \
                        "MATH1241", "MATH1081", "MATH2011", "MATH2521", "COMP2511", "COMP3331", "COMP3311", \
                        "COMP3231", "MATH3222", "ELEC2141"], "COMP3900") == True

    assert is_unlocked(["COMP1531", "COMP1927", "COMP3161", "COMP1511", "COMP1521", "COMP1531", \
                        "MATH1141", "MATH1241", "MATH1081", "MATH2011", "MATH2521", "COMP2511", \
                        "COMP3331", "COMP3311", "COMP3231", "MATH3222", "ELEC2141"], "COMP3900") == True
    
    assert is_unlocked(["COMP1531", "COMP3161", "COMP2521", "COMP1511", "COMP1521", "COMP1531", \
                        "MATH1141", "MATH1241", "MATH1081", "MATH2011", "MATH2521", "COMP2511", \
                        "COMP3331", "COMP3311", "COMP3231", "MATH3222", "ELEC2141"], "COMP3900") == True

# 'COMP3901': 'Prerequisite: 12 units of credit in  level 1 COMP courses and 18 units of credit in level 2 COMP courses', 
def test_3901():
    assert is_unlocked([], "COMP3901") == False
    assert is_unlocked(["COMP1511", "COMP1531"], "COMP3901") == False
    assert is_unlocked(["COMP1511"], "COMP3901") == False
    assert is_unlocked(["COMP2511"], "COMP3901") == False
    assert is_unlocked(["COMP2511", "COMP2521"], "COMP3901") == False
    assert is_unlocked(["COMP2521", "COMP2511", "COMP2121"], "COMP3901") == False
    assert is_unlocked(["COMP1511", "COMP1531", "COMP2521", "COMP2511"], "COMP3901") == False
    assert is_unlocked(["COMP1511","COMP2521", "COMP2511"], "COMP3901") == False
    assert is_unlocked(["COMP1511", "COMP2521", "COMP2511", "COMP2111"], "COMP3901") == False
    assert is_unlocked(["COMP1511", "COMP1531", "COMP2521", "COMP2511", "COMP2111"], "COMP3901") == True
    assert is_unlocked(["COMP1511", "COMP1531", "COMP3900", "COMP2511", "COMP2521"], "COMP3901") == False
    assert is_unlocked(["COMP1521", "COMP1531", "COMP2521", "COMP2511", "COMP2121"], "COMP3901") == True
    assert is_unlocked(["COMP1521", "COMP1531", "COMP2521", "COMP2511", "COMP2121", "COMP2111"], "COMP3901") == True
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521", "COMP2511", "COMP2121"], "COMP3901") == True


# 'COMP3902': 'Prerequisite: COMP3901 and 12 units of credit in level 3 COMP courses', 
def test_3902():
    assert is_unlocked([], "COMP3902") == False
    assert is_unlocked(["COMP3901"], "COMP3902") == False
    assert is_unlocked(["COMP3900"], "COMP3902") == False
    assert is_unlocked(["COMP3900", "COMP3211"], "COMP3902") == False
    assert is_unlocked(["COMP3901", "COMP3901"], "COMP3902") == True
    assert is_unlocked(["COMP3901", "COMP3900", "COMP3211"], "COMP3902") == True
    assert is_unlocked(["COMP3901", "COMP2511", "COMP2521"], "COMP3902") == False


# 'COMP4121': 'COMP3121 or   COMP3821', 
def test_4121():
    assert is_unlocked([], "COMP4121") == False
    assert is_unlocked(["MATH3121", "MATH3821"], "COMP4121") == False
    assert is_unlocked(["COMP3121"], "COMP4121") == True
    assert is_unlocked(["COMP3121", "COMP3821"], "COMP4121") == True
    assert is_unlocked(["COMP3821"], "COMP4121") == True

# 'COMP4128': 'Prerequisite: COMP3821 or (COMP3121 and 12 units of credit in level 3 COMP courses)', 
def test_4128():
    assert is_unlocked([], "COMP4128") == False
    assert is_unlocked(["COMP3121"], "COMP4128") == False
    assert is_unlocked(["COMP3900"], "COMP4128") == False
    assert is_unlocked(["COMP3900", "COMP3901"], "COMP4128") == False
    assert is_unlocked(["COMP3821"], "COMP4128") == True
    assert is_unlocked(["COMP3121", "COMP3900"], "COMP4128") == True
    assert is_unlocked(["COMP3121", "COMP3900", "COMP3901"], "COMP4128") == True
    assert is_unlocked(["COMP3821", "COMP3121", "COMP3900", "COMP3901"], "COMP4128") == True

# 'COMP4141': 'Pre-requisite: MATH1081 and (COMP1927 or COMP2521)', 
def test_4141():
    assert is_unlocked([], "COMP4141") == False
    assert is_unlocked(["MATH1081"], "COMP4141") == False
    assert is_unlocked(["COMP1927"], "COMP4141") == False
    assert is_unlocked(["COMP2521"], "COMP4141") == False
    assert is_unlocked(["COMP1927", "COMP2521"], "COMP4141") == False
    assert is_unlocked(["MATH1081", "COMP2521"], "COMP4141") == True
    assert is_unlocked(["MATH1081", "COMP1927"], "COMP4141") == True
    assert is_unlocked(["MATH1081", "COMP2521", "COMP1927"], "COMP4141") == True


# 'COMP4161': 'Completion  of 18 units of credit', 
def test_4161():
    assert is_unlocked([], "COMP4161") == False
    assert is_unlocked(["COMP1511"], "COMP4161") == False
    assert is_unlocked(["COMP1511", "COMP1521"], "COMP4161") == False
    assert is_unlocked(["MATH1141", "MATH1241"], "COMP4161") == False
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531"], "COMP4161") == True
    assert is_unlocked(["COMP1521", "COMP2521", "COMP3900"], "COMP4161") == True
    assert is_unlocked(["MATH1141", "COMP2521", "COMP1521"], "COMP4161") == True
    assert is_unlocked(["MATH1141", "MATH1241", "MATH2521"], "COMP4161") == True


# 'COMP4336': 'Prerequisite: COMP3331.', 
def test_4336():
    assert is_unlocked([], "COMP4336") == False
    assert is_unlocked(["MATH3331"], "COMP4336") == False
    assert is_unlocked(["COMP3331"], "COMP4336") == True
    assert is_unlocked(["COMP3311"], "COMP4336") == False
    assert is_unlocked(["COMP3331", "COMP3311"], "COMP4336") == True

# 'COMP4418': 'Pre-req: COMP3411', 
def test_4418():
    assert is_unlocked([], "COMP4418") == False
    assert is_unlocked(["MATH3411"], "COMP4418") == False
    assert is_unlocked(["COMP3411"], "COMP4418") == True
    assert is_unlocked(["COMP3331"], "COMP4418") == False
    assert is_unlocked(["COMP3411", "COMP3311"], "COMP4418") == True


# 'COMP4601': '(COMP2511 or COMP2911) and completion of 24 units of credit', 
def test_4601():
    assert is_unlocked([], "COMP4601") == False
    assert is_unlocked(["COMP2511"], "COMP4601") == False
    assert is_unlocked(["COMP2911"], "COMP4601") == False
    assert is_unlocked(["COMP2511", "COMP2911"], "COMP4601") == False
    assert is_unlocked(["COMP2521", "COMP1521", "MATH1241", "COMP1531"], "COMP4601") == False
    assert is_unlocked(["COMP2511", "COMP1511", "COMP1521", "COMP1531"], "COMP4601") == True
    assert is_unlocked(["COMP2911", "COMP1511", "COMP1521", "COMP1531"], "COMP4601") == True
    assert is_unlocked(["COMP2511", "COMP2911", "COMP1521", "COMP1531"], "COMP4601") == True
    assert is_unlocked(["COMP2511", "MATH1241", "MATH1141", "MATH1081"], "COMP4601") == True
    assert is_unlocked(["COMP2511", "MATH1241", "MATH1141", "MATH1081", "COMP2911"], "COMP4601") == True

# 'COMP4951': '36 units of credit in COMP courses', 
def test_4951():
    assert is_unlocked([], "COMP4951") == False
    assert is_unlocked(["COMP1511"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1521"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1531", "COMP1521"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521", "COMP2511"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521", "COMP2511", "MATH1241"], "COMP4951") == False
    assert is_unlocked(["MATH1141", "MATH1081", "MATH2601", "MATH2521", "MATH2011", "MATH1241"], "COMP4951") == False
    assert is_unlocked(["COMP1511", "COMP1521", "COMP1531", "COMP2521", "COMP2511", "COMP3900"], "COMP4951") == True

# 'COMP4952': '4951', 
def test_4952():
    assert is_unlocked([], "COMP4952") == False
    assert is_unlocked(["MATH4951"], "COMP4952") == False
    assert is_unlocked(["COMP4951"], "COMP4952") == True
    assert is_unlocked(["COMP1511", "COMP4951"], "COMP4952") == True

# 'COMP4953': '4952', 
def test_4953():
    assert is_unlocked([], "COMP4953") == False
    assert is_unlocked(["MATH4952"], "COMP4953") == False
    assert is_unlocked(["COMP4952"], "COMP4953") == True
    assert is_unlocked(["COMP1511", "COMP4952"], "COMP4953") == True

# 'COMP9301': '12 units of credit in (COMP6443,  COMP6843, COMP6445, COMP6845, COMP6447)', 
def test_9301():
    assert is_unlocked([], "COMP9301") == False
    assert is_unlocked(["COMP1511"], "COMP9301") == False
    assert is_unlocked(["COMP1511", "COMP2521"], "COMP9301") == False
    assert is_unlocked(["COMP6443"], "COMP9301") == False
    assert is_unlocked(["COMP6843"], "COMP9301") == False
    assert is_unlocked(["COMP6445"], "COMP9301") == False
    assert is_unlocked(["MATH6443"], "COMP9301") == False
    assert is_unlocked(["MATH6443", "MATH6843"], "COMP9301") == False
    assert is_unlocked(["COMP6443", "COMP6843"], "COMP9301") == True
    assert is_unlocked(["COMP6445", "COMP6845"], "COMP9301") == True
    assert is_unlocked(["COMP6443", "COMP6447"], "COMP9301") == True
    assert is_unlocked(["COMP6443", "COMP6843", "COMP6445", "COMP6845", "COMP6447"], "COMP9301") == True


# 'COMP9302': '(COMP6441 OR COMP6841) AND 12 units of credit in (COMP6443, COMP6843, COMP6445, COMP6845, COMP6447)', 
def test_9302():
    assert is_unlocked([], "COMP9302") == False
    assert is_unlocked(["COMP6441"], "COMP9302") == False
    assert is_unlocked(["COMP6841"], "COMP9302") == False
    assert is_unlocked(["COMP6843"], "COMP9302") == False
    assert is_unlocked(["COMP6443"], "COMP9302") == False
    assert is_unlocked(["COMP6443", "COMP6843"], "COMP9302") == False
    assert is_unlocked(["COMP6441", "COMP6443", "COMP6843"], "COMP9302") == True
    assert is_unlocked(["COMP6841", "COMP6445", "COMP6845"], "COMP9302") == True
    assert is_unlocked(["COMP6441", "COMP6841"], "COMP9302") == False
    assert is_unlocked(["COMP6441", "COMP6841", "COMP6447", "COMP6443"], "COMP9302") == True
    assert is_unlocked(["COMP6441", "COMP6841", "COMP6447", "COMP6443", "COMP6843", "COMP6445","COMP6845"], "COMP9302") == True

# 'COMP9417': 'MATH1081 and ((COMP1531 or COMP2041) or (COMP1927 or COMP2521))', 
def test_9417():
    assert is_unlocked([], "COMP9417") == False
    assert is_unlocked(["MATH1081"], "COMP9417") == False
    assert is_unlocked(["COMP1531"], "COMP9417") == False
    assert is_unlocked(["COMP2041"], "COMP9417") == False
    assert is_unlocked(["COMP1927"], "COMP9417") == False
    assert is_unlocked(["COMP2521"], "COMP9417") == False
    assert is_unlocked(["MATH1081", "COMP1531"], "COMP9417") == True
    assert is_unlocked(["MATH1081", "COMP2041"], "COMP9417") == True
    assert is_unlocked(["MATH1081", "COMP1927"], "COMP9417") == True
    assert is_unlocked(["MATH1081", "COMP2521"], "COMP9417") == True
    assert is_unlocked(["COMP2521", "COMP1531"], "COMP9417") == False
    assert is_unlocked(["MATH1081", "COMP1531", "COMP2521", "COMP2041", "COMP1927"], "COMP9417") == True
    assert is_unlocked(["COMP1531", "COMP2521", "COMP2041", "COMP1927"], "COMP9417") == False


# 'COMP9418': 'Prerequisite:  MATH5836 or COMP9417', 
def test_9418():
    assert is_unlocked([], "COMP9418") == False
    assert is_unlocked(["MATH5836"], "COMP9418") == True
    assert is_unlocked(["COMP9417"], "COMP9418") == True
    assert is_unlocked(["COMP9417", "COMP1521"], "COMP9418") == True
    assert is_unlocked(["MATH5836", "COMP9417"], "COMP9418") == True
    assert is_unlocked(["COMP5836", "MATH9417"], "COMP9418") == False

# 'COMP9444': 'Prequisite: COMP1927 or COMP2521 or MTRN3500', 
def test_9444():
    assert is_unlocked([], "COMP9444") == False
    assert is_unlocked(["COMP2521"], "COMP9444") == True
    assert is_unlocked(["MTRN3500"], "COMP9444") == True
    assert is_unlocked(["COMP1927"], "COMP9444") == True
    assert is_unlocked(["COMP2521", "COMP1927"], "COMP9444") == True
    assert is_unlocked(["COMP2521", "COMP1927", "MTRN3500"], "COMP9444") == True
    assert is_unlocked(["COMP1927", "MATH1241"], "COMP9444") == True
     
# 'COMP9447': 'COMP6441 or COMP6841 or COMP3441', 
def test_9447():
    assert is_unlocked([], "COMP9447") == False
    assert is_unlocked(["COMP6441"], "COMP9447") == True
    assert is_unlocked(["COMP6841"], "COMP9447") == True
    assert is_unlocked(["COMP3441"], "COMP9447") == True
    assert is_unlocked(["COMP3441", "COMP6841"], "COMP9447") == True
    assert is_unlocked(["COMP3441", "COMP6841", "COMP6441"], "COMP9447") == True
    assert is_unlocked(["COMP3441", "MATH1241"], "COMP9447") == True

# 'COMP9491': '18 units oc credit in (COMP9417, COMP9418, COMP9444, COMP9447)'}
def test_9491():
    assert is_unlocked([], "COMP9491") == False
    assert is_unlocked(["COMP9417"], "COMP9491") == False
    assert is_unlocked(["COMP9418"], "COMP9491") == False
    assert is_unlocked(["COMP9444"], "COMP9491") == False
    assert is_unlocked(["COMP9477"], "COMP9491") == False
    assert is_unlocked(["COMP9417","COMP9418"], "COMP9491") == False
    assert is_unlocked(["COMP9417","COMP9418", "COMP9444"], "COMP9491") == True
    assert is_unlocked(["COMP9417","COMP9418", "COMP9444", "MATH1241"], "COMP9491") == True
    assert is_unlocked(["COMP9417","COMP9418", "MATH1241"], "COMP9491") == False
