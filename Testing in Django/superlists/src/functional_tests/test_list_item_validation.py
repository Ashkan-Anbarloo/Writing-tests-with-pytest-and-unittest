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
        self.fail('write me!')
