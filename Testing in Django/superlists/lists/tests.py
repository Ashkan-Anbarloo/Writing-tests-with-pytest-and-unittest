from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from .models import Item , List
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
        self.assertContains(response , "<form method='POST' action='/lists/new'>")
        self.assertContains(response , 'name="item_text"')
    
    # def test_display_all_list_items(self):
    #     Item.objects.create(text='itemey 1')
    #     Item.objects.create(text='itemey 2')

    #     response = self.client.get('/')

    #     self.assertContains(response , 'itemey 1')
    #     self.assertContains(response , 'itemey 2')

    # def test_can_save_a_POST_request(self):
    #     # response = self.client.post('/' , data={"item_text":"A new list item"})

    #     # self.assertEqual(Item.objects.count() , 1)
    #     # new_item = Item.objects.first()
    #     # self.assertEqual(new_item.text , 'A new list item')

    #     # self.assertRedirects(response , '/')
    #     self.client.post("/", data={"item_text": "A new list item"})
    #     self.assertEqual(Item.objects.count(), 1)
    #     new_item = Item.objects.first()
    #     self.assertEqual(new_item.text, "A new list item")
    
    # def test_redirects_after_POST(self):
    #     response = self.client.post("/", data={"item_text": "A new list item"})
    #     self.assertRedirects(response, "/lists/the-only-list-in-the-world/")
    
    # def test_only_saves_items_when_necessary(self):
    #     self.client.get('/')
    #     self.assertEqual(Item.objects.count() , 0)


class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):
        self.client.post('/lists/new' , data={'item_text' : 'A new list item'})
        self.assertEqual(Item.objects.count() , 1)
        new_item = Item.objects.get()
        self.assertEqual(new_item.text , 'A new list item')
    
    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new' , data={'item_text' : 'A new list item'})
        new_list = List.objects.get()
        self.assertRedirects(response , f'/lists/{new_list.id}/')
        


class ListViewTest(TestCase):
    def test_uses_list_template(self):
        mylist = List.objects.create()
        response = self.client.get(f'/lists/{mylist.id}/')
        self.assertTemplateUsed(response , 'list.html')


    def test_renders_input_form(self):
        mylist = List.objects.create()
        response = self.client.get(f'/lists/{mylist.id}/')
        self.assertContains(response , f"<form method='POST' action='/lists/{mylist.id}/add_item'>")
        # self.assertContains(response , '<input name="item_text">')
        self.assertContains(response , 'name="item_text"')

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


    
class ListAndItemModelsTest(TestCase):
    def test_saving_and_retrieving_items(self):
        mylist = List()
        mylist.save()

        first_item = Item()
        first_item.text = 'the first (ever) list item'
        first_item.list = mylist
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = mylist
        second_item.save()

        saved_list = List.objects.get()
        self.assertEqual(saved_list , mylist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count() , 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text , 'the first (ever) list item')
        self.assertEqual(first_saved_item.list , mylist)
        self.assertEqual(second_saved_item.text , 'Item the second')
        self.assertEqual(second_saved_item.list , mylist)

    # def test_can_save_multiple_item(self):
    #     self.client.post('/' , data={'item_text':'first item'})
    #     response = self.client.post('/' , data={'item_text':'second item'})
    #     self.assertContains(response , 'first item')
    #     self.assertContains(response , 'secend item')


class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        self.client.post(
            f"/lists/{correct_list.id}/add_item",
            data={"item_text": "A new item for an existing list"},
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
            data={"item_text": "A new item for an existing list"},
        )
        self.assertRedirects(response, f"/lists/{correct_list.id}/")