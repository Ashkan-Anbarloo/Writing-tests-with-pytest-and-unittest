from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item , List
import lxml.html
import html
from django.urls import reverse 
from lists.forms import EMPTY_ITEM_ERROR
# Create your tests here.

# class SmokeTest(TestCase):
#     def test_bad_math(self):
#         self.assertEqual(1+1 , 2)

class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response , 'home.html')
    
    def test_renders_input_form(self):
        response = self.client.get('/')
        parsed = lxml.html.fromstring(response.content)
        [form] = parsed.cssselect('form[method=POST]')
        self.assertEqual(form.get('action') , "/lists/new")
        [input] = form.cssselect('input[name=text]')
        inputs = form.cssselect('input')
        self.assertIn('text' , [input.get('name') for input in inputs])
        # self.assertContains(response , "<form method='POST' action='/lists/new'>")
        # self.assertContains(
        #     response,
        #     '<input name="item_text" id="id_new_item" placeholder="Enter a to-do item" />',
        #     html=True,
        # )

    
    
class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new' , data={'text' : 'A new list item'})
        self.assertEqual(Item.objects.count() , 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text , 'A new list item')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new' , data={'text' : 'A new list item'})
        new_list = List.objects.get()
        self.assertRedirects(response , f'/lists/{new_list.id}/')
    
    def post_invalid_input(self):
        return self.client.post('/lists/new' , data={'text':""})
    
    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(), 0)
    

    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_for_invalid_input_shows_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, html.escape(EMPTY_ITEM_ERROR))

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        mylist = List.objects.create()
        response = self.client.get(f'/lists/{mylist.id}/')
        self.assertTemplateUsed(response , 'list.html')


    def test_renders_input_form(self):
        mylist = List.objects.create()
        response = self.client.get(f'/lists/{mylist.id}/')
        parsed = lxml.html.fromstring(response.content)
        [form] = parsed.cssselect("form[method=POST]")
        self.assertEqual(form.get('action') , f"/lists/{mylist.id}/add_item")
        [input] = form.cssselect("input[name=text]")
        # self.assertContains(response, f'<form method="POST" action="/lists/{mylist.id}/add_item">')
        # self.assertContains(
        #     response , 
        #     '<input name="item_text" id="id_new_item" placeholder="Enter a to-do item" />',
        #     html=True,                   
        # )

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1' , list=correct_list)
        Item.objects.create(text='itemey 2' , list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item' , list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertContains(response , 'itemey 1')
        self.assertContains(response , 'itemey 2')
        self.assertNotContains(response , 'other list item')
    
    def test_display_all_list_items(self):
        mylist = List.objects.create()
        Item.objects.create(text = 'itemey 1' , list=mylist)
        Item.objects.create(text = 'itemey 2' , list=mylist)

    def post_invalid_input(self):
        mylist = List.objects.create()
        return self.client.post(f"/lists/{mylist.id}/", data={"text": ""})
    
    def test_for_invalid_input_nothing_saved_to_db(self):
        self.post_invalid_input()
        self.assertEqual(Item.objects.count(), 0)

    def test_for_invalid_input_renders_list_template(self):
        response = self.post_invalid_input()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "list.html")

    def test_for_invalid_input_shows_error_on_page(self):
        response = self.post_invalid_input()
        self.assertContains(response, html.escape(EMPTY_ITEM_ERROR))

    

class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(
            f"/lists/{correct_list.id}/add_item",
            data={"text": "A new item for an existing list"},
        )
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text, "A new item for an existing list")
        self.assertEqual(new_item.list, correct_list)


    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.post(
            f"/lists/{correct_list.id}/add_item",
            data={"text": "A new item for an existing list"},
        )
        self.assertRedirects(response, f"/lists/{correct_list.id}/")