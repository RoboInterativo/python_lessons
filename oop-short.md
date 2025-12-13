Класс в питоне, это данные и фунции которые созданы чтобы их обрабатывать.

Для чего, легко использовать в разработке. позволяет избежать самоповторов.

blueprint Заготовка, слепок. класс является заготовкой, если мы содаем объект на основе класса
то говорят про инстанс, экзепляр объекта на основе нашего класса

# Статический метод
# Классовый метод
# Классовые переменные
# Переменные объекта
# Иницализация метод

```python
class EmpLoyee
  #классовая переменная
  all_workers=0
  raise_amount=1.04
  #Инит меттод, конструктор класса
  def __init__(self,first,last,pay):
    #переменные объекта, инстанса
    self.first=first
    self.last=last
    self.pay=pay
    Employee.all_workers +=1
    self.email=f"{self.last}.{self.first}@company.com"

    #deleter
    @fullname.deleter    
    def fullname(self):

        self.first=None
        self.last=None
    #Сеттер
    @fullname.setter    
    def fullname(self,name):
        first,last=name.split()
        self.first=first
        self.last=last

  @property
  def fullname(self):
    return f"{self.first} {self.last}"

  # классовый метод меняет классовую переменную
  @classmethod
  def set_raise_amt(cls,amount):
    cls.raise_amount=amount

  #Альтернативный консттруктор на классовом методе
  @classmethod
  def from_string(cls,emp_str):
    first,lass,pay=emp_str.split("-")
    return cls(first,last,pay)

  #статический метод (не связан с объектом)
  @staticmethod
  def is_workday(day):
    if day.weekday==5 or  day.weekday()==6:
      return False
    return True
  #  Магический метод __add__
  def __add__(self,other):
        return self.pay+other.pay



class Developer(EmpLoyee):
  pass
emp1=Employee("Alex","Shilo","10000")
print(emp1.fullname()) #Статический метод
print(Employee.fullname(emp1)) #Метода класса

print (Employee.__dict()__)
print (emp1.__dict()__)
print (emp1+emp2)
```






help (Developer.__main__)







Декораторы
```python
def decorator_function (original_function):
  def wrapper_function(*args,**kwargs):
    print ('Execute Before')
    result=original_function(*args,**kwargs)
    print ("Execute After",original_function.__name__,"\n")
    return result
  return wrapper_function
@decorator_function
def display_info(name,age):
  print ("display info wan with arguments()"
```
