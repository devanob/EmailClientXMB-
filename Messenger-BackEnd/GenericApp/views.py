from django.shortcuts import render
from django.views.generic import View

#sample view
class messengerView(View):
    template_name = "insert-template-name"
    def get(self,request):
        return  render(request, self.template_name)