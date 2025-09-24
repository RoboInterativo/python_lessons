
def myfunc(string1):


    return ""


# myfunc("abba")
# myfunc("abbu")
import re

# Регулярное выражение, составленное в MATLAB

phone_pattern = re.compile(r'^(\+7|8)[\s\-]?\(?\d{3}\)?[\s\-]?\d{3}[\s\-]?\d{2}[\s\-]?\d{2}$')
password_pattern = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%*#?&]{8,}$')
name_pattern = re.compile(r'^[A-Za-zА-Яа-яЁё\s\-]+$')
username_pattern = re.compile(r'^[a-zA-Z0-9_]{3,20}$')
email_pattern=re.compile(r"^\S+@\S+\.\S+$")
def validate(valstr,pattern):
# Проводим проверку электронного адреса
    #pattern = re.compile()
    is_valid= pattern.match(valstr)
    result=is_valid  is not None
    return  result
#print(is_valid is not None)  # Вернёт "True", если адрес действителен, и "False" в противном случае
rez=validate("1@1.ru",email_pattern)
print  (rez,type(rez))
