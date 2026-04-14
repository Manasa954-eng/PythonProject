#dataload is a fixture which is defined at global level and also at method level
#method level is defined because te fixture has to return something. When nothing needs to be returned, only global level is enough
#But when something is need to be returned, then we need them at method level too

import pytest


@pytest.mark.usefixtures("dataload")
class Testexemple:

    def test_one(self, dataload):
        print(dataload[0])
        print(dataload[1])

@pytest.mark.usefixtures
def test_two(multiple):
    print(multiple[0])

