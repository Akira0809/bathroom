from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from . forms import UserCreateForm
from . import forms
from account.models import Data, User

class TopView(TemplateView):
    template_name = "account/top.html"
    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "account/home.html"

    def get(self, request, *args, **kwargs):
        data = Data.objects.first()
        b = list(data.big)
        s = list(data.small)
        user = User.objects.get(user=request.user)
        user_choise = user.button
        context = {
            'radio_selection': user_choise,
            'b0': b[0],
            'b1': b[1],
            'b2': b[2],
            'b3': b[3],
            'b4': b[4],
            'b5': b[5],
            'b6': b[6],
            'b7': b[7],
            'b8': b[8],
            'b9': b[9],
            'b10': b[10],
            'b11': b[11],
            's0': s[0],
            's1': s[1],
            's2': s[2],
            's3': s[3],
            's4': s[4],
            's5': s[5],
            's6': s[6],
            's7': s[7],
            's8': s[8],
            's9': s[9],
            's10': s[10],
            's11': s[11]
        }
        return self.render_to_response(context)

class LoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "account/login.html"

class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = "account/login.html"

class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'account/create.html', {'form': form,})
    
    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return render(request, 'account/create.html', {'form': form,})


def data_view(request):
    if request.method == 'POST':
        myradio = request.POST.get("my_radio")
        data = Data.objects.first()
        user = User.objects.get(user=request.user)
        user.button = myradio
        user.save()
        big = list(data.big)
        small = list(data.small)
        if (myradio == None):
            data = Data.objects.first()
            user = User.objects.get(user=request.user)
            user_choise = user.button
            b = list(data.big)
            s = list(data.small)
            return render(request, 'account/home.html', {
                'radio_selection': user_choise,
                'b0': b[0],
                'b1': b[1],
                'b2': b[2],
                'b3': b[3],
                'b4': b[4],
                'b5': b[5],
                'b6': b[6],
                'b7': b[7],
                'b8': b[8],
                'b9': b[9],
                'b10': b[10],
                'b11': b[11],
                's0': s[0],
                's1': s[1],
                's2': s[2],
                's3': s[3],
                's4': s[4],
                's5': s[5],
                's6': s[6],
                's7': s[7],
                's8': s[8],
                's9': s[9],
                's10': s[10],
                's11': s[11]
            })
        if (myradio[0] == 'b'):
            big[int(myradio[1:])]+=1
        else:
            small[int(myradio[1:])]+=1
        data = Data.objects.first()
        data.big = list(big)
        data.small = list(small)
        data.save()
        b = list(data.big)
        s = list(data.small)
        user_choise = user.button

    return render(request, 'account/home.html', {
        'radio_selection': user_choise,
        'b0': b[0],
        'b1': b[1],
        'b2': b[2],
        'b3': b[3],
        'b4': b[4],
        'b5': b[5],
        'b6': b[6],
        'b7': b[7],
        'b8': b[8],
        'b9': b[9],
        'b10': b[10],
        'b11': b[11],
        's0': s[0],
        's1': s[1],
        's2': s[2],
        's3': s[3],
        's4': s[4],
        's5': s[5],
        's6': s[6],
        's7': s[7],
        's8': s[8],
        's9': s[9],
        's10': s[10],
        's11': s[11]
    })
