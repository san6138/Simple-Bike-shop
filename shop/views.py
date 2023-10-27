
from django.views.decorators.http import require_GET
from django.views.generic import DetailView, ListView
from .models import *
from django.shortcuts import render
from .forms import OrderForm
from django.shortcuts import redirect

# Create your views here.
@require_GET
def bikeview(request):
    bikes = Bike.objects.all()
    return render(request, "available_bikes.html", {"bikes": bikes})

class BikeView(DetailView):
    model = Bike
    template_name = 'bike_detail.html'
    def get(self, request, *args, **kwargs):
        bike = self.get_object()
        form = OrderForm()
        if bike.tire.quantity > 1 and bike.frame.quantity and bike.seat.quantity:
            if bike.has_basket:
                baskets = Basket.objects.all()
                for basket in baskets:
                    if basket.quantity > 0:
                            break
                else:
                    return self.render_to_response({'object': bike})
            return self.render_to_response({'object': bike, 'form': form})
        return self.render_to_response({'object': bike})

class OrderListView(ListView):
    model = Order
    template = '/order_list.html'
    context_object_name = 'orders'

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            bike = Bike.objects.filter(id=request.POST['bike_id'])[0]
            bike.tire.quantity -= 2
            bike.frame.quantity -= 1
            bike.seat.quantity -= 1
            baskets = Basket.objects.all()
            for basket in baskets:
                if basket.quantity > 0:
                    basket.quantity -= 1
                    basket.save()
                    break
            order = Order.objects.create(surname=form.cleaned_data['surname'],
                                         phone_number=form.cleaned_data['phone_number'],
                                         name=form.cleaned_data['name'],
                                         bike=bike,
                                         status='P')
            return redirect(f'http://127.0.0.1:8001/order/{order.id}')



class OrderDetailView(DetailView):
    model = Order
    template = '/order_detail.html'
    context_object_name = 'order'