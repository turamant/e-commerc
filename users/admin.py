from django.contrib import admin

from .models import VerifyCode


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "Mu Student Fresh Background"
    site_footer = "mxshop"
    # menu_style = "accordion"

@admin.register(VerifyCode)
class VerifyCodeAdmin(admin.ModelAdmin):
    list_display = ['code', 'mobile', "add_time"]


