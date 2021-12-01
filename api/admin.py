from django.contrib import admin
from .models import Digital_assets_inventory, Profile, Agreement, Agreement_type, Role, Service_provider, Receiving_UNEP_division

# Register your models here.
admin.site.register(Profile)
admin.site.register(Role)
admin.site.register(Agreement)
admin.site.register(Agreement_type)
admin.site.register(Service_provider)
admin.site.register(Receiving_UNEP_division)
admin.site.register(Digital_assets_inventory)

