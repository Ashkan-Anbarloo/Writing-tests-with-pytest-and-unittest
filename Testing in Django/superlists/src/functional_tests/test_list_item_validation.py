from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import unittest
# from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.common.exceptions import WebDriverException
import os
from unittest import skip
from pathlib import Path
from .base import FunctionalTest


BASE_DIR = Path(__file__).resolve().parent.parent.parent


MAX_WAIT = 5


class ItemValidationTest(FunctionalTest):
    # @skip
    def test_cannot_add_empty_list_item(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element(By.ID , "id_new_item").send_keys(Keys.ENTER)

        self.assertEqual(self.browser.find_element(By.CSS_SELECTOR , ".invalid-feedback").text , "You can't have an empty list item")
        self.fail('finish this test!')
        self.wait_for(
            lambda: self.assertEqual(
                self.browser.find_element(By.CSS_SELECTOR , ".invalid-feedback").text , "You can't have an empty list item",)
        )
        self.browser.find_element(By.ID , "id_new_item").send_keys("purchase milk")
        self.browser.find_element(By.ID , "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("1: Purchase milk")

        self.browser.find_element(By.ID , "id_new_item").send_keys(Keys.ENTER)

        self.wait_for(
            lambda: self.assertEqual(
            self.browser.find_element(By.CSS_SELECTOR, ".invalid-feedback").text,
            "You can't have an empty list item",
            )
        )
        self.browser.find_element(By.ID, "id_new_item").send_keys("Make tea")
        self.browser.find_element(By.ID, "id_new_item").send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table("2: Make tea")
