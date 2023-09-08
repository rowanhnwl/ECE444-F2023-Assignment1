from utils import *

tests = ["hello", 349.180447902, 2034, "python", 9.3084, 8938, "str", 65.0038, 492]

for test in tests:
    print("Testing: " + str(test))
    
    try:
        print("reversed(): " + str(utils.reversed(test)))
    except:
        print("reversed() failed on " + str(test))

    try:
        print("formatter():" + str(utils.formatter(test)) + "\n")
    except:
        print("formatter() failed on " + str(test) + "\n")
