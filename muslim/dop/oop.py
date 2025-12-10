class Employee:
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

    @property
    def fullname(self):
      return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self,name):
      self.first,   self.last =name.split()

    @fullname.deleter
    def fullname(self):
      self.first=None
      self.last =None

    #Классовый метод меняет классовые переменные
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amount=amount

    #Альтернативный консттруктор
    @classmethod
    def from_string(cls,emp_str):
        first,lass,pay=emp_str.split("-")
        return cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday==5 or  day.weekday()==6:
          return False
        return True


    #Для преобразования в строку
    @fullname.deleter
    def fullname(self):

        self.first=None
        self.last=None
    def __str__(self):
        return f"{self.first},{self.last}"
    def __repr__(self):
        return  f"Employee ( {self.first},{self.last},{self.pay})"

    def __add__(self,other):
        return self.pay+other.pay

    def __len__(self):
         pass

class Developer(Employee):
  raise_amount= 1.01
  #Расширяем init
  def __init__(self,first,last,pay,lp):
      super().__init__(first,last,pay)
      self.lp=lp


emp1=Employee("Alex","Shilo","10000")
print (emp1.fullname)
# emp1.fullname="Serg Shilo"
del(emp1.fullname)
print (emp1.fullname)
# print(emp1.fullname()) #Статический метод
# print(Employee.fullname(emp1)) #Метода класса


# print (help(Employee.__dict__))
# print (help (emp1.__dict__ ) )
