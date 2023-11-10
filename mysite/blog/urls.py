from django.urls import path

from blog.views import post_view

    #path('<slug:slug>/', post_view.PostDetail.as_view(), name='post_detail')

urlpatterns = [
	path('', post_view.PostView.as_view(), name='home'),
    path('<slug:slug>/', post_view.post_detail, name='post_detail')
]