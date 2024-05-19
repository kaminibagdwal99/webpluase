from django.conf import settings
from django.db import models
from django.shortcuts import reverse


CATEGORY_CHOICES = (
    ('12','12 MONTH'),
    ('01','1 MONTH'),
    ('03','3 MONTH'),
    ('06','6 MONTH')
)

LABEL =(
    ('p','primary'),
    ('s','secondary'),
    ('d','danger')


)
class Package(models.Model):
    name = models.CharField(max_length =100)
    description = models.TextField(max_length=200)


    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(max_length=1000)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2, null = True, default='12')
    label = models.CharField(choices=LABEL,max_length=1, default='p')
    discounted_price = models.FloatField(max_length=1000)
    package = models.ManyToManyField(Package)
    slug = models.SlugField(default = '')
    description = models.TextField(default = False)
    image = models.ImageField(default = False)



    def __str__(self):
        return self.title

    
    def get_absolute_url(self):
        return reverse("core:product", kwargs={
            'slug': self.slug
        })

    
    def get_add_to_cart_url(self):
        return reverse("core:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("core:remove-from-cart", kwargs={
            'slug': self.slug
        })

        


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,blank = True, null= True)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Item,on_delete=models.CASCADE )
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discounted_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discounted_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default = False)


    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total




    