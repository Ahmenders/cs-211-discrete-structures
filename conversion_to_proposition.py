
# coding: utf-8

# In[2]:


def Converse(l):
    negation="~"
    implies="->"
    if l[0]==negation and l[4]==negation:
        return(negation+l[-1]+implies+negation+l[1])
    elif l[0]==negation and l[4]!=negation:
        return(l[-1]+implies+negation+l[1])
    elif l[0]!=negation and l[3]==negation: 
        return(negation+l[-1]+implies+l[0])
    else:
        return(l[-1]+implies+l[0])


# In[3]:


def Inverse(l):
    negation="~"
    implies="->"
    if l[0]==negation and l[4]==negation:
        return(l[1]+implies+l[-1])
    elif l[0]==negation and l[4]!=negation:
        return(l[1]+implies+negation+l[-1])
    elif l[0]!=negation and l[3]==negation: 
        return(negation+l[0]+implies+l[-1])
    else:
        return(negation+l[0]+implies+negation+l[-1])


# In[4]:


def Contrapositive(l):
    l = Converse(l)
    l = Inverse(l)
    return l

#Another logic for contrapositive
   # negation = "~"
   # implies = "->"
   # if l[0] == negation and l[4] == negation:
   #     return (l[-1] + implies + l[1])
   # elif l[0] == negation and l[4] != negation:
   #     return(negation + l[-1] + implies + l[1])
   # elif l[0] != negation and l[3] == negation: 
   #     return(l[-1] + implies + negation + l[0])
   # else:
   #     return(negation + l[-1] + implies + negation + l[0])


# In[7]:


x= input("Propositional : ")
y= input("Type Of Propositional : ")
l= list(x)
if y == 'Implication' or y == "implication":
    print('Converse : '+ Converse(l))
    print('Contapositive : '+ Contrapositive(l))
    print('Inverse : '+ Inverse(l))
if y == 'Converse' or y == 'converse':
    print('Implication : '+ Converse(l))
    l = Converse(l)
    print('Contrapositive : '+ Contrapositive(l))
    print('Inverse : '+ Inverse(l))
if y == 'Contrapositive'or y == 'contrapositive':
    l = Contrapositive(l)
    print('Implication : '+ l)
    print('Converse : '+ Converse(l))
    print('Inverse : '+ Inverse(l))
if y == 'Inverse'or y == 'inverse':
    l = Inverse(l)
    print('Implication : '+ l)
    print('Converse : '+ Converse(l))
    print('Contrapostive : '+ Contrapositive(l))

