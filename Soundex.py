# Word dictonary with key and there values for make process easy.
words = {'a':0, 'b':1,'c':2,'d':3,'e':0,'f':1,'g':2,'h':0,
        'i':0,'j':2,'k':2,'l':4,'m':5,'n':5,'o':0,'p':1,'q':2,
        'r':6,'s':2,'t':3,'u':0,'v':1,'w':0,'x':2,'y':0,'z':2}

# Takes input from user.
# Using convert input into lower char.
names1 = input("Enter name here : ").lower()
# A variable to store final value.
total = 0
# Using loop to take every single character from given string.
names_val = {'ali':'a4','alee':'a4','sufyan':'s215','sufiyan':'s215','sofiyan':'s215','hussain':'h225','hossain':'h225','hanif':'h15','haneef':'h15'}
# total variable for store the sum of name.
total = 0
#nfirst for store the 1st char of input value.
nfirst = names1[0]
#  Using for loop for break input into charecters.
# So easily found the value from dictonary.
for i in names1:
    t = words[i]
    if t < 1:
        pass
    else:
        nfirst = (f"{nfirst}{t}")
        total = total+t

names_val[names1]=nfirst
a = [k for k,v in names_val.items() if v == f'{nfirst}']
# Using if else statement.
# If algorithm found more than one similar word than print all similar words.
if len(a) > 1:
    print("we found some similar words")
    print("Word  \tvalue  \tTotal ")
    for i in range(len(a)):
        print(f"{a[i]}\t{nfirst}\t{total}" )
# Else print the name, value or total.
else: 
    print("we found some similar words")
    print("Word  \tvalue  \tTotal ")
    for i in range(len(a)):
        print(f"{a[i]}\t{nfirst}\t{total}" )
        #print(f"Word : {a[i]} , value : {nfirst} , Total value of name is : {total}" )
