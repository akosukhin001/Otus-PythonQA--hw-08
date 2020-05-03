import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--url', default='http://localhost', )
    parser.addoption('--browser', default='Chrome', choices=['Chrome', 'Firefox'])


@pytest.fixture
def browser_param(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    # print(url, browser)
    if browser == 'Chrome':
        # print('CH')
        options = webdriver.ChromeOptions()
        options.add_argument('start-maximized')
        options.add_argument('headless')
        wd = webdriver.Chrome(options=options)
    else:
        # print('FF')
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        # options.add_argument('-private')
        wd = webdriver.Firefox(options=options)
        wd.maximize_window()

    request.addfinalizer(wd.quit)
    return wd, url
