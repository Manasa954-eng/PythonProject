#for class, start with Test
#for method, start with test_
#for file, start or end with test_ or _test respectively

#instead of giving fixtures again and again, we can define them at class level
#By using @pytest.mark.usefixtures(" ")


import pytest


@pytest.mark.usefixtures("setup")
class Test_Optimize_Fixture:

    def test_demo1(self):
        print("Hey")

    def test_demo2(self):
       print("Hey")

    def test_demo3(self):
        print("Hey")


#In order for the report to print,
#use this  "py.test --html=report.html -s"
#a report is created in our project which we can open and check the status
