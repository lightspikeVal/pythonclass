#Worklist
import random as re
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah']
shopping=re.choices(students,k=2)
while shopping[0]==shopping[1]:
    if shopping[0]==shopping[1]:
        shopping=re.choices(students,k=2)
        print("Re")
cleaning=[]
for i in range(len(students)):
    if students[i] not in shopping:
        if len(cleaning)==3:
            break
        cleaning.append(students[i])
        
cooking=[]
for i in range(len(students)):
    if students[i] not in shopping and students[i] not in cleaning:
        cooking.append(students[i])
print("Shopping list: ", shopping)
print("Cleaning list: ", cleaning)
print("Cooking list: ", cooking)
