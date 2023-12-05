from django.contrib import admin
from .models import Livre

admin.site.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['nom', 'auteur', 'date_publication', 'note']