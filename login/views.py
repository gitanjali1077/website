from django.shortcuts import redirect
from .models import *
from .forms import *
from django.views.generic import CreateView

class addUser(CreateView):
    form_class = addUserMultiForm
    template_name = "addUser.html"
    success_url = 'www.facebook.com'

    def form_valid(self, form):
        user = form['user'].save()
        profile = form['profile'].save(commit=False)
        profile.userName = User.objects.get(username= user.username)
        profile.save()
        return redirect(self.success_url)
