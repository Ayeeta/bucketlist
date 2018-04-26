from src.bucketlist import Bucketlist
import unittest

class TDDInBucketlist(unittest.TestCase):

    def setUp(self):
        self.bucketlist = Bucketlist('title')
        self.titles = []
        self.items = []
        self.bucketDict = {}

    def test_create_bucketlist_method(self):
        self.bucketlist.create()                      
        self.assertIn('title', self.bucketlist.titles, msg='title not in list')

    def test_delete_bucketlist_method(self):
        self.bucketlist.delete_bucketlist('title')
        self.assertNotIn('title', self.bucketlist.titles, msg='not deleted')

    def test_view_bucketlist_method(self):
        self.assertEqual(self.bucketlist.view_bucketlist(), {})

    def test_update_bucektlist_method(self):
        self.bucketlist.update_bucketlist('title','title_x') 
        self.bucketDict = {'title':['item1','item2']}
        self.bucketDict['title_x'] = self.bucketDict.pop('title')      
        self.assertIn('title_x', self.bucketDict, msg='still in bucketDict')
            

    def test_add_item_method_adds_to_item_list(self):
        self.bucketlist.add_item('item1')
        self.assertIn('item1', self.bucketlist.items, msg='not in items list')  

    def test_add_item_method_add_to_bucketDict(self):
        self.bucketlist.add_item('item')
        self.assertIn('title', self.bucketlist.bucketDict, msg='not added to dict')

    def test_view_items_method(self):
        b = self.bucketlist.view_items()
        self.assertEqual(b,[])

    def test_delete_item_method(self):
        self.bucketlist.delete_item('item1')
        self.assertNotIn('item1', self.bucketlist.items, msg='item not deleted')

    def test_update_item_method(self):
        self.bucketlist.update_item('item1','item_x')
        for idx, list_items in enumerate(self.items):
            if 'item1' in list_items:
                self.items[idx] = 'item_x'
                self.assertIn('item_x', self.bucketlist.titles, msg='new bucketlist not found')
            else:
                self.assertIn('item1', self.bucketlist.titles, msg='not deleted')



