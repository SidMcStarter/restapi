from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from .models import Country
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import CreateCountryForm
from django.contrib.auth.decorators import login_required
import requests
from django.contrib.auth.models import User
from .filters import CountryFilter
# Create your views here.
@login_required
def populate(request):
    if request.user.is_superuser:
        r = requests.get("https://restcountries.com/v3.1/all")
        data = r.json()
        user = User.objects.get(is_superuser=True)
        for country in data:
            try:
                new_country = Country(name=country["name"]["official"], capital= country["capital"][0],
                    currencies= list(country["currencies"].values()), languages = list(country["languages"].values()), region= country["region"],
                    subregion = country["subregion"], population = country["population"],
                    image = country["flags"]["png"],user=user)
            except KeyError:
                pass;
            new_country.save()
    return redirect("home")


# def home(request):
#     populate()
#     return render(request,"countries/base.html")

class CountriesViews(ListView):
    model = Country
    context_object_name = "countries"
    template_name = "countries/home.html"
    paginate_by = 20
    def get_queryset(self):
        superuser = User.objects.get(is_superuser=True)
        query_set = Country.objects.filter(user=superuser)
        user = self.request.user
        if user.is_authenticated and not user.is_superuser:
            # contains the countries created by the user
            user_set = Country.objects.filter(user=user)
            # combines the prexisting superuser set with the user set
            query_set = query_set|user_set
        filter = CountryFilter(self.request.GET, query_set)
        print(filter.qs)
        return filter.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query_set = self.get_queryset()
        filter = CountryFilter(self.request.GET, query_set)
        context["filter"] = filter
        return context


class CountryDetailView(DetailView):
    model = Country
    template_name = "countries/country_detail.html"
    context_object_name = "country"


class CreateCountryView(LoginRequiredMixin, CreateView):
    model = Country
    template_name = "countries/create_country.html"
    form_class = CreateCountryForm
    context_object_name = "country"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_success_url(self):
        return reverse("country",kwargs={"pk":self.object.id, "country":self.object.name.replace(" ","-").lower()})
# @login_required
# def createCountry(request):
#     form = CreateCountryForm()
#     if request.method == 'POST':
#         post = request.POST.copy()
#         user = request.user
#         post["user"] = user
#         request.POST = post
#         form = CreateCountryForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("home")) 

    # return render(request,'countries/create_country.html',{"form":form})

class UpdateCountryView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Country
    template_name = "countries/create_country.html"
    form_class = CreateCountryForm
    context_object_name = "country"
    def get_success_url(self):
        return reverse("country",kwargs={"pk":self.object.id, "country":self.object.name.replace(" ","-").lower()})
    def test_func(self):
        country = self.get_object()
        return self.request.user.is_superuser or country.user.is_superuser or self.request.user == country.user

# @login_required
# def updateCountry(request, country=None, id=None):
#     country = Country.objects.get(id=id)
#     # pre fill the form
#     form = CreateCountryForm(instance=country)
#     if request.method == "POST":
#         post = request.POST.copy()
#         user = request.user
#         post["user"] = user
#         request.POST = post
#         form = CreateCountryForm(request.POST,instance=country)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse("home"))
#     context = {"form":form}
#     return render(request,'countries/update_country.html',context)

class DeleteCountryView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Country
    template_name = "countries/delete_country.html"
    success_url = reverse_lazy('home')
    context_object_name = "country"
    def test_func(self):
        country = self.get_object()
        return self.request.user.is_superuser or country.user.is_superuser or self.request.user == country.user
    # def handle_no_permission(self):
    #     return redirect("login")



@login_required
def delete_all(request):
    if request.user.is_superuser:
        Country.objects.all().delete()
    return redirect(reverse("home"))



    
