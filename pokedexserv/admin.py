from django.contrib import admin
from .models import PokemonServ
# Register your models here.


class PokemonServAdmin(admin.ModelAdmin):
    readonly_fields=("created","updated")

admin.site.register(PokemonServ,PokemonServAdmin)


