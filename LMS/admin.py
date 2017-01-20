from django.contrib import admin
from .models import Language,Locale_String,Locale_String_History
# Register your models here.

# class LanguageAdmin(admin.ModelAdmin):
#     list_display = ('language_name','language_description')
#
#
#
# class LocaleStringAdmin(admin.ModelAdmin):
#     #list_display = ('language_name','localestring_Id','localestring_value','last_updated_date')
#
#     list_display = ('language_name','localestring_Id')
#
#     def language_name(self, instance):
#         return instance.language.language_name

admin.site.register(Language)
admin.site.register(Locale_String)
admin.site.register(Locale_String_History)
