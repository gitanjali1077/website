from django.views import generic
#require a form to create a new object
from django.views.generic.edit import CreateView,UpdateView ,DeleteView
# for uploading form
from django.core.urlresolvers import reverse_lazy
# for login
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Album
from django.views.generic import View
from .forms import UserForm ,UserForm1,UserForm2

class IndexView(generic.ListView):
        template_name = 'notes/index.html'
        context_object_name = 'all_albums'

        def get_queryset(self):
                return Album.objects.all()



class DetailView(generic.DetailView):
        model =Album
        template_name = 'notes/detail.html'


#creating a form class for form view but for this we import createview


class AlbumCreate(CreateView):
        model = Album
        fields = ['artist','album_title','genre','album_logo']
        
    #here u need not specify template name

class AlbumUpdate(UpdateView):
        model = Album
        fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
        model = Album
        success_url = reverse_lazy('notes:index')
    # success where u would be redirected after deleting the album


class UserFormView(View):
        form_class = UserForm
        template_name = 'notes/registration_form.html'

        #display blank form
        def get(self,request):
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form})

        #process form data
        def post(self, request):
                form = self.form_class(request.POST)

                if form.is_valid():

                        user = form.save(commit=False)
                        #here we are not saving the object to the database
                        #only keeping it locally for further references
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        email = form.cleaned_data['email']
                        college = form.cleaned_data['college']
                       
                        #user.set_password(password)
                        user.save()

                        user = authenticate(username=username ,password=password)

                        if user is not None:

                                if user.is_active:
                                        login(request, user)
                                        return redirect('notes:index')

                return render(request, self.template_name, {'form':form})              
class UserFormView1(View):
        form_class = UserForm2
        template_name = 'notes/registration_form.html'

        #display blank form
        def get(self,request):
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form})

        #process form data
        def post(self, request):
                form = self.form_class(request.POST)

                if form.is_valid():

                        user = form.save(commit=False)
                        #here we are not saving the object to the database
                        #only keeping it locally for further references
                        username = form.cleaned_data['username']
                        password = form.cleaned_data['password']
                        email = form.cleaned_data['email']
                        #college = form.cleaned_data['college']
                       
                        user.set_password(password)
                        user.save()

                        user = authenticate(username=username ,password=password)

                        if user is not None:

                                if user.is_active:
                                        login(request, user)
                                        return redirect('notes:index')

                return render(request, self.template_name, {'form':form})              

class UserFormLoginView(View):
        form_class = UserForm1
        template_name = 'notes/login_form.html'

        def get(self,request):
                form = self.form_class(None)
                return render(request, self.template_name, {'form': form})

        def post(self, request):
                form = self.form_class(request.POST)

                if form.is_valid():
                         username = form.cleaned_data['username']
                         password = form.cleaned_data['password']
                        # q = self.form_class.objects.filter(username=username )
                         q=authenticate(username=username ,password=password)

                         if  q:
                           return redirect('notes:index')
                return render(request, self.template_name, {'form':form})              


                         
                       

















    
                
