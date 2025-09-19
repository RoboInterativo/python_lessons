
def myfunc(string_for,find_string,replace_string):
    word=""
    word_index=[]
    i=0
    beg=-1
    words=[]
    find_string_index=[]
    for i in range(len (string_for )):

        if i<len(string_for):
            if string_for[i] !=" ":
                if beg==-1:
                    beg=i
                word=word+string_for[i]
            else:
               if beg>=0:

                    word_index.append( (beg,i-1) )
                    words.append(word)
                    beg=-1
                    word=""


    word_index.append( (beg,i) )
    words.append(word)
    str2=""
    for i in range(len(words) ):
        if words[i]==find_string:
            str2=str2+replace_string
            find_string_index.append(i)
        else:
            str2=str2+words[i]
        if i+1<len(words):
            beg,end=word_index[i]
            beg2,end2=word_index[i+1]
            sp=beg2-end-1
            if sp>0:
                str2=str2+" "*sp
    beg,end=word_index[-2]
    beg2,end2=word_index[-1]
    if beg2<0:


        # print(word_index[-2],word_index[-1])
        sp=end2-end
        if sp>0:
            str2=str2+" "*sp





    # print(word_index,words,len(string_for))
    # print(find_string_index)
    # print(str2)

    return str2


# rez=myfunc("cat runs to another cat","cat","bull")

# result= myfunc("cat   runs   to   another   cat   ","cat","bull")
#
# result2 ="bull   runs   to   another   bull   "
# print(len(result), len(result2))
