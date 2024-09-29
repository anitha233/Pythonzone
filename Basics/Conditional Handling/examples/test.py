import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge $2 a day")
elif type == "t3.medium":
    print("It will charge $4 a day")  
elif type == "t2.Xlarge":
    print("It will charge $8 a day")      
else:
    print("we can't do it")  