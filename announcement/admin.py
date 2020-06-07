from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import Announcement


class AnnouncementAdmin(SummernoteModelAdmin, TranslationAdmin):
    list_display = ('id', 'title_ko', 'title_en',)
    ordering = ('id',)
    search_fields = ('title',)


admin.site.register(Announcement, AnnouncementAdmin)
