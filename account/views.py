from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView, CreateView
from django.shortcuts import render, redirect
from . forms import UserCreateForm
from . import forms
from account.models import Data, User
from django_user_agents.utils import get_user_agent

class TopView(TemplateView):
    template_name = "account/top.html"
    def get(self, request, *args, **kwargs):
        return self.render_to_response({})

class HomeView(LoginRequiredMixin, TemplateView):
    def get(self, request, *args, **kwargs):
        user_agent = get_user_agent(request)
        data = Data.objects.first()
        b = list(data.big)
        s = list(data.small)
        bm = list(data.big_maximum)
        sm = list(data.small_maximum)
        try:
            user = User.objects.get(user=request.user)
        except:
            user = User(user=request.user, button="a")
            user.save()
        user_choise = user.button
        context = {
            'radio_selection': user_choise,
            'bm0': bm[0],
            'bm1': bm[1],
            'bm2': bm[2],
            'bm3': bm[3],
            'bm4': bm[4],
            'bm5': bm[5],
            'bm6': bm[6],
            'bm7': bm[7],
            'bm8': bm[8],
            'bm9': bm[9],
            'bm10': bm[10],
            'bm11': bm[11],
            'sm0': sm[0],
            'sm1': sm[1],
            'sm2': sm[2],
            'sm3': sm[3],
            'sm4': sm[4],
            'sm5': sm[5],
            'sm6': sm[6],
            'sm7': sm[7],
            'sm8': sm[8],
            'sm9': sm[9],
            'sm10': sm[10],
            'sm11': sm[11],
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

        if user_agent.is_mobile:
            return render(request, "account/home_mobile.html", context)
        else:
            return render(request, "account/home.html", context)

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
        user_agent = get_user_agent(request)
        data = Data.objects.first()
        user = User.objects.get(user=request.user)
        rebutton = user.button
        user.button = myradio
        user.save()
        big = list(data.big)
        small = list(data.small)
        big_maximum = list(data.big_maximum)
        small_maximum = list(data.small_maximum)
        if rebutton != "a":
            if rebutton[0] == "b":
                big[int(rebutton[1:])]-=1
                big_maximum[int(rebutton[1:])] = False
            else:
                small[int(rebutton[1:])]-=1
                small_maximum[int(rebutton[1:])] = False
        if (myradio == None):
            data = Data.objects.first()
            user = User.objects.get(user=request.user)
            user_choise = user.button
            b = list(data.big)
            s = list(data.small)
            if user_agent.is_mobile:
                return render(request, "account/home_mobile.html", {
                    'radio_selection': user_choise,
                    'bm0': bm[0],
                    'bm1': bm[1],
                    'bm2': bm[2],
                    'bm3': bm[3],
                    'bm4': bm[4],
                    'bm5': bm[5],
                    'bm6': bm[6],
                    'bm7': bm[7],
                    'bm8': bm[8],
                    'bm9': bm[9],
                    'bm10': bm[10],
                    'bm11': bm[11],
                    'sm0': sm[0],
                    'sm1': sm[1],
                    'sm2': sm[2],
                    'sm3': sm[3],
                    'sm4': sm[4],
                    'sm5': sm[5],
                    'sm6': sm[6],
                    'sm7': sm[7],
                    'sm8': sm[8],
                    'sm9': sm[9],
                    'sm10': sm[10],
                    'sm11': sm[11],
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
            else:
                return render(request, 'account/home.html', {
                    'radio_selection': user_choise,
                    'bm0': bm[0],
                    'bm1': bm[1],
                    'bm2': bm[2],
                    'bm3': bm[3],
                    'bm4': bm[4],
                    'bm5': bm[5],
                    'bm6': bm[6],
                    'bm7': bm[7],
                    'bm8': bm[8],
                    'bm9': bm[9],
                    'bm10': bm[10],
                    'bm11': bm[11],
                    'sm0': sm[0],
                    'sm1': sm[1],
                    'sm2': sm[2],
                    'sm3': sm[3],
                    'sm4': sm[4],
                    'sm5': sm[5],
                    'sm6': sm[6],
                    'sm7': sm[7],
                    'sm8': sm[8],
                    'sm9': sm[9],
                    'sm10': sm[10],
                    'sm11': sm[11],
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
            if big[int(myradio[1:])] <= 9:
                big[int(myradio[1:])]+=1
                if big[int(myradio[1:])] == 10:
                    big_maximum[int(myradio[1:])] = True
        elif (myradio[0] == 's'):
            if small[int(myradio[1:])] <= 3:
                small[int(myradio[1:])]+=1
                if small[int(myradio[1:])] == 4:
                    small_maximum[int(myradio[1:])] = True
        data = Data.objects.first()
        data.big = list(big)
        data.small = list(small)
        data.big_maximum = list(big_maximum)
        data.small_maximum = list(small_maximum)
        data.save()
        b = list(data.big)
        s = list(data.small)
        bm = list(data.big_maximum)
        sm = list(data.small_maximum)
        user_choise = user.button
    if user_agent.is_mobile:
        return render(request, "account/home_mobile.html", {
            'radio_selection': user_choise,
                    'bm0': bm[0],
                    'bm1': bm[1],
                    'bm2': bm[2],
                    'bm3': bm[3],
                    'bm4': bm[4],
                    'bm5': bm[5],
                    'bm6': bm[6],
                    'bm7': bm[7],
                    'bm8': bm[8],
                    'bm9': bm[9],
                    'bm10': bm[10],
                    'bm11': bm[11],
                    'sm0': sm[0],
                    'sm1': sm[1],
                    'sm2': sm[2],
                    'sm3': sm[3],
                    'sm4': sm[4],
                    'sm5': sm[5],
                    'sm6': sm[6],
                    'sm7': sm[7],
                    'sm8': sm[8],
                    'sm9': sm[9],
                    'sm10': sm[10],
                    'sm11': sm[11],
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
    else:
        return render(request, 'account/home.html', {
            'radio_selection': user_choise,
            'bm0': bm[0],
            'bm1': bm[1],
            'bm2': bm[2],
            'bm3': bm[3],
            'bm4': bm[4],
            'bm5': bm[5],
            'bm6': bm[6],
            'bm7': bm[7],
            'bm8': bm[8],
            'bm9': bm[9],
            'bm10': bm[10],
            'bm11': bm[11],
            'sm0': sm[0],
            'sm1': sm[1],
            'sm2': sm[2],
            'sm3': sm[3],
            'sm4': sm[4],
            'sm5': sm[5],
            'sm6': sm[6],
            'sm7': sm[7],
            'sm8': sm[8],
            'sm9': sm[9],
            'sm10': sm[10],
            'sm11': sm[11],
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
