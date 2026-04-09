from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import MyUserCreationForm
# Create your views here.

class RegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')