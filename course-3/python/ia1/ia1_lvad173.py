# -*- coding: utf-8 -*-
"""ia1_lvad173.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N5Ih03ndHP8M-zrhcQSW0zFEzdKi7VCo
"""

# 1
w=float(input('enter width in meter:'))
l=float(input('enter length in meter:'))
area=w*l
if area<200:
  cat='small'
  print(f"it has a area of {area} meter square and it is in {cat} category")
elif area<700:
  cat='medium'
  print(f"it has a area of {area} meter square and it is in {cat} category")
else:
  cat='large'
  print(f"it has a area of {area} meter square and it is in {cat} category")

#2
height=float(input('enter height in meter'))
weight=float(input('enter weight in kg'))
bmi=weight/(height**2)
print(bmi)
if bmi<20:
  print('eat more')
elif bmi<30:
  print('maintain')
else:
  print('diet and ex')

#3
student_grade_dic={
    1:{'math':87,'eng':76,'science':77},
    2:{'math':54,'eng':86,'science':67}
}
def ret(dic):
  print(dic)

def add(dic,k,value):
  dic[k]=value
  return dic

def update(dic,k,v):
  dic[k]=v
  return dic

ret(student_grade_dic)
add_dic=add(student_grade_dic,3,{'math':84,'eng':81,'science':63})
print(add_dic)
up_dic=update(student_grade_dic,1,{'math':97,'eng':76,'science':77})
print(up_dic)

#4
age=int(input('age:'))
if age<13:
  category='children'
  rating=['u']
elif age<18:
  category='teen'
  rating=['u','u/a']
elif age<60:
  category='adult'
  rating=['u','u/a','a']
else:
  category='senior'
  rating=['u','u/a','a']
print(f"{age} is on category {category} and can watch {rating}")

#5
list_s_id=[1,2,3,4,5,6,7,8,9,10,11]
List_even_s_id=[]
for l in list_s_id:
  if l%2==0:
    List_even_s_id.append(l)

print(List_even_s_id)

#6
hash_word='xyz@123'
while(True):
  password=input('enter password:')
  if password==hash_word:
    print('correct password')
    break

#7
def avg_score(score_list):
  score_sum=0
  for l in score_list:
    score_sum=score_sum+l
  avg=score_sum/(len(score_list))
  return avg
def insight(s):
  if s>9:
    print('good job')
  elif s>7:
    print('good, improve further')
  elif s>5:
    print('bad, action should be taken to improve satisfaction')
  else:
    print('very bad, solve immediately')
scores=[3,6,7,8,9,2,3,5,7,1,9,9,10,5,7,9,9,9]#scores are stored in list
avg_of_score=avg_score(scores)
print(f"average score is {avg_of_score}")
insight(avg_of_score)

#8
def count_vowel(st):
  count_v=0
  st1=st.lower()
  for s in st1:
    if (s=='a') or (s=='e') or (s=='i') or (s=='o') or (s=='u'):
      count_v=count_v+1
  return count_v

string_to_count_vowel=input('enter text here:')
c=count_vowel(string_to_count_vowel)
print(f"there are {c} vowels in teh string")

#9
import datetime
cur_ti=datetime.datetime.now()
in_time=input('yyyy-mm-dd hh:mm')
input_time=datetime.datetime.strptime(in_time,'%Y-%m-%d %H:%M')
if cur_ti>input_time:
  print('over')
elif cur_ti<input_time:
  print('pls wait')
else:
  print('alert')

#10
def loanpay(l,b):
  try:
    if l>b:
      raise loanerror()
    else:
      print('can pay')
  except loanerror:
    print('insufficient balance')
class loanerror(Exception):
  pass
try:
  bal=float(input('bank balance :'))
  p=float(input('principle amount:'))
  n=int(input('time on year:'))
  r=float(input('interest rate:'))
  loan=p+((p*n*r)/100)
  loanpay(loan,bal)
except ValueError:
  print('enter correct value')
except ZeroDivisionError:
  print('zero division error')

#11
try:
  id=int(input('inter id :'))
  name=(input('name:'))
  year=int(input('year of birth:'))
  print('all values are correct')
except ValueError:
  print('enter correct value')

#12
a_div=float(input('(a/b)enter value of a:'))
b_div=float(input('(a/b)enter value of b:'))
try :
  div_value=a_div/b_div
  print(div_value)
except ZeroDivisionError:
  print('you cant divide a value by 0, enter a value for b which is not 0')

#13
lines=[]
for i in range(5):
  line=input()
  lines.append(line)
with open('/content/log.txt','w') as file:
  for l in lines:
    file.write(l)
    file.write('\n')

#14
with open('/content/log.txt','r') as file1:
  print(file1.readlines())

#15
input_comp=input()
with open('/content/news.csv','a') as file:
  file.write(input_comp)
  file.write('\n')

with open('/content/news.csv','r') as file:
  print(file.read())