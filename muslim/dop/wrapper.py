def decorator_function (original_function):
  def wrapper_function(*args,**kwargs):
    print ('Execute Before')
    result=original_function(*args,**kwargs)
    print ("Execute After",original_function.__name__,"\n")
    return result
  return wrapper_function

@decorator_function
def display_info(name,age):
  print (f"display info wan with arguments({name} ,{age}) ")


display_info("Alex",44)
