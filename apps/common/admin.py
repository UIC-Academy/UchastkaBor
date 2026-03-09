from django.contrib import admin

from apps.common.models import State, Region, Currency, Media


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "state",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
        "state",
    ]
    list_filter = [
        "state",
    ]


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
    ]
    search_fields = [
        "name",
    ]
    fields = [
        "name",
    ]


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "file",
    ]
    search_fields = [
        "file",
    ]
    fields = [
        "file",
    ]