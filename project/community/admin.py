from django.contrib import admin
# 게시글(Post) Model을 불러옵니다
from .models import Post
from .models import Financial
from .models import Notice
from .models import Donations_Report
from .models import History

# Register your models here.
# 관리자(admin)가 게시글(Post)에 접근 가능
admin.site.register(Post)
admin.site.register(Notice)
admin.site.register(Financial)
admin.site.register(Donations_Report)
admin.site.register(History)