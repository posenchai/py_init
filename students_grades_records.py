import numpy as np

dic_print_string = {
    "A": "90分以上",  # up_90
    "B": "80~90分",  # 80_90
    "C": "70~80分",  # 70_80
    "D": "60~70分",  # 60_70
    "E": "60分以下(不及格)",  # lower_60
}


class Grade_recorder:
    def __init__(self):
        self.str_input_name = None
        self.str_input_grade = None
        self.dic_students = {}  # OrderedDict()
        self._lst_higest_grade = [-9999, "name1", "name2"]
        self._lst_lowest_grade = [9999, "name1", "name2"]
        self._tup_grade_cate = {
            "A": {},  # up_90
            "B": {},  # 80_90
            "C": {},  # 70_80
            "D": {},  # 60_70
            "E": {},  # lower_60
        }
        self.input_name_and_grade()

    def input_name_and_grade(self):
        while True:

            self.str_input_name = input("請輸入姓名: ")
            if self.str_input_name == "q":
                break
            self.str_input_grade = float(input("  >> 請輸入成績: "))

            per_student = {
                self.str_input_name: self.str_input_grade,
            }

            self.dic_students.update(per_student)
            self._update_higest_grade()
            self._update_lowest_grade()

    def _update_higest_grade(self):
        if self.str_input_grade > self._lst_higest_grade[0]:
            self._lst_higest_grade = [self.str_input_grade, self.str_input_name]

        elif self.str_input_grade == self._lst_higest_grade[0]:
            self._lst_higest_grade.append(self.str_input_name)

    def _update_lowest_grade(self):
        if self.str_input_grade < self._lst_lowest_grade[0]:
            self._lst_lowest_grade = [self.str_input_grade, self.str_input_name]

        elif self.str_input_grade == self._lst_lowest_grade[0]:
            self._lst_lowest_grade.append(self.str_input_name)

    def get_higest_grade(self):
        print("成績最高的分數: ", self._lst_higest_grade[0], end=", ")
        print("學生姓名: ", self._lst_higest_grade[1:])

    def get_lowest_grade(self):
        print("成績最低的分數學生: ", self._lst_lowest_grade[0], end=", ")
        print("學生姓名: ", self._lst_lowest_grade[1:])

    def get_mean(self):
        print("平均分數: ", np.mean([g for g in self.dic_students.values()]))

    def _cate_grades(self):
        for per_name, per_grade in self.dic_students.items():
            if per_grade >= 90:
                self._tup_grade_cate["A"].update({per_name: per_grade})

            elif per_grade >= 80:
                self._tup_grade_cate["B"].update({per_name: per_grade})

            elif per_grade >= 70:
                self._tup_grade_cate["C"].update({per_name: per_grade})

            elif per_grade >= 60:
                self._tup_grade_cate["D"].update({per_name: per_grade})

            else:
                self._tup_grade_cate["E"].update({per_name: per_grade})

    def get_grade_category(self):
        self._cate_grades()
        for grade_cate, dic_students in self._tup_grade_cate.items():
            print(dic_print_string[grade_cate], "人數: ", len(dic_students))
