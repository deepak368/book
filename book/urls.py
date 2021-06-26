"""productProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.shortcuts import render
from .views import UserRegisterView,UserLoginView,User_logout,Create_Bookview,List_Book,bookDeleteView,bookEditView,\
    Adminpage,Search_view,order_view,cart

urlpatterns = [
    path("home",lambda request:render(request,"book/base.html"),name="homepage"),
    path("",UserLoginView.as_view(),name="login"),
    path("register",UserRegisterView.as_view(),name="register"),
    path("logout",User_logout,name="logout"),
    path("error",lambda request:render(request,"book/error.html"),name="error"),
    path("createbook",Create_Bookview.as_view(),name="create"),
    path("book/list",List_Book.as_view(),name="list"),
    path("admin-page",lambda request:render(request,"book/adminpage.html"),name="admin-page"),
    path("admin-auction",Adminpage.as_view(),name="admin"),
    path("book-edit/<int:pk>",bookEditView.as_view(),name="edit"),
    path("book-delete/<int:pk>",bookDeleteView.as_view(),name="delete"),
    path("search", Search_view, name="searchbook"),
    path("order/<int:id>",order_view,name="order"),
    path("cart",cart,name="cart")

    ]