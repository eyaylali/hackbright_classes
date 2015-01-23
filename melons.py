class AbstractMelon(object):
#create an exception if an instance of AbstractMelon is created

    def __init__(self):
        self.name = None
        self.color = None
        self.shape = 'natural'
        self.origin = False #domestic
        self.seasons = []

    def get_price(self, qty, base_price=5.00):
        if self.origin == True:
            base_price = base_price * 1.5
        if self.shape == 'square':
            base_price = base_price * 2
        return base_price * qty


class Watermelon(AbstractMelon):

    def __init__(self):
        super(Watermelon,self).__init__()
        self.name = "Watermelon"
        self.color = "green"
        self.seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        base_price = super(Watermelon, self).get_price(qty)
        if qty >= 3:
            return base_price * 0.75
        return base_price

class Cantaloupe(AbstractMelon):

    def __init__(self):
        super(Cantaloupe,self).__init__()
        self.name = "Cantaloupe"
        self.color = "tan"
        self.seasons = ["Spring", "Summer"]

    def get_price(self,qty):
        base_price = super(Cantaloupe, self).get_price(qty)
        if qty >= 5:
            return base_price * 0.5
        return base_price

class Casaba(AbstractMelon):

    def __init__(self):
        super(Casaba,self).__init__()
        self.name = "Casaba"
        self.color = "green"
        self.seasons = ['Spring', 'Summer', 'Fall', 'Winter']
        self.origin = True

    def get_price(self,qty):
        base_price = super(Casaba, self).get_price(qty,base_price=6.00)
        return base_price
        

def main():
    
    our_watermelon = Watermelon()
    our_canteloupe = Cantaloupe()
    our_casaba = Casaba()

    melons = [our_watermelon, our_canteloupe, our_casaba]

    for melon in melons:
        print "%s is the shape: %s" % (melon.name, melon.shape)
        print "%s is the color: %s" % (melon.name, melon.color)
        print "Two %ss cost $%.2f" % (melon.name, melon.get_price(2))
        print "Five %ss cost $%.2f" % (melon.name, melon.get_price(5))

main()