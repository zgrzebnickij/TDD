from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistiorTests(StaticLiveServerTestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(2)

  def tearDown(self):
    self.browser.quit()

  def check_for_row_in_table(self, row_text):
    table = self.browser.find_element_by_id("id_list_table")
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn(row_text, [row.text for row in rows])

  def test_can_start_a_list_and_retrive_it_later(self):
    self.browser.get(self.live_server_url)

    # Page title and header mention to-do list
    assert "To-Do" in self.browser.title
    header_text = self.browser.find_element_by_tag_name("h1").text
    self.assertIn("To-Do", header_text)

    # Invitation for entering to-do item
    inputbox = self.browser.find_element_by_id("id_new_item")
    self.assertEqual(
      inputbox.get_attribute("placeholder"),
      "Enter a to-do item"
    )

    # Typing "Buy spoon" into text box by Edith
    inputbox.send_keys("Buy spoon")

    # Updating page after hiting enter
    # Visible new item in list
    inputbox.send_keys(Keys.ENTER)
    edith_list_url = self.browser.current_url
    print(edith_list_url)
    self.assertRegex(edith_list_url, "/lists/.+")
    self.check_for_row_in_table("1: Buy spoon")

    # Stil visible text box
    # entering new todo
    inputbox = self.browser.find_element_by_id("id_new_item")
    inputbox.send_keys("Buy fork")
    inputbox.send_keys(Keys.ENTER)

    # second update on page and to wisible items of Edith
    self.check_for_row_in_table('1: Buy spoon')
    self.check_for_row_in_table('2: Buy fork')

    # Does the page remember items? Uniqe ulrs
    # Ues new session to make sure no information
    # is comming from cookies
    self.browser.quit()
    self.browser = webdriver.Chrome()

    # Adam visit the home page. there is no sign of eddit's
    # list
    self.browser.get(self.live_server_url)
    page_text = self.browser.find_element_by_tag_name("body").text
    self.assertNotIn("Buy spoon", page_text)
    self.assertNotIn("Buy fork", page_text)

    # Adam start new list by entering a new item
    inputbox = self.browser.find_element_by_id("id_new_item")
    inputbox.send_keys("Buy milk")
    inputbox.send_keys(Keys.ENTER)

    # Adam get his own unique URL
    adam_list_url = self.browser.current_url
    self.assertRegex(adam_list_url, "/lists/.+")
    self.assertNotEqual(adam_list_url, edith_list_url)
    
    # there is no trace of edith's list
    page_text = self.browser.find_element_by_tag_name("body").text
    self.assertNotIn("Buy spoon", page_text)
    self.assertIn("Buy milk", page_text)

    # satisfied, the both go to sleep
  
  def test_layout_and_styling(self):
    #Adam goest to the home page
    self.browser.get(self.live_server_url)
    self.browser.set_window_size(1024, 768)

    #He noticed the input box is nicely centered
    inputbox = self.browser.find_element_by_id("id_new_item")
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=8
    )
    # She starts a new list and sees the input is nicely
    # centered there too
    inputbox.send_keys('testing\n')
    inputbox = self.browser.find_element_by_id('id_new_item')
    self.assertAlmostEqual(
      inputbox.location['x'] + inputbox.size['width'] / 2,
      512,
      delta=8
    )
