from django.urls import path
from . import views
urlpatterns=[
    path('',views.MarketPlace.as_view(), name='marketplace'),
    path('<slug:vendor_slug>/',views.VendorDetail.as_view(), name="vendor_detail")
]