from django.shortcuts import render
from django.views import View
class ViewHomepage(View):
    template_name = 'index.html'
    def get(self, request):
        return render(request,self.template_name)
    
class ViewGallery(View):
    template_name = 'gallery.html'
    def get(self, request):
        return render(request, self.template_name)
    
class ViewOrder(View):
    template_name = 'order.html'
    def get(self, request):
        return render(request, self.template_name)
    
class ViewPolicy(View):
    template_name = 'policy.html'
    def get(self, request):
        return render(request, self.template_name)
    
class ViewTerm(View):
    template_name = 'term.html'
    def get(self, request):
        return render(request, self.template_name)