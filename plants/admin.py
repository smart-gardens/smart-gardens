from django.contrib import admin

from .models import Cultivar, Family, Genus, Species

admin.site.register(Family)
admin.site.register(Species)
admin.site.register(Cultivar)
admin.site.register(Genus)
