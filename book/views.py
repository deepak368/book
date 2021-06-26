from django.shortcuts import render,redirect
from .forms import UserRegisterForm,UserLoginForm,AddbookForm,OrderForm
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.contrib.auth import login,logout,authenticate
from .models import addbookmodel,order_model
from .decorators import admin_only
from django.utils.decorators import method_decorator
from .filters import bookFilter

class UserRegisterView(TemplateView):
    form_class=UserRegisterForm
    model=User
    template_name ="book/registration.html"
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            return redirect("error")

class UserLoginView(TemplateView):
    form_class=UserLoginForm
    def get(self, request, *args, **kwargs):
        form=self.form_class()
        context={}
        context["form"]=form
        return render(request,"book/login.html",context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect("searchbook")
            else:
                return redirect("login")
        return render(request,"book/registration.html")
def User_logout(request):
    logout(request)
    return redirect("login")
@method_decorator(admin_only,name='dispatch')
class Create_Bookview(TemplateView):
    form_class=AddbookForm
    model = addbookmodel
    template_name = "book/createbook.html"
    def get(self, request, *args, **kwargs):
        form =self.form_class()
        context={}
        context["form"]=form
        return render(request,self.template_name,context)
    def post(self,request, *args, **kwargs):
        form=self.form_class(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            print("saved")
            return redirect("create")

class List_Book(TemplateView):
    def get(self, request, *args, **kwargs):
        lists=addbookmodel.objects.all()
        context={}
        context["lists"] = lists
        return render(request,"book/listbook.html",context)

@method_decorator(admin_only,name='dispatch')
class bookEditView(TemplateView):
    model=addbookmodel
    form_class=AddbookForm
    context={}
    template_name ="book/createbook.html"
    def get(self, request, *args, **kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(instance=edit)
        self.context["form"]=form
        return render(request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        edit=self.model.objects.get(id=kwargs["pk"])
        form=self.form_class(request.POST,instance=edit)
        if form.is_valid():
            form.save()
            return redirect("admin")
        else:
            return render(request,self.template_name,self.context)
@method_decorator(admin_only,name='dispatch')
class bookDeleteView(TemplateView):
    model=addbookmodel
    def get(self, request, *args, **kwargs):
        dele=self.model.objects.get(id=kwargs["pk"])
        dele.delete()
        return redirect("admin")
@method_decorator(admin_only,name='dispatch')
class Adminpage(TemplateView):
    def get(self, request, *args, **kwargs):
        lists=addbookmodel.objects.all()
        context={}
        context["lists"] = lists
        return render(request,"book/adminAuctionpage.html",context)


def Search_view(request):
    book = addbookmodel.objects.all()
    context = {}
    bookfilter = bookFilter(request.GET,queryset=book)
    context["filter"] = bookfilter
    return render(request, "book/search.html", context)

def order_view(request,id):
    product = addbookmodel.objects.get(id=id)
    form = OrderForm(initial={"Product": product})
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cart")

    return render(request, "book/order.html", context)

def cart(request):
    orders=order_model.objects.all()
    context={}
    context["orders"]=orders
    return render(request,"book/cart.html",context)
