from django.views.generic import TemplateView
from .models import Model1, Model2, Model3


class IndexTemplateView(TemplateView):
    template_name = 'example/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['model1'] = Model1.objects.all()
        context['model2'] = Model2.objects.all()
        context['model3'] = Model3.objects.all()
        return context
