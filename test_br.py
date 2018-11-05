import pytest
import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://sportmaster.ru")
    assert "Спортмастер" in driver.title
    action = ActionChains(driver);
    menu1 = driver.find_element_by_id("newMenu")
    action.move_to_element(menu1).perform();
    menu2 = driver.find_element_by_xpath("//*[@id='newMenu']/ul/li[1]/span");
    action.move_to_element(menu2).perform();
    menu2.click();
    kurtki = driver.find_element_by_xpath("//*[@id='newMenu']/ul/li[1]/div/div[1]/div/div[1]/ul[1]/li[1]/a");
    kurtki.click();

class TextChecking(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = "https://www.sportmaster.ru/catalog/muzhskaya_odezhda/kurtki/"

    def is_text_present(self, text):
        return str(text) in self.driver.page_source

    def test_example(self):
        self.driver.get(self.base_url + "/")
        self.assertTrue(self.is_text_present("Показать по:"))