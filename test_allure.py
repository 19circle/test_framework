import pytest
import allure

@allure.feature("测试功能名称")
@pytest.mark.parametrize('a,b',[(1+2,3),(3+4,7)])
def test_success(a,b):
    with allure.step("参数化步骤"):
        print(a+b)
        assert a == b


@allure.severity(allure.severity_level.NORMAL)
@allure.testcase('www.baidu.com','百度')
@allure.story("失败功能")
def test_failure():
    """this test fails"""
    assert True


# @allure.severity(allure.severity_level.MINOR)
@allure.story("跳过功能")
def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')

@allure.story("中断功能")
@allure.severity(allure.severity_level.BLOCKER)
def test_broken():
    raise Exception('oops')