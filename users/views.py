from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.generic import DetailView, ListView,CreateView


from users.forms import UserForm
from .forms import UserForm

User = get_user_model()


class UserListView(ListView):
    template_name = "users/users_list.html"
    queryset = User.objects.all()


class UserDetailView(DetailView):
    template_name = "users/users_detail.html"
    queryset = User.objects.all()

class UserCreateView(CreateView): # новое изменение
    template_name = 'users/users_new.html'
    fields = User.objects.all()


def users_create(request):
    form = UserForm()
    return render(request, "users/users_update.html", {"form": form})


def users_new(request):
    form = UserForm()
    return render(request, 'users/users_edit.html', {'form': form})