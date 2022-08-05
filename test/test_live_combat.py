

import pytest
import yaml
import allure

class Calculator():
    def add(self,a,b):
        return a+b
    def redu(self,a,b):
        return a-b
    def div(self,a,b):
        return a / b
    def mul(self,a,b):
        return a*b

@pytest.fixture(scope='package')
def calculator():
    print("计算机初始化")
    cal = Calculator()
    yield cal
    print("输出操作")





class Test_Calculator():
    @pytest.mark.parametrize("a,b,c",[(1,2,3),(2,3,5),(3,7,10)])
    def test_add_calculator(self,a,b,c,calculator):
        assert calculator.add(a,b) == c

    @pytest.mark.parametrize("a,b,c", [(2, 2, 0), (3, 4, -1), (4, 7, -3)])
    def test_re_calculator(self,a,b,c,calculator):
        assert calculator.redu(a,b) == c

    @pytest.mark.parametrize("a,b,c", [(2, 0, 0), (3, 4, 12), (4, 7, 28)])
    def test_mul(self,a,b,c,calculator):
        assert calculator.mul(a,b) == c

    @pytest.mark.parametrize("a,b,c", [(3,1,3), (3, 2, 1.5), (12,2,6)])
    def test_div(self, a, b, c, calculator):
        assert calculator.div(a, b) == c


