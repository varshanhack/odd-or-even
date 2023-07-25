import sys,subprocess
while True:
 n=int(input("Enter a number = "))
 if n%2==0:
    print(n,"is even number")
 else:
    print(n,"is odd number")
 print("c = continue\nx = exit")
 x=input("Type c or x ==> ")
 if x=="c":
     subprocess.run("cls",shell=True)
 else:
     break

