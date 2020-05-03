def test_opencart(browser_param):
    wd, url = (browser_param)
    # print(url, wd)
    wd.get(url)
    page_title = wd.title
    assert page_title == 'Your Store'
