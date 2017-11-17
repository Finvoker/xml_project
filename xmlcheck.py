
# coding: utf-8

# In[2]:


stack=[]
listline=[]
file = open('example.xml')
for line in file:
    listline.append(line)
file.close()

for line in listline :    
    tag = line[0]
    title = line[2]
    if (line[1]!= ' '):
        print('line not well_formed')
        break
    else:
        if tag=="0" :
            stack.append(title)
            #print('title taken')
            #print(stack)
        else :
            if tag=="1" :
                if stack[-1]==title :
                    #print('title poped')
                    stack.pop()
                    #print(stack)
                else:
                    print('not well-ordered')
                    break
            else:
                print('not well-formed xml')
                break


# In[3]:


if len(stack)==0 :
    print('well_formed!')
    #print(stack)
else:
    print('not well-formed')


# In[4]:


for line in listline : 
    print(line)

