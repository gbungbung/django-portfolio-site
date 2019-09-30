from django.contrib import admin

from portfolio.models import Art, Hires, ArtCategory, Cv, CvCategory

admin.site.register(Art)
admin.site.register(Hires)
admin.site.register(ArtCategory)
admin.site.register(CvCategory)
admin.site.register(Cv)

