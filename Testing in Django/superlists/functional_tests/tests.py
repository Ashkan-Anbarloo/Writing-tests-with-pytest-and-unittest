from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 5
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
    
    def tearDown(self):
        self.browser.quit()

    # def test_can_start_a_todo_list(self):
    #     self.browser.get(self.live_server_url)

    def wait_for_row_in_list_table(self , row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID , 'id_list_table')
                rows = table.find_elements(By.TAG_NAME , 'tr')
                self.assertIn(row_text , [row.text for row in rows])
                # self.assertIn("foo", [row.text for row in rows])
                return 
            except(AssertionError , WebDriverException):
                if time.time() - start_time > MAX_WAIT:
                    raise
                time.sleep(0.5)

    # def check_for_row_in_list_table(self , row_text):
    #     table = self.browser.find_element(By.ID , "id_list_table")
    #     rows = table.find_elements(By.TAG_NAME , 'tr')
    #     self.assertIn(row_text , [row.text for row in rows])

    def test_can_start_a_todo_list(self):
        # self.browser.get('http://localhost:8000')
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do' , self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME , 'h1').text
        self.assertIn('To-Do' , header_text)

        inputbox = self.browser.find_element(By.ID , 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder') , 'Enter a to-do item')

        inputbox.send_keys('Buy peacock feathers')
        # inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(3)
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
        # self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(3)
        # table = self.browser.find_element(By.ID , 'id_list_table')
        # rows = table.find_elements(By.TAG_NAME , 'tr')

        # self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),f"New to-do item did not appear in table. Contents were:\n{table.text}",)
        # self.assertIn(
        # "2: Use peacock feathers to make a fly",
        # [row.text for row in rows],
        # )
        # self.assertIn(
        # "1: Buy peacock feathers",
        # [row.text for row in rows],
        # )
        #-----------
        self.wait_for_row_in_list_table("2: Use peacock feathers to make a fly")
        self.wait_for_row_in_list_table("1: Buy peacock feathers")
        
        
        #-----------
        # self.fail('Finish the test!')
        # [...rest of comments as before]

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID , 'id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy peacock feathers')

        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url , '/lists/.+')

        self.browser.delete_all_cookies()

        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element(By.TAG_NAME , 'body').text
        self.assertNotIn('Buy peacock feathers' , page_text)

        inputbox = self.browser.find_element(By.ID , 'id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url , '/lists/.+')
        self.assertNotEqual(francis_list_url , edith_list_url)

        page_text = self.browser.find_element(By.TAG_NAME , 'body').text
        self.assertNotIn('Buy peacock feathers' , page_text)
        self.assertIn('Buy milk' , page_text)


if __name__ == '__main__':
    unittest.main()



# browser = webdriver.Firefox()
# browser.get('http://localhost:8000')

# assert 'To-Do' in browser.title 
# browser.quit()