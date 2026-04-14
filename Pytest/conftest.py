#conftest files are generalized fixtures. When we call them in any test case of any file in that particular project, they are executed.
#Usually we need such fixtures in order to invoke browsers. Instead of everytime invoking by writing code, we can have a generalized fixture which we can call upon
#If we want the fixture only to repeat once when given at class level, we can give, scope='class' as argument
#If not mentioned anything, it is default applied at method level
import pytest


@pytest.fixture(scope='class')
def setup():
    print("Hello to Everyone")


@pytest.fixture()
def dataload():
    print("tuple data is returned")
    return ["Manasa", "Commandeer", "abc@gmail.com"]

#parameterization can be done with written statements in tuple formats
@pytest.fixture(params=[("one", "two"),("three", "four", "five"), "six"])
def multiple(request):
    return request.param
