from django.urls import path
from . import views
urlpatterns = [

    path('',views.homepage),
    path('ShowCakes/<cid>',views.ShowCakes),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Login',views.Login),
    path('SignUp',views.SignUp),
    path('Logout',views.Logout),
    path('addToCart',views.addToCart),
    path('ShowAllCartItems',views.ShowAllCartItems),
    path('MakePayment',views.MakePayment)
    
    
     
    
]
