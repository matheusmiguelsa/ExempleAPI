from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ClientForm
from rest_framework import viewsets
from pages.models import Client
from pages.api.serializer import ClientSerializer
from rest_framework.permissions import IsAuthenticated



class ClientViewSet(viewsets.ModelViewSet):
    permission_class = (IsAuthenticated, )
    
    queryset = Client.objects.all()
    serializer_class= ClientSerializer





    
class HomePageView(TemplateView):
    template_name = 'home.html'

    
    def home(request):

        form = ClientForm()
        
        if request.method == 'POST':
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
          
                
        context = {'form':form}
        return render(request, 'home.html', context)





