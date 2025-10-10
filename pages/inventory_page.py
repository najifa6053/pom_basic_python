import time 


class Inventory:
    def __init__(self, driver):
        self.driver = driver
        
    def current_url(self):
        time.sleep(1)
        return self.driver.current_url