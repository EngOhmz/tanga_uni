# Register your models here.
from django.contrib import admin
from .models import Event, News, GalleryImage, Leader, ContactMessage, Member, Donation, Member

admin.site.register(Event)
admin.site.register(News)
admin.site.register(GalleryImage)
admin.site.register(Leader)
admin.site.register(ContactMessage)
# admin.site.register(Member)
admin.site.register(Donation)

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'phone', 'member_type', 'university_name', 'living_place']
    search_fields = ['full_name', 'email']
    list_filter = ['member_type']
