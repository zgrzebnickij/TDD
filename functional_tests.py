from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVistiorTests(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(3)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrive_it_later(self):
    self.browser.get("http://localhost:8000")

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

    # Typing "Buy spoon" into text box
    inputbox.send_keys("Buy spoon")

    # Updating page after hiting enter
    # Visible new item in list
    inputbox.send_keys(Keys.ENTER)

    table = self.browser.find_element_by_id("id_list_table")
    rows = self.browser.find_elements_by_tag_name("tr")
    self.assertIn('1: Buy spoon', [row.text for row in rows])

    # Stil visible text box
    # entering new todo
    inputbox = self.browser.find_element_by_id("id_new_item")
    inputbox.send_keys("Buy fork")
    inputbox.send_keys(Keys.ENTER)

    # second update on page and to wisible items
    table = self.browser.find_element_by_id("id_list_table")
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn('1: Buy spoon', [row.text for row in rows])
    self.assertIn('2: Buy fork', [row.text for row in rows])
    # Does the page remember items? Uniqe ulrs
    self.fail("finish the test")

if __name__ == "__main__":
  unittest.main(warnings='ignore')
