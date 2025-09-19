
def myfunc(string1):

    def reverse(mystr1):
        mystr2=""
        for i in range(len(mystr1) ):

                mystr2=mystr2+string1[-1*(i+1)]
        return mystr2
    print (string1 ,reverse(string1))
    return string1==reverse(string1)
# 12121
# myfunc("abba")
# myfunc("abbu")
