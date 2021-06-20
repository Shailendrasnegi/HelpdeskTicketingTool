from django.shortcuts import render
from django.views.generic import FormView, ListView, CreateView, TemplateView
from .forms import Form_page
from .models import FirstData


# Create your views here.


class CustomerComplainList(ListView):
    model = FirstData
    template_name = 'Complain.List.html'
    context_object_name = 'customer_detail'


# Use of FormView
class CustomerComplainForm(FormView):
    form_class = Form_page
    template_name = 'Complain.Create.html'
    success_url = "/ThankYou/"

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['Customer_Name'])
        print(form.cleaned_data['Customer_Detail'])
        print(form.cleaned_data['Mail_ID'])
        print(form.cleaned_data['Service_ID'])
        print(form.cleaned_data['Service_Type'])
        print(form.cleaned_data['Problem_Description'])
        return super().form_valid(form)


# CreateView
class CustomerComplainCreate(CreateView):
    form_class = Form_page
    template_name = 'Complain.Create.html'
    success_url = "/status/"


class CustomerTemplaplate(TemplateView):
    template_name = 'MSG.html'
