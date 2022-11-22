from django.views.generic import DetailView, TemplateView
from app_pay.models import Item
from django.views import View
from django.http import JsonResponse
import stripe
from django.conf import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessView(TemplateView):
    template_name = 'app_pay/success.html'


class CancelView(TemplateView):
    template_name = 'app_pay/cancel.html'


class ItemDetailView(DetailView):

    model = Item
    template_name = 'app_pay/item_detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        contex = super(ItemDetailView, self).get_context_data(**kwargs)
        contex.update({
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return contex


class CreateCheckoutSessionView(View):

    def get(self, request, *args, **kwargs):
        item_id = self.kwargs['pk']
        item = Item.objects.get(id=item_id)
        YOUR_DOMAIN = 'http://127.0.0.1:8000'
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name,
                            #'images': ['Ссылка'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/'
        )
        return JsonResponse({
            'id': checkout_session.id
        })
