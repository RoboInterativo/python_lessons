
def prefix_decorator(prefix):
    def decorator_function (original_function):
      def wrapper_function(*args,**kwargs):
        print (prefix,'Execute Before')
        result=original_function(*args,**kwargs)
        print (prefix,"Execute After",original_function.__name__,"\n")
        return result
      return wrapper_function
    return decorator_function

@prefix_decorator("Prefix add")
def display_info(name,age):
  print (f"display info wan with arguments({name} ,{age}) ")


display_info("Alex",44)
