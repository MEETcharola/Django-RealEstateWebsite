from django.contrib import admin
from .models import Property_Residential, Property_Commercial, Property_Plot, Property_PG, Property_Images

admin.site.register(Property_Residential)
admin.site.register(Property_Commercial)
admin.site.register(Property_Plot)
admin.site.register(Property_PG)
admin.site.register(Property_Images)

