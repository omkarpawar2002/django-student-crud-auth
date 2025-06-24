from django.urls import path
from .views import ( signup,signout,signin )

urlpatterns = [
    path('signup/',signup,name='signup'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='signout')
]