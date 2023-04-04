import random
import string

gen=["Indece","Aim","daavi","Samuel","Scisa","agenda","agen","27","36","#","$%^","Kwame","Anumd3",
"common","naa","teshie","body","personal","person"]
nouns=["kante","Chelsea","Hack","TA","gyimie","flutter","greedy","red","Yellow","green","green","blue",
"violet","vex","cheating","56","65","63","2","3","4"]

while True:
     gen=random.choice(gen)
     nouns=random.choice(nouns)
     number=random.randrange(0,100)
     special_char=random.choice(string.punctuation)

     password= gen+nouns+str(number)+special_char
     print("Your Password is:%s" %password)

     response =input("Would you like another password? Type Y or N: ")
     if response == 'N':
        break