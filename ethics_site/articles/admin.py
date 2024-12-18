from django.contrib import admin
from .models import Article, HomePageInfo, Comment, ContactSubmission, Video, CommunityCategory

admin.site.register(HomePageInfo)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(ContactSubmission)
admin.site.register(Video)
admin.site.register(CommunityCategory)
