from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from .models import Item
# Create your tests here.

# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1 , 2)

class HomePageTest(TestCase):
    # def test_home_page_return_correct_html(self):
    #     request = HttpRequest()
    #     response = home_page(request)
    #     html = response.content.decode('utf8')
    #     self.assertIn('<title>To-Do lists</title>' , html)
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertTrue(html.endswith('</html>'))
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # self.assertContains(response , '<title>To-Do lists</title>')
        # self.assertContains(response, "<html>")
        # self.assertContains(response, "</html>")
        self.assertTemplateUsed(response , 'home.html')
    
    # def test_render_homepage_conyent(self):
    #     response = self.client.get('/')
    #     self.assertContains(response , 'To-Do')

    def test_renders_input_form(self):
        response = self.client.get('/')
        self.assertContains(response , "<form method='POST'>")
        self.assertContains(response , 'name="item_text"')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/' , data={"item_text":"A new list item"})
        self.assertContains(response , "A new list item")
        self.assertTemplateUsed(response , 'home.html')

    
class ItemModel(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count() , 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text , 'the first (ever) list item')
        self.assertEqual(second_saved_item.text , 'Item the second')