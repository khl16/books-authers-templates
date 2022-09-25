from django.urls import path     
from . import views
urlpatterns = [
    path('add_book/',views.add_app),
    path('form_add',views.form_add),
    path('show/<int:book_id>',views.view ,name='show'),
    path('add_auther',views.add_auther),

]
