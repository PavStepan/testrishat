from django.urls import path
from app_pay.views import ItemDetailView, CreateCheckoutSessionView, SuccessView, CancelView

urlpatterns = [
    path('buy/<int:pk>/', CreateCheckoutSessionView.as_view(), name='buy'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),

]
