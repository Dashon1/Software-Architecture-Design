from inventory import inventory

class cart:
    #the main thing here is that I wanted the shopping cart to keep track of the items in the cart by appending to a list of item objects so first we need to import the item class I drafted up
    def __init__(self):
        self.total = 0
        self.items = []
        self.itemNum = 0
        self.inv = inventory()
    
    def getTotal(self):
        return self.total

    #this should append the added item to the list
    # I was thinking about returning the index of the item added for use with the remove function but was undecided at the time
    def additem(self, item):
        #make sure stock isn't empty
        if (self.inv.get_stock(item.get_name()) <= 0):
            return False
        else:
            #add item to items array
            self.items.append(item)
            return True

        #update total
        self.total += item.get_price(item.get_name())

        #update inventory
        self.inv.rm_stock(item.get_name())

    #this should remove the iem from the lsit
    def rmitem(self, item):
        #rm item from items array
        #update total
        #update item number