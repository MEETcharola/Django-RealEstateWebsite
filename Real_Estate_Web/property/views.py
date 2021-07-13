import smtplib
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# from django.core.checks import messages
from django.core.mail import send_mail, EmailMessage, get_connection
from django.core.mail.backends import smtp
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import UpdateView

from users.models import Profile
from .choices import state_choices
from .models import Property_Residential, Property_Commercial, Property_Plot, Property_PG, Property_Images
from .forms import RESPropertyCreationForm, COMPropertyCreationForm, PLOTPropertyCreationForm, PGPropertyCreationForm, \
    Images

import smtplib
from email.message import EmailMessage
from django.core.files import File as DjangoFile


# Create your views here.

residential = Property_Residential.objects.all()
commercial = Property_Commercial.objects.all()
plot = Property_Plot.objects.all()
pg = Property_PG.objects.all()
all_property_list = list(residential) + list(commercial) + list(plot) + list(pg)


def dashboard(request):
    listings = Property_Residential.objects.order_by('-date_posted')
    latest_properties = Property_Residential.objects.order_by('-date_posted')

    profiles = Profile.objects.all()
    agents = []
    for profile in profiles:
        if profile.registered_as == "Agent":
            user = User.objects.get(pk=profile.user.id)
            agents.append(user)

    context = {
        'properties': listings,
        'latest_properties': latest_properties,
        'agents': agents[:3]
    }
    return render(request, 'property/dashboard.html', context)


@login_required
def property_create(request, form_type=None):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    if request.method == 'POST':
        if form_type != None:
            if form_type == "Residential":
                pro_form = RESPropertyCreationForm(request.POST, request.FILES)
            elif form_type == "Commercial":
                pro_form = COMPropertyCreationForm(request.POST, request.FILES)
            elif form_type == "Plot":
                pro_form = PLOTPropertyCreationForm(request.POST, request.FILES)
            else:
                pro_form = PGPropertyCreationForm(request.POST, request.FILES)

            if pro_form.is_valid():
                pro_form = pro_form.save(commit=False)
                pro_form.realtor = request.user
                pro_form.save()
                messages.success(request, f'Your property has been posted.')
                return redirect('property-list')
        else:
            pass
    else:
        if form_type != None:
            if form_type == "Residential":
                pro_form = RESPropertyCreationForm(request.POST, request.FILES)
            elif form_type == "Commercial":
                pro_form = COMPropertyCreationForm(request.POST, request.FILES)
            elif form_type == "Plot":
                pro_form = PLOTPropertyCreationForm(request.POST, request.FILES)
            else:
                pro_form = PGPropertyCreationForm(request.POST, request.FILES)
        else:
            pro_form = RESPropertyCreationForm(request.POST, request.FILES)
    return render(request, 'property/property-create.html', {'pro_form': pro_form, 'form_type': form_type})


def property_create_partial(request):
    form_type = request.POST['property-type']
    print(f"hello in partial view {form_type}")
    return HttpResponseRedirect(reverse('property-create', args=[form_type]))


# AGENT SECTION

def agent_list(request):
    profiles = Profile.objects.all()
    agents = []
    for profile in profiles:
        if profile.registered_as == "Agent":
            user = User.objects.get(pk=profile.user.id)
            agents.append(user)

    paginator = Paginator(agents, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    print(agents)
    context = {
        'agents': paged_listings
    }

    return render(request, 'property/agent-list.html', context)


def agent_single(request, user_id):
    user = User.objects.get(pk=user_id)
    properties = []
    for property in all_property_list:
        if property.realtor.id == user_id:
            properties.append(property)

    context = {
        'agent': user,
        'properties': properties
    }

    return render(request, 'property/agent-single.html', context)


# AGENT SECTION END

# PROPERTY LISTING SECTION

def property_list(request, city_name = None):

    queryset_list = all_property_list
    # queryset_list = Property_Residential.objects.all()

    if 'type' in request.GET:
        if request.GET['type'] == 'Residential':
            queryset_list = Property_Residential.objects.all()
        elif request.GET['type'] == 'Commercial':
            queryset_list = Property_Commercial.objects.all()
        else:
            queryset_list = Property_Plot.objects.all()

    if 'for' in request.GET:
        if request.GET['for'] == 'Pg':
            queryset_list = Property_PG.objects.all()

    print(queryset_list)

    # Property_type
    if 'type' in request.GET:
        print("INSIDE TYPE")
        p_type = request.GET['type']
        if p_type:
            queryset_list = queryset_list.filter(property_type__icontains=p_type)
            print(queryset_list)

    # Property_for
    if 'for' in request.GET:
        print("INSIDE FOR")
        p_for = request.GET['for']
        if p_for:
            queryset_list = queryset_list.filter(property_for__icontains=p_for)
            print(queryset_list)

    # City
    if 'city' in request.GET:
        print("INSIDE CITY")
        city = request.GET['city']
        print(city)
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
            print(queryset_list)

    # State
    if 'state' in request.GET:
        print("INSIDE STATE")
        state = request.GET['state']
        print(state_choices[state])
        if state:
            queryset_list = queryset_list.filter(state__iexact=state_choices[state])
            print(queryset_list)

    # Bedrooms
    if 'bedrooms' in request.GET:
        print("INSIDE BEDROOMS")
        bedrooms = request.GET['bedrooms']
        print(bedrooms)
        if bedrooms:
            if request.GET['type'] != 'Commercial' and request.GET['type'] != 'Plot':
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
                print(queryset_list)

        # Bathrooms
    if 'bathrooms' in request.GET:
        print("INSIDE BATHROOMS")
        bathrooms = request.GET['bathrooms']
        print(bathrooms)
        if bathrooms:
            if request.GET['type'] == 'Commercial':
                queryset_list = queryset_list.filter(washrooms__lte=bathrooms)
                print(queryset_list)
            elif request.GET['type'] == 'Residential':
                queryset_list = queryset_list.filter(bathrooms__lte=bathrooms)
                print(queryset_list)

        # Balconies
    if 'balconies' in request.GET:
        print("INSIDE BALCONIES")
        balconies = request.GET['balconies']
        print(balconies)
        if balconies:
            if request.GET['type'] != 'Commercial' and request.GET['type'] != 'Plot':
                queryset_list = queryset_list.filter(balconies__lte=balconies)
                print(queryset_list)

    # Price
    if 'price' in request.GET:
        print("INSIDE PRICE")
        price = request.GET['price']
        print(price)
        if price:
            queryset_list = queryset_list.filter(price__lte=price)
            print(queryset_list)

    paginator = Paginator(queryset_list, 9)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)


    context = {
        'properties': paged_listings,
        'values': request.GET,
    }

    return render(request, 'property/property-list.html', context)


def property_single(request, property_id, property_type=None):
    if property_type == "Residential":
        residentials = Property_Residential.objects.all()
        for p in residentials:
            if p.pk == property_id:
                images = Property_Images.objects.filter(residential__property_type__contains='Residential',
                                                        object_id=p.pk)
                context = {
                    'property': p,
                    'type': Property_Residential,
                    'subimages': images
                }

    if property_type == "Commercial":
        commercials = Property_Commercial.objects.all()
        for p in commercials:
            if p.pk == property_id:
                images = Property_Images.objects.filter(commercial__property_type__contains='Commercial',
                                                        object_id=p.pk)
                context = {
                    'property': p,
                    'type': Property_Commercial,
                    'subimages': images
                }

    if property_type == "Plot":
        plots = Property_Plot.objects.all()
        for p in plots:
            if p.pk == property_id:
                images = Property_Images.objects.filter(plot__property_type__contains='Plot', object_id=p.pk)
                context = {
                    'property': p,
                    'type': Property_Plot,
                    'subimages': images
                }

    if property_type == "PG":
        pgs = Property_PG.objects.all()
        for p in pgs:
            if p.pk == property_id:
                images = Property_Images.objects.filter(pg__property_type__contains='PG', object_id=p.pk)
                context = {
                    'property': p,
                    'type': Property_PG,
                    'subimages': images
                }
    print(context['subimages'])

    if request.method == "POST":
        print(f"TO : {request.POST.get('email')}")
        print(f"FROM : {context['property'].realtor.email}")
        send_mail('Property contact',
                  request.POST.get('message', False),
                  # request.POST.get('email', False),  # FROM
                  request.user.email,
                  [request.user.email, context['property'].realtor.email ],  # TO
                  fail_silently=False)

        return render(request, 'property/property-single.html', context)

    return render(request, 'property/property-single.html', context)


# PROPERTY LISTING SECTION END

# PROPERTY UPDATE START

class residential_property_update(LoginRequiredMixin, UpdateView):
    model = Property_Residential
    fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode', 'description', 'price',
              'bedrooms',
              'balconies', 'bathrooms', 'floor_number', 'total_floor', 'furnishing', 'car_parking', 'carpet_area',
              'super_area',
              'status', 'photo_main']
    template_name = 'property/property-update.html'
    success_url = '/property/property-list/'

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.realtor:
            return True
        return False


class commercial_property_update(LoginRequiredMixin, UpdateView):
    model = Property_Commercial
    fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode', 'landzone',
              'ideal_for_business', 'description', 'price',
              'washrooms', 'personal_washrooms', 'floor_number', 'total_floor', 'furnishing', 'carpet_area',
              'super_area',
              'status', 'photo_main']
    template_name = 'property/property-update.html'
    success_url = '/property/property-list/'

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.realtor:
            return True
        return False


class plot_property_update(LoginRequiredMixin, UpdateView):
    model = Property_Plot
    fields = ['property_for', 'title', 'address', 'city', 'locality', 'state', 'zipcode',
              'floors_allowed_for_construction', 'number_of_openside', 'width_of_road_facing_the_plot',
              'boundry_wall_status', 'description', 'price',
              'plot_area', 'plot_length', 'status', 'photo_main']
    template_name = 'property/property-update.html'
    success_url = '/property/property-list/'

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.realtor:
            return True
        return False


class pg_property_update(LoginRequiredMixin, UpdateView):
    model = Property_PG
    fields = ['title', 'address', 'city', 'locality', 'state', 'zipcode', 'description', 'monthly_rent',
              'security_deposit',
              'bedrooms',
              'balconies', 'bathrooms', 'furnishing',
              'status', 'photo_main']
    template_name = 'property/property-update.html'
    success_url = '/property/property-list/'

    def form_valid(self, form):
        form.instance.realtor = self.request.user
        return super().form_valid(form)

    def test_func(self):
        property = self.get_object()
        if self.request.user == property.realtor:
            return True
        return False


# PROPERTY UPDATE END


# PROPERTY DELETE START

@login_required
def property_delete(request, property_id, property_type):
    if property_type == "Residential":
        pro = Property_Residential.objects.get(pk=property_id)
    elif property_type == "Commercial":
        pro = Property_Commercial.objects.get(pk=property_id)
    elif property_type == "Plot":
        pro = Property_Plot.objects.get(pk=property_id)
    else:
        pro = Property_PG.objects.get(pk=property_id)

    print(f"PROPERTY TO BE DELETED : {pro}")
    if pro:
        user_id = pro.realtor.id
        pro.delete()
        return agent_single(request, user_id)
    else:
        print("NOT FOUND NOT DELETED")


# PROPERTY DELETE END

# PROPERTY IMAGES UPLOAD START

@login_required
def property_image_upload(request, property_id, property_type):
    context = {
        "property_id": property_id,
        "property_type": property_type,
    }
    if request.method == "POST":
        images = request.FILES.getlist('images')
        print(images)
        if property_type == "Residential":
            property = Property_Residential.objects.get(pk=property_id)
            for image in images:
                Property_Images.objects.create(image=image, content_object=property)

        elif property_type == "Commercial":
            property = Property_Commercial.objects.get(pk=property_id)
            for image in images:
                Property_Images.objects.create(image=image, content_object=property)

        elif property_type == "Plot":
            property = Property_Plot.objects.get(pk=property_id)
            for image in images:
                Property_Images.objects.create(image=image, content_object=property)

        else:
            property = Property_PG.objects.get(pk=property_id)
            for image in images:
                Property_Images.objects.create(image=image, content_object=property)

        messages.success(request, f'Images has been added to your property.')
        return redirect('/property/property-single/' + str(context['property_id']) + '/' + context['property_type'])
    else:
        return render(request, 'property/property-image-upload.html', context)

# MAIL SUPPORT

# def ViewSendEmail(request):
#     send_mail('Property contact',
#         request.POST[''],
#         request.user.email, #FROM
#         ['meetcharola.inexture@gmail.com'], #TO
#         fail_silently=False)
#     return render(request, 'property/property-list.html')




# PROPERTY IMAGES UPLOAD END

def about(request):
    return render(request, 'property/about.html')


def contact(request):
    if request.method == "POST":
        print(f"TO : {request.POST.get('email')}")
        send_mail(request.POST.get('subject'),
              request.POST.get('message'),
              request.POST.get('email'),  # FROM
              [request.POST.get('email'), 'meetcharola.inexture@gmail.com'],  # TO
              fail_silently=False)

        return render(request, 'property/dashboard.html')

    return render(request, 'property/contact.html')
