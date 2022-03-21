from decimal import Decimal

from store.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, product_qty):
        product_id = str(product.id)
        qty = product_qty

        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}

        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['qty'] for item in self.basket.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * Decimal(item['qty']) for item in self.basket.values())

    def delete(self, product_id):
        """
        Delete item from session data
        """
        print(product_id)
        product = str(product_id)
        if product in self.basket:
            print("product id:", product, "is in self.basket")
            del self.basket[product]

        self.save()
            
    def save(self):
        self.session.modified = True
        
    def update(self, product, qty):
        product_id = str(product)
        
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()

