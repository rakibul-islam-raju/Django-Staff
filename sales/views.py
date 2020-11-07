from django.shortcuts import render
from .models import Sale
from .utils import get_plot

# Create your views here.
def main_view(request):
    qs = Sale.objects.all()
    x = [x.item for x in qs]
    y = [y.price for y in qs]
    chart = get_plot(x, y)

    context = {
        'chart': chart
    }

    return render(request, 'sales/plot.html', context)
