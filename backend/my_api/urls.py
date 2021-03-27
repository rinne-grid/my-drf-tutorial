from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from my_api import views

urlpatterns = [
    path("snippets/", views.snippet_list),
    path("snippets/<int:pk>/", views.snippet_detail),
]

# 特定の形式を参照するためのシンプルできれいな方法を提供
# http://127.0.0.1/snippets.json
# http://127.0.0.1/snippets.api
urlpatterns = format_suffix_patterns(urlpatterns)
