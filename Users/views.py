from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView
from .forms import CreateUserForm
from .models import MyUser


class CreateUser(generic.CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'create_user.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        )
        myuser = MyUser.objects.create(user=user,
                                       profile_picture=data['profile_picture'],
                                       bio=data['bio']
                                       )
        return redirect('login')


class ProfilePage(DetailView):
    model = MyUser
    context_object_name = 'profile'
    template_name = 'profile.html'