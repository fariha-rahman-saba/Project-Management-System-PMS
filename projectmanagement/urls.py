from django.urls import path
from . import views
from .views import HomeView, ProjectDetailView, AddProjectView, UpdateProjectView, DeleteProjectView,  LikeView, AddCommentView, ProjectVIew

urlpatterns = [
    path('about/', views.about, name="about"),
    path('', HomeView.as_view(), name="home"),
    path('project_view/', ProjectVIew.as_view(), name="project-view"),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='project-detail'),
    path('add_project/', AddProjectView.as_view(), name='add_project'),
    path('project/edit/<int:pk>', UpdateProjectView.as_view(), name='update_project'),
    path('project/<int:pk>/remove', DeleteProjectView.as_view(), name='delete_project'),
    path('like/<int:pk>', LikeView, name='like_project'),
    path('project/<int:pk>/comment/',
         AddCommentView.as_view(), name='add_comment'),
]
