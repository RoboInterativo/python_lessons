
def myfunc(string1):


    return ""


# myfunc("abba")
# myfunc("abbu")
import re

# Регулярное выражение, составленное в MATLAB
pattern = re.compile(r"^\S+@\S+\.\S+$")

# Проводим проверку электронного адреса
is_valid = pattern.match("user@example.com")
print(is_valid is not None)  # Вернёт "True", если адрес действителен, и "False" в противном случае
