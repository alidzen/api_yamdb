from django.urls import path, include
from rest_framework.routers import DefaultRouter

from socials.views import ReviewView, CommentView

v1_router = DefaultRouter()
v1_router.register(r'reviews', ReviewView, basename='reviews')
v1_router.register(r'reviews/(?P<review_id>\d+)/comments', CommentView, basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls))
]