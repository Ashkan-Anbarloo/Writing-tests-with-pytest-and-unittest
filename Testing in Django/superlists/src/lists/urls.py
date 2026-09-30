from django.urls import path
# from lists.views import home_page
from lists import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path("", views.home_page, name="home"),
    path("new", views.new_list, name="new_list"),
    path("<int:list_id>/", views.view_list , name="view_list"),
    path('<int:list_id>/add_item' , views.add_item , name='add_item'),
]