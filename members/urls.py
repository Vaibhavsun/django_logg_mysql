from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[path('',views.main,name="main"),path('patients/',views.patient,name="patient"),path('doctors/',views.patient,name='patient'),path('patients/login',views.login,name='login'),path('doctors/login',views.login,name='login'),path('doctors/view_posts',views.to_show_doctors_blog,name='to_show_doctors_blog'),path('doctors/blog_posts',views.to_show_doctors_blog,name='to_show_doctors_blog'),path('patients/view_posts',views.to_show_doctors_blog,name='to_show_doctors_blog')]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
#here we can see the url for main view which is this / see patients and doctors both are poiinting to same view here login view can be seen which coming from both patients and doctors view
# here we are having urls which are pointing to blogs posts