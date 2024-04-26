

#ARMAN NAJAFI 4022125

import pandas as pd
import random

test = pd.read_csv("test.csv")
file = pd.read_csv("train.csv")


#رقم اخر قبمت بیت کوین در روز یازدهم باید حذف شود و مقدار آن گرد شود



def change_random_element(lst):
    random_index = random.randint(0, len(lst) - 1)
    lst[random_index] = round(random.uniform(1.1, 1.9),1)


eq=part1=part2=part3=part4=part5=part6=part7=part8=part9=part10=column11=cell_value=diff=index=score=group1=group2=random_number1=random_number2=None
parent1=parent2=None
list_result=[]
sort_diff_list=[] 
x_parents=[]
x_parent1=[]
x_parent2=[]

smaller_99=[]
smaller_499=[]
smaller_1000=[]
smaller_1500=[]
smaller_2000=[]
bigger_2000=[]
parents_array=[]
i=0


for index, row in file.iterrows():
    if i<=100:
        i=i+1
        x1=0
        x2=0
        x3=round(random.uniform(0.001 ,1.03), 1)
        x4=round(random.uniform(0.001, 1.07), 1)
        x6=round(random.uniform(0.001, 1.09), 1)       
        x5=round(random.uniform(1, 1.1), 1)
        x7=round(random.uniform(1, 1.2), 1)
        x8=round(random.uniform(1, 1.5), 1)
        x9=round(random.uniform(1.7, 2), 1)
        x10=round(random.uniform(1.9, 2), 1)
        for column_name , cell_value in row.items():
            if column_name == 'dim1':
                part1 = cell_value * x1
            elif column_name == 'dim2':
                part2 = cell_value * x2
            elif column_name == 'dim3':
                part3 = cell_value * x3
            elif column_name == 'dim4':
                part4 = cell_value * x4
            elif column_name == 'dim5':
                part5 = cell_value * x5
            elif column_name == 'dim6':
                part6 = cell_value * x6
            elif column_name == 'dim7':
                part7 = cell_value * x7
            elif column_name == 'dim8':
                part8 = cell_value * x8
            elif column_name == 'dim9':
                part9 = cell_value * x9
            elif column_name == 'dim10':
                part10 = cell_value * x10
            elif column_name == 'result':
                column11 = cell_value
            elif column_name == 'shomare':
                index = cell_value
        # eq= zigma (zarib random * meghdar cell)
        eq=part1+part2+part3+part4+part5+part6+part7+part8+part9+part10  
        eq = round(eq)
        eq = str(eq)
        eq = eq[:-1]
        eq = int(eq)
        #diff 
        diff= cell_value - eq
        diff= abs(diff)
        
        list=[index,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,eq,diff]
        list_result.append(list)
        
        indexedDiff=[index, diff] #this line is important
        sort_diff_list.append(indexedDiff)
        sort_diff_list.sort(key=lambda x: x[1])
        
        
        #fitness function actions------------------------------------------------------------------------------------------------------

for index in (sort_diff_list):
    if index[1] <99:
        smaller_99.append(index[1])
    
    if index[1]>99 and index[1] < 499:
        smaller_499.append(index[1])
    
    if index[1]>499 and index[1] < 1000:
        smaller_1000.append(index[1])
    
    if index[1]>1000 and index[1] < 1500:
        smaller_1500.append(index[1])
    
    if index[1]>1500 and index[1] < 2000:
        smaller_2000.append(index[1])
    
    if index[1]>2000:
        bigger_2000.append(index[1])
    

random_number1 = random.randint(1, 100)
random_number2 = random.randint(1, 100)


if random_number1 >= 0 and random_number1 <=45:
    group1= smaller_99

if random_number1 > 46 and random_number1 <=60:
    group1= smaller_1000


if random_number1 >= 61 and random_number1 <=75:
    group1= smaller_1500
    

if random_number1 >= 75 and random_number1 <=90:
    group1= smaller_2000
    

if random_number1 >= 91 and random_number1 <=100:
    group1= smaller_1500

#group2 -------------------------------------------------------------------------------

if random_number2 >= 0 and random_number2 <=45:
    group2= smaller_99

if random_number2 > 46 and random_number2 <=60:
    group2= smaller_1000


if random_number2 >= 61 and random_number2 <=75:
    group2= smaller_1500
    

if random_number2 >= 75 and random_number2 <=90:
    group2= smaller_2000
    

if random_number2 >= 91 and random_number2 <=100:
    group2= smaller_1500

group1Chooser = random.randint(0, len(group1)-1)
group2Chooser = random.randint(0, len(group2)-1)

print("len group 1 :" , len(group1))


diffparent1 = group1[group1Chooser]
diffparent2 = group2[group2Chooser]


print('diff parent 1 :',diffparent1)
print('diff parent 2 :',diffparent2)
for index in list_result:
    if index[12] == diffparent1:
        parents_array.append(index)
        break

for index in list_result:  
    if index[12] == diffparent2:
        parents_array.append(index)
        break



# parents  
  
for parent_array in parents_array:
    x_parents.append(parent_array)

x_parents[0].pop(0)
x_parents[1].pop(0)
x_parents[0].pop(11)
x_parents[1].pop(11)
x_parents[0].pop(10)
x_parents[1].pop(10)

print('x parents : ',x_parents)

parent1=x_parents[0]
parent2=x_parents[1]
print('parent 1 : ',parent1)
print('parent 2 : ',parent2)
# cross over parent --------------------------------------------------------------------------------------------------------------------------


# انتخاب یک اندیس رندم برای برش
cut_index = random.randint(0, len(parent1) - 1)

# ترکیب بخش‌ها
child1 = parent1[:cut_index] + parent2[cut_index:]
child2 = parent2[:cut_index] + parent1[cut_index:]


print('\ncut index : ',cut_index)
print('\n-------------cross over -----------')
print("\nChild 1:", child1)
print("Child 2:", child2)


# mutations ------------------------------------------------------------------------------------------------------------------------



print('\n------------- mutation -----------')
change_random_element(child1)
change_random_element(child2)
print("\n new Child 1:", child1)
print("\n new Child 2:", child2)

print('--------------------------------')


print('رقم اخر قبمت بیت کوین در روز یازدهم باید حذف شود و مقدار آن گرد شود')

