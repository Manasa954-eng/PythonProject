#Any Pytest file should start with test_ or end with _test
#Any Code should be wrapped in method
#pytest method names should always start with test_ keyword
#In pytest, every method is treated as every test case
#In pytest, if two methods have the same name, then only the latest method results are shown. It is better to have unique method names.
import pytest


@pytest.mark.smoke
def test_first_program():
    print("Hello World")

@pytest.mark.xfail
def test_second_program():
    print("Good Evening")


#To run the same test in console instaed of pycharm, give the pytest path in the console
#Second, run using the following commands
 #path py.test (To run all the appropriate tests in that path)
 #path py.test -v (To run all the appropriate tests with more info than previous)
 #path py.test -v -s (To run all the appropriate tests with more info and logs)

#To run the specfic files from console, write the name
 #path py.test test_demo1.py -v -s

#In pytest, the naming convention of test methods are very important as we can run certain tests from different files using that convention (Method names should have some sense)
#In order to run a particular tests from different files, we can do it on particular key word that the test methods are holding
  #path py.test -k second -v -s

#-k stands for method names execution
#-s logs in output
#-v stands for more info metadata

#you can mark (tag) tests with @pytest.mark.smoke and then run with -m

#To skip a particular test, @pytest.mark.skip

#To run a test and still it should not be reported, because we need the test case for the other test cases to run but we know that their is some bug in it, so it should not report
 #@pytest.mark.xfail

 #pytest -n -2 //pytest -xdist plugin to run the test in parallel to save time