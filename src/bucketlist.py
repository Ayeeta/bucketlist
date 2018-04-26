class Bucketlist(object):
    """Enable the user perform various operations on the bucketlist
        e.g create bucketlist and add bucketlist item
    """

    def __init__(self, title):
        self.title = title
        self.titles = []
        self.bucketDict = {}
        self.items = []

    def create(self): 
        self.titles.append(self.title)

    def delete_bucketlist(self, title):
        if title in self.titles:
            self.titles.remove(self.title)
    
    def view_bucketlist(self):
        return self.bucketDict

    def update_bucketlist(self, title, title_x):
        if title in self.bucketDict:
            self.bucketDict[title_x] = self.bucketDict.pop(title)
        return self.bucketDict

    def add_item(self, item):
        self.items.append(item)
        self.bucketDict[self.title] = self.items

    def view_items(self):
        return self.items

    def delete_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)

    def update_item(self, item1, item_x):
        for i, bucket_items in enumerate(self.items):
            if item1 in bucket_items:
                self.items[i] = item_x
        return self.items


    