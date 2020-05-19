# test.py is a file within the package package_1
# test_func is a function within test.py file of package_1

# Multiple ways to import and use the actual function within a package

from package_1.test import test_func
from package_1 import test

print("main file")

# Call the function from test.py
test.test_func()

# Since the import has been done, another direct way to call the function
test_func()
