from django.urls import path
from . import views
# from .views import PostListView, PostDetailView, PostEditView, PostDeleteView, CommentDeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('settings', views.settings, name='settings'),
    path('upload', views.upload, name='upload'),
    path('follow', views.follow, name='follow'),
    path('search', views.search, name='search'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('like-post', views.like_post, name='like-post'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    # path('post/<int:pk>/', views.get, name='post-detail'),
    # path('post/<int:pk>/', views.post, name='post-detail'),
    path('post/<str:pk>/', views.post_detail, name='post_detail'),

]