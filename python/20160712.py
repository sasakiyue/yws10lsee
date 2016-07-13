
# coding: utf-8

# In[84]:

# チェック関数
def check(count):
    
    str_count = str(count)
#     print(str_count)
#     print (int(len(str_count)/2))
    
    for i in range(int(len(str_count)/2)):
#         print (str(i) + ":" + str_count[i])
#         print (str(i) + ":" + str_count[-1 -i])
        if str_count[i] != str_count[-1-i]:
               return False
    
    return True
    


# In[85]:

count = 10

while True:
    
    count_bi = format(count,'b')
    count_oct = format(count,'o')
    
    count_check = check(count)
    count_bi_check = check(count_bi)
    count_oct_check = check(count_oct)
    
    if count_check == True:
        if count_bi_check == True:
            if count_oct_check == True:
                break
            
    count+=1


# In[86]:

count


# In[ ]:



