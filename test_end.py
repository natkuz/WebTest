import time
import pytest
from testpage import OperationHelper
import logging
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def test_step_one(browser):
    logging.info("Test_one starting")
    test_page = OperationHelper(browser)
    test_page.go_to_site()
    test_page.enter_login(data.get('login'))
    test_page.enter_pass(data.get('password'))
    test_page.click_login_button()
    time.sleep(3)
    assert test_page.get_enter_text() == "Home", "test_step_one FAILED"


def test_step_two(browser):
    logging.info("Test_two starting")
    test_page = OperationHelper(browser)
    test_page.click_about_button()
    time.sleep(3)
    assert test_page.get_size_font() == "2em", "step_two FAILED"


if __name__ == '__main__':
    pytest.main(['-vv'])
