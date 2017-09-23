from django.conf.urls import url
from . import views

app_name='notes'
  
urlpatterns = [
    #mainpage
    url(r'^$', views.IndexView.as_view() , name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
     url(r'^registration/$', views.UserFormView1.as_view(), name='registration'),
   
    url(r'^login/$', views.UserFormLoginView.as_view(), name='login'),
   
    #page with ids
    #as detail view always expects a primary key so pk is written there
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view() , name='detail'),
    # /notes/album/add/
    url(r'album/add/$' ,views.AlbumCreate.as_view(),name='album-add'),    

      # /notes/album/2/
    url(r'album/(?P<pk>[0-9]+)/$' ,views.AlbumUpdate.as_view(),name='album-update'),    

      # /notes/album/2/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$' ,views.AlbumDelete.as_view(),name='album-delete'),    
   
      

]
if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     
