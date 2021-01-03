"""firstbike URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from firstapp.views import basefile,signuppage,products,loginpage,homepage,testpage,bookingpage,aboutuspage,contactuspage,findbikepage,savedata,savelogin,savesignup
urlpatterns = [
    path('admin/', admin.site.urls),
    path('basefile/',basefile, name="basefile"),
    path("signuppage/",signuppage , name="signuppage"),
    path('loginpage/', loginpage, name="loginpage"),
    path('homepage/', homepage, name="homepage"),
    path('bookingpage/', bookingpage, name="bookingpage"),
    path('aboutuspage/', aboutuspage, name="aboutuspage"),
    path('contactuspage/', contactuspage, name="contactuspage"),
    path('findbikepage/', findbikepage, name="findbikepage"),
    path('savedata/',savedata , name="savedata"),
    path('savelogin/',savelogin , name="savelogin"),
    path('savesignup/',savesignup , name="savesignup"),
    path('testpage/',testpage, name="testpage"),
    path('products/<int:id>',products,name="products")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
