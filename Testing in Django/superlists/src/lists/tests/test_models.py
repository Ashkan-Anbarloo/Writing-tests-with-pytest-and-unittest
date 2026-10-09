from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item , List
import lxml.html


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

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), f'/lists/{list_.id}/')
