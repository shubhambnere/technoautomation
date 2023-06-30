from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group
from import_export.admin import ImportExportModelAdmin
from .models import  *
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from allauth.account.models import EmailAddress

from django.utils.html import format_html

admin.site.site_header = "Simply Shiksha"
admin.site.site_title = "Simply Shiksha"

admin.site.unregister(EmailAddress)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(User)
admin.site.unregister(Site)
admin.site.unregister(Group)



class InquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Product_Inquiry
    list_display = ('name', 'show_contact_no_url', 'show_email_url' )
    search_fields = ['name']
    # list_filter =['name']
    # list_editable = ['name']
    def show_email_url(self, obj):
        return format_html("<a href='mailto:{url}'>{url}</a>", url=obj.email)

    def show_contact_no_url(self, obj):
        return format_html(" {url} <a href='https://wa.me/91{url}'>   : Whatsapp </a> &nbsp;&nbsp;&nbsp; <a href='Tel:{url}'>Call Now</a> ", url=obj.contact_no)


class Product_InquiryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = Inquiry
    list_display = ('name', 'show_contact_no_url', 'show_email_url', 'product'  )

    search_fields = ['name']
    # list_filter =['name']
    # list_editable = ['name']
    def show_email_url(self, obj):
        return format_html("<a href='mailto:{url}'>{url}</a>", url=obj.email)

    def show_contact_no_url(self, obj):
        return format_html(" {url} <a href='https://wa.me/91{url}'>   : Whatsapp </a> &nbsp;&nbsp;&nbsp; <a href='Tel:{url}'>Call Now</a> ", url=obj.contact_no)


admin.site.register(Product_Inquiry, Product_InquiryAdmin)
admin.site.register(Inquiry, InquiryAdmin)