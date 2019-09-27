import unittest

# equivalent to:
# cd <path to folder of this file>
# python -m unittest discover -v -p '*_unittest.py'
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover(".", pattern="*.py")
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(tests)
