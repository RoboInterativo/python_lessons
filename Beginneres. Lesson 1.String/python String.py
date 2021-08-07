#!/usr/bin/env python
# coding: utf-8

# In[36]:


#Выввод сообщения 
print ('Hello world!')


# In[54]:


#Вывод сообщения при помощи переменных
message='Hello world'
#Выввод сообщения 
print (message)


# In[38]:


#Зачем нужные двойные кавычки, экранирование символов
message='Kid\'s World!'
print (message)
message="Kid's world"
print (message)


# In[45]:


#Обращение к символу по индексу
message="Hello world"

#Первый символ
print (message[0])

#Слово Hello
print (message[0:5])

#Слово Hello
print (message[:5])

#Слово World
print (message[6:11])

#Слово World
print (message[6:])        
               


# In[63]:


#count
message='Hello world'

#Число символов в строке
print (len (message))

#Число симвлов l
print (message.count('l'))

#Если символы есть 
print (message.find('Hello'))

#Если символов нет в строке
print (message.find('universe'))

#Upper, lower,replce
print (message.upper())
print (message.lower())
print (message.replace ('world','universe') )


# In[49]:


#Переменные и сцепка строк +
greeting='Hello'
name='Mike'
message=greeting+', '+ name+'!'
print (message)


# In[53]:


#Форматирование строк
greeting='Hello'
name='Mike'

#Старый формат
message='{}, {}!'.format(greeting, name)
print (message)

#Новый python3.6+
message=f'{greeting}, {name}!'

print (message)


# In[65]:


#Внутрення справка питон
print (dir (str))
print (help (str))

