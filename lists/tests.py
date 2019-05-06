from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page
import re

class HomePageTest(TestCase):
   
  def test_root_url_resolve_to_home_page_viev(self):
    found = resolve("/")
    self.assertEqual(found.func, home_page)

  def test_home_page_returns_correct_html(self):
    request = HttpRequest()
    response = home_page(request)
    expected_html = render_to_string("home.html")
    self.assertTrue(response.content.decode(), expected_html)

  @staticmethod
  def remove_csrf(html_code):
      csrf_regex = r'<input[^>]+csrfmiddlewaretoken[^>]+>'
      return re.sub(csrf_regex, '', html_code)

  def assertEqualExceptCSRF(self, html_code1, html_code2):
      return self.assertEqual(
          self.remove_csrf(html_code1),
          self.remove_csrf(html_code2)
      )

  def test_home_page_can_save_a_POST_request(self):
    request = HttpRequest()
    request.method = "POST"
    request.POST["item_text"] = "A new list item"

    response = home_page(request)
    self.assertIn("A new list item", response.content.decode())
    expected_html = render_to_string( 
      "home.html",
      {"new_item_text": "A new list item"},
      request=request,
    )
    self.assertEqual(
      self.remove_csrf(response.content.decode()),
      self.remove_csrf(expected_html)
      )