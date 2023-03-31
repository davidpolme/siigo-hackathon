## run the first test use_test_1.py
print("Running use_test_1.py")
with open("use_test_1.py") as f:
    exec(f.read())
    
## run the second test use_test_5.py
print("Running use_test_5.py")
with open("use_test_5.py") as f:
    exec(f.read())