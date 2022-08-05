import pytest
import yaml

class TestDemo():
    @pytest.mark.parametrize('env',yaml.safe_load(open('./data2.yml')))
    def test_demo(self,env):
        if 'test' in env:
            print(f"这是测试环境  {env}")
        if 'dev' in env:
            print("这是开发环境 %s" % env)
    def test_env(self):
        print(yaml.safe_load(open('./data2.yml')))
