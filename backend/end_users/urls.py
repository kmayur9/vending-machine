from django.urls import path
from end_users import views


urlpatterns = [
	path('products/', views.ProductApiView.as_view()),
	path('denominations/', views.DenominationApiView.as_view()),
	path('orders/', views.OrderApiView.as_view()),
]
