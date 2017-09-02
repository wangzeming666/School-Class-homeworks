from sorted_student import *
import sys

print("""
+----------------------------------+
| a) 添加学生信息                  |
| d) 删除学生信息                  |
| m) 修改学生信息(改学生成绩)      |
| 1) 按学生成绩高到低显示学生信息  |
| 2) 按学生成绩低到高显示学生信息  |
| 3) 按学生年龄到高低显示学生信息  |
| 4) 按学生年龄低到高显示学生信息  |
| q) 退出。                        |
+----------------------------------+

""")

while True:
    inputt = input()
    if inputt == 'a':
        input_student(input("You can choise a file, enter none to abandeon") )
    if inputt == 'd':
        delite()
    if inputt == 'm':
        change()
    if inputt == '1':
        sorted1()
        output_list()
    if inputt == '2':
        sorted2()
        output_list()
    if inputt == '3':
        sorted3()
        output_list()
    if inputt == '4':
        sorted4()
        output_list()
    if inputt == 'q':
        sys.exit()
        
        
