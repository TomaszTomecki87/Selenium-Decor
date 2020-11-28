import pytest
from selenium import webdriver

@pytest.fixture()
def setUp():
    print("\nRunning method level setUp")
    yield
    print("\nRunning method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    if browser == 'chrome':
        #opt = webdriver.ChromeOptions()
        #opt.add_argument('user-data-dir=C:\\Users\\TT\\AppData\\Local\\Google\\Chrome\\User Data\\Default')
        baseURL = 'https://letskodeit.com/automationpractice/'
        driver = webdriver.Chrome()
        #driver = webdriver.Chrome(options=opt)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        #print('Running tests on Chrome')

    elif browser == 'firefox':
        #opt = webdriver.FirefoxOptions()
        #opt.add_argument('user-data-dir=C:\\Users\\Tomek\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\da59ftip.default-release')
        baseURL = 'https://letskodeit.com/automationpractice/'
        driver = webdriver.Firefox()
        #driver = webdriver.Firefox(options=opt)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        #print("Running tests on FF")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("\nRunning one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")