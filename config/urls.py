from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home_page.urls')),
    path('account/', include('account.urls')),
    path('user/', include('user_profile.urls')),
    path('my-learning', include('my_learning.urls')),
    path('home-work', include('home_work.urls')),
    path('sub-admin/', include('sub_admin_profile.urls')),
    path('blog/', include('blogs_page.urls')),
    path('about/', include('about_page.urls')),
    path('contact/', include('contact_page.urls')),
    path('course/', include('courses_page.urls')),
    path('faq/', include('FAQ_page.urls')),
    path('support/', include('support_page.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
