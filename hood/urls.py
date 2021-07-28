from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("profile/",views.profile,name="profile"),
    path("business/",views.business,name="business"),
    path("post/",views.add_post,name="post"),
    path('register/',views.register,name='register'),
    path('logout/',views.logoutpage,name='logoutpage'),
    path('seach/',views.search_business,name='search')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)