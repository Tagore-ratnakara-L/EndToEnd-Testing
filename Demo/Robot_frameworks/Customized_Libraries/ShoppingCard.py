import time

from robot.api.deco import library, keyword
from robot.libraries.BuiltIn import BuiltIn


# instead of importing selenium package and writing for webdriver again
# you can import already Built in robot package to drive it directly by methods

@library
class ShoppingCard():
    def __init__(self):
        self.selenlib = BuiltIn().get_library_instance("SeleniumLibrary")

    # method name wil be converted to Keyword name
    @keyword
    def hello_world(self):
        print("Hello World!")

    @keyword
    def add_item_to_cart_and_checkout(self, ListOfProducts):
        # ${elements}=    Get WebElements    css:.card-title
        # for Get WebElements hover over to main robot file it will get the basic python
        # method defined in package/library assign it below instance
        i = 1

        Products_titles=self.selenlib.get_webelements("css:.card-title")
        # for i in range(len(Products_titles)):
        #     n = i + 1
        #     if ListOfProducts == Products_titles[i].text:
        #         self.selenlib.click_element("xpath:(//*[@class='card-footer'])["+str(n)+"]/button")
        for productTitle in Products_titles:
            if productTitle.text in ListOfProducts:
                self.selenlib.click_button("xpath:(//*[@class='card-footer'])["+str(i)+"]/button")
            i = i+1
        time.sleep(3)
        self.selenlib.wait_until_element_is_visible("css:.nav-link.btn.btn-primary")
        time.sleep(1)
        self.selenlib.click_element("css:.nav-link.btn.btn-primary")
