from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from posts.views import products_view, post_detail_view
from djangoProject import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello, name='hello'),
    path('now_date/', now_date, name='now_date'),
    path('goodbye/', goodbye, name='goodbye'),
    path('', main_view),
    path('posts/', products_view),
    path('posts/<int:id>/', product_detail_view)

]
