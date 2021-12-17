from random import *
import datetime
import sys
import time
from abc import *
class Util:
  record = []
  company = 'CALL CENTER'
  @staticmethod
  def Id():
    no = ''
    for i in range(1):
      no += str(randint(1,9))
    return no

  @classmethod
  def m1(cls,msg):
    Util.record.append(msg)
  
  @staticmethod
  def Number():
    phone = ''
    phone += str(randint(6,9))
    for i in range(9):
      phone += str(randint(0,9))
    return phone

class Callcenter(Util):
  def __init__(self,name,age):
    self.number = Util.Number()
    self.id = Util.Id()
    self.name = name
    self.age = age

  def start(self):
    dateTimeObj = datetime.datetime.now()
    print()
    print('START_TIME')
    print('{}/{}/{}'.format(dateTimeObj.day,dateTimeObj.month,dateTimeObj.year))
    print('{}:{}:{}'.format(dateTimeObj.hour,dateTimeObj.minute,dateTimeObj.second))
    msg ='date and time:{} with name:{} age:{} id:{} phone:{}'.format(datetime.datetime.now(),self.name,self.age,self.Id(),self.Number())
    Util.m1(msg)

  def end(self):
    dateTimeObj = datetime.datetime.now()
    print()
    print('END_TIME')
    print('{}/{}/{}'.format(dateTimeObj.day,dateTimeObj.month,dateTimeObj.year))
    print('{}:{}:{}'.format(dateTimeObj.hour,dateTimeObj.minute,dateTimeObj.second))
  
  def duration(self):
    dateTimeObj = datetime.datetime.now()
    time = '{}:{}:{}'.format(dateTimeObj.hour,dateTimeObj.minute,dateTimeObj.second)
    date = datetime.datetime.strptime(time, "%H:%M:%S")
    total = date - datetime.datetime(2021,12,18)
    seconds = total.total_seconds()
    print('Duration:{}'.format(seconds))

print('Company Name:',Util.company)
print('Do u want see : call details or live recording')
print('1.c - call details\n2.e - exit')
option = input('enter a choose option [c|e]:').lower()
count = 1
while option not in ['c','e']:
  if count >= 3:
    print('you attempt max time. plz try again:')
    sys.exit()
  option = input('invalid option choose correct one [s|c]:').lower()
  count+=1

if option == 'c':
  name = input("enter ur name :")
  age = int(input('enter ur age:'))
  c = Callcenter(name,age)
  print('good name:{}\nage is:{}\nId is:{}\nPhone No:{}'.format(name,age,c.id,c.number))
  c.start()
  time.sleep(15)
  c.end()
  c.duration()

else:
  print('thanks for using application:')
  sys.exit()