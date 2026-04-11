from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MyUserCreationForm, UserProfileForm
from .models import User
from interactions.models import Like
# Create your views here.

class RegisterView(CreateView):
    form_class = MyUserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, ListView):
    template_name = 'users/profile.html'
    context_object_name = 'user_likes'
    
    def get_queryset(self):
        return Like.objects.filter(user=self.request.user).prefetch_related('anime', 'manga')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user