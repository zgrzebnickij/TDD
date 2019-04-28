from selenium import webdriver
import unittest

class NewVistiorTests(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(4)

  def tearDown(self):
    self.browser.quit()

  def test_can_start_a_list_and_retrive_it_later(self):
    self.browser.get("http://localhost:8000")

    # Page title and header mention to-do list
    assert "To-Do" in self.browser.title

    # Invitation for entering to-do item

    # Typing "Buy spoon" into text box

    # Updating page after hiting enter
    # Visible new item in list

    # Stil visible text box
    # entering new todo

    # second update on page and to wisible items

    # Does the page remember items? Uniqe ulrs

if __name__ == "__main__":
  unittest.main(warnings='ignore')
