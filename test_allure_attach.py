
import allure
import pytest
def test_text():
    allure.attach("这是一个文本",attachment_type=allure.attachment_type.TEXT)
    allure.attach("<body>你你你你你你你</body>",attachment_type=allure.attachment_type.HTML)
    allure.attach.file("E:\学习\赛事\学术搜索\领域.png",attachment_type=allure.attachment_type.PNG)
