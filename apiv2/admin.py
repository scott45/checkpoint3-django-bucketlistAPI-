from django.contrib import admin
from .models import Bucketlist, Item


class BucketlistAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bucketlist, BucketlistAdmin)


class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, ItemAdmin)
