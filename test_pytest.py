import pytest

def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
def test_answer1():
    assert inc(4) == 5
@pytest.fixture()
def login():
    print("登录操作")
class Testyear():
    @pytest.mark.parametrize('input,expr',[(1,2),(2+4,6),(6*9,54)])
    def test_a(self,input,expr,login):
        assert input ==expr
    def test_b(self):
        print('b')
    def test_c(self,login):
        print('c')
    def c(self):
        print('我就试一试你可不可以')

