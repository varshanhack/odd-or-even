# Odd or Even
import sys,subprocess
while True:
 n=int(input("Enter a number = "))
 print("")
 if n%2==0:
    print(n,"is even number")
 else:
    print(n,"is odd number")
 print("")
 input("Press enter to continue...")
 subprocess.run("cls",shell=True)
