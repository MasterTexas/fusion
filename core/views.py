from django.views.generic import FormView
from .models import Servico, Colaborador, Caracteristica, Preco
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['colaboradores'] = Colaborador.objects.all()
        context['caracteristicas'] = Caracteristica.objects.all()
        context['precos'] = Preco.objects.all()
        return context

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Erro ao enviar o email!')
        return super().form_invalid(form)