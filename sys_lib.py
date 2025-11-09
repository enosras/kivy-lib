import sys
import subprocess
import time
import math


x = len(sys.argv)
print(len(sys.argv))
try:
    if x < 3:
    #print(x)

        digit_one = sys.argv[1]
        digit_two = sys.argv[2]
        print("digit two", digit_two)
        print("digit one", digit_one)
        subprocess.run(['./sys.sh', digit_one, digit_two])
except:
    print("Thanks, error")
    time.sleep(1)