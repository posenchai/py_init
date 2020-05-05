import numpy as np

# str_input_name = None
# float_input_grade = None
dic_STUDENTS = {}
lst_highest_grade = [-9999, "name1", "name2"]
lst_lowest_grade = [9999, "name1", "name2"]
dic_GRADE_CATE = {
    "A": {},  # up_90
    "B": {},  # 80_90
    "C": {},  # 70_80
    "D": {},  # 60_70
    "E": {},  # lower_60
}

dic_PRT_CATE_STR = {
    "A": "90分以上",  # up_90
    "B": "80~90分",  # 80_90
    "C": "70~80分",  # 70_80
    "D": "60~70分",  # 60_70
    "E": "60分以下(不及格)",  # lower_60
}

while True:

    str_input_name = input("請輸入姓名: ")
    if str_input_name == "q":
        break
    float_input_grade = float(input("  >> 請輸入成績(數值): "))
    dic_STUDENTS.update({str_input_name: float_input_grade})

    if float_input_grade > lst_highest_grade[0]:
        lst_highest_grade = [float_input_grade, str_input_name]
    elif float_input_grade == lst_highest_grade[0]:
        lst_highest_grade.append(str_input_name)

    if float_input_grade < lst_lowest_grade[0]:
        lst_lowest_grade = [float_input_grade, str_input_name]

    elif float_input_grade == lst_lowest_grade[0]:
        lst_lowest_grade.append(str_input_name)

print("1. 成績最高的分數: ", lst_highest_grade[0], "學生姓名: ", lst_highest_grade[1:])
print("2. 成績最低的分數: ", lst_lowest_grade[0], "學生姓名: ", lst_lowest_grade[1:])
print("3. 平均分數: ", np.mean([g for g in dic_STUDENTS.values()]))

for per_name, per_grade in dic_STUDENTS.items():
    if per_grade >= 90:
        dic_GRADE_CATE["A"].update({per_name: per_grade})

    elif per_grade >= 80:
        dic_GRADE_CATE["B"].update({per_name: per_grade})

    elif per_grade >= 70:
        dic_GRADE_CATE["C"].update({per_name: per_grade})

    elif per_grade >= 60:
        dic_GRADE_CATE["D"].update({per_name: per_grade})

    else:
        dic_GRADE_CATE["E"].update({per_name: per_grade})

print("4. 分數統計: ")
for grade_cate, per_cate_students in dic_GRADE_CATE.items():
    print(dic_PRT_CATE_STR[grade_cate], "人數: ", len(per_cate_students))
