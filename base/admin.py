from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(List)
admin.site.register(Item)
admin.site.register(Inquire)
admin.site.register(Message)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(CartProduct)