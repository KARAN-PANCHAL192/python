day=0
q1="is your birthday in set?\n"+\
    "1 3 5 7\n"+\
    "9 11 13 15\n"+\
    "17 19 21 23\n"+\
    "25 27 29 31\n"+\
    "1 for yes,0 for no"
ans=int(input(q1))
if ans==1:
    day+=1
q2="is your birthday in set?\n"+\
    "2 3 5 6 7\n"+\
    "10 11 14 15\n"+\
    "18 19 22 23\n"+\
    "26 27 30 31\n"+\
    "1 for yes,0 for no"
ans=int(input(q2))
if ans==1:
    day+=2
q3="is your birthday in set?\n"+\
    "4 5 6 7\n"+\
    "12 13 14 15\n"+\
    "20 21 22 23\n"+\
    "28 29 30 31\n"+\
    "1 for yes,0 for no"
ans=int(input(q3))
if ans==1:
    day+=4
q4="is your birthday in set?\n"+\
    "8 9 10 11\n"+\
    "12 13 14 15\n"+\
    "25 26 27\n"+\
    "28 29 30 31\n"+\
    "1 for yes,0 for no"
ans=int(input(q4))
if ans==1:
    day+=8
q5="is your birthday in set?\n"+\
    "16 17 18 19\n"+\
    "20 21 22 23\n"+\
    "24 25 26 27\n"+\
    "28 29 30 31\n"+\
    "1 for yes,0 for no"
ans=int(input(q5))
if ans==1:
    day+=16
print(day,"is your birthday date")



    
    
    
    
