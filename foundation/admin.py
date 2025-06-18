from django.contrib import admin
from .models import Event, News, GalleryImage, Leader, ContactMessage, Member, Donation


# Register simple models
admin.site.register(Event)
admin.site.register(News)
admin.site.register(GalleryImage)
admin.site.register(Leader)
admin.site.register(Donation)

# ContactMessage admin customization
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'short_message', 'date_sent')
    search_fields = ('name', 'email', 'message')
    list_filter = ('date_sent',)

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message
    short_message.short_description = 'Message'




# Register Member model with custom admin and PDF export action
# @admin.register(Member)
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'email', 'phone', 'member_type', 'university_name', 'living_place')
#     search_fields = ('full_name', 'email')
#     list_filter = ('member_type',)
#     actions = [export_members_pdf]
