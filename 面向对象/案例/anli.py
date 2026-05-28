#学生类
class student:
    # 初始化
    def __init__(self, name, age=0, chinese=0, math=0, english=0):
        self.name = name
        self.age = age
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        return f"学生姓名：{self.name}，年龄：{self.age}，语文成绩：{self.chinese}，数学成绩：{self.math}，英语成绩：{self.english}"

    # 修改学生成绩
    def update_score(self, chinese=None, math=None, english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

#教务系统类
class education_system:
    def __init__(self):
        self.students_list = []

    # 添加学生
    def add_student(self):
        input_name = input("请输入学生姓名：")
        for s in self.students_list:
            if s.name == input_name:
                print("学生已存在！")
                return
        input_age = int(input("请输入学生年龄："))
        input_chinese = int(input("请输入学生语文成绩："))
        input_math = int(input("请输入学生数学成绩："))
        input_english = int(input("请输入学生英语成绩："))
        if 0 <= input_chinese <= 100 and 0 <= input_math <= 100 and 0 <= input_english <= 100:
            new_student = student(input_name, input_age, input_chinese, input_math, input_english)
            self.students_list.append(new_student)
        else:
            print("成绩输入有误，请重新输入！")
    #根据名字修改学生成绩
    def update_student_score(self):
        input_name = input("请输入要修改成绩的学生姓名：")
        for s in self.students_list:
            if s.name == input_name:
                input_chinese = int(input("请输入学生新的语文成绩："))
                input_math = int(input("请输入学生新的数学成绩："))
                input_english = int(input("请输入学生新的英语成绩："))
                if 0 <= input_chinese <= 100 and 0 <= input_math <= 100 and 0 <= input_english <= 100:
                    s.update_score(chinese=input_chinese, math=input_math, english=input_english)
                    print("成绩修改成功！")
                    print(s)
                    return
                else:
                    print("成绩输入有误，请重新输入！")
                return
        print("未找到该学生！")    
    # 根据名字删除学生
    def delete_student(self):
        input_name = input("请输入要删除的学生姓名：")
        for s in self.students_list:
            if s.name == input_name:
                self.students_list.remove(s)
                print("学生删除成功！")
                return
        print("未找到该学生！")
    #根据名字查询学生信息
    def search_student(self):
        input_name = input("请输入要查询的学生姓名：")
        for s in self.students_list:
            if s.name == input_name:
                print(s)
                return
        print("未找到该学生！")
    # 显示所有学生信息
    def show_students(self):
        for student in self.students_list:
            print(student)
    #运行系统
    def run(self):
        while True:
            print("\n欢迎使用教务系统！")
            print("1. 添加学生")
            print("2. 修改学生成绩")
            print("3. 删除学生")
            print("4. 查询学生信息")
            print("5. 显示所有学生信息")
            print("6. 退出系统")
            choice = input("请输入您的选择：")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.update_student_score()
            elif choice == '3':
                self.delete_student()
            elif choice == '4':
                self.search_student()
            elif choice == '5':
                self.show_students()
            elif choice == '6':
                print("感谢使用教务系统，再见！")
                break
            else:
                print("无效的选择，请重新输入！")
if __name__ == "__main__":
    system = education_system()
    system.run()
       