from selenium import webdriver
from selenium.webdriver import ActionChains


browser = webdriver.Chrome(executable_path=r"C:\Users\Thomas\Desktop\ben\chromedriver.exe")


class ChromefoxTest:
    def __init__(self, url):
        self.url = url
        self.uri = []
        self.folder = "C:\\Users\\Thomas\\Desktop\\ben"

    def chromeTest(self):
        self.driver = webdriver.Chrome()
        actionChains = ActionChains(self.driver)
        self.driver.get(self.url)
        self.r = []
        self.r = self.driver.find_elements_by_tag_name("a")
        self.r = self.r[55:]
        for v in self.r:
            actionChains.context_click(v)
        actionChains.perform()
        for v in self.r:
            href = v.get_attribute("href")
            if href is not None:
                self.uri.append(href)
        self.uri = self.uri[:-7]
        with open('links.txt', 'w') as f:
            for item in self.uri:
                f.write("%s\n" % item)




if __name__ == '__main__':
    FT = ChromefoxTest(
        "https://www.google.com/search?q=unicorn+thomas+book+volcano&tbm=isch&ved=2ahUKEwjH9surr93uAhWSa6wKHTOQCRQQ2-cCegQIABAA&oq=unicorn+thomas+book+volcano&gs_lcp=CgNpbWcQAzoICAAQsQMQgwE6BQgAELEDOgIIADoHCAAQsQMQQzoECAAQQzoGCAAQCBAeOgQIABAYUOTCBliKqAdggKoHaABwAHgAgAFNiAHCC5IBAjI3mAEAoAEBqgELZ3dzLXdpei1pbWfAAQE&sclient=img&ei=AswiYMftJZLXsQWzoKagAQ&bih=578&biw=1280")
    FT.chromeTest()

