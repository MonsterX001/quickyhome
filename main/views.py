from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile, Houseuploads, User
from .filters import ListingFilter
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    listings = Houseuploads.objects.all()
    listing_filter = ListingFilter(request.GET, queryset = listings)
    
    #set pagination
    p = Paginator(Houseuploads.objects.all(), 12)
    page = request.GET.get('page')
    venues = p.get_page(page)

    context ={
        'listing_filter': listing_filter,
        'venues' : venues
    }

    return render(request, 'index.html',  context)
    
def search(request):
    listings = Houseuploads.objects.all()
    listing_filter = ListingFilter(request.GET, queryset = listings)
    context ={
        'listing_filter': listing_filter,
        'listings': listings
    }

    if listing_filter != None:
        messages.info(request, 'Your search was not found. Try to search by location only\n Otherwise, We do not have Houses from that location yet')
        return render(request, 'searches.html', context) 
    else: 
        messages.info(request, 'Your search was not found. Try to search by location only\n Otherwise, We do not have Houses from that location yet')
        return render(request, 'searches.html', context)
        

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()

                #log user and redirect to uploading page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login) 
                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect ('account')
        else:
            messages.info(request, 'Passwords not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('account')
        else:
            messages.info(request, 'Credentials Are Invalid')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def account(request):
    
    user_profile = Profile.objects.get(user=request.user)
    #houses = Houseuploads.objects.get(user=request.user.id)
    context = {
            'user_profile': user_profile,
            #'houses': houses
        }
    if request.method == 'POST':
        if request.FILES.get('image') == None:
            profileimg = user_profile.profileimg
            agentname = request.POST['agencyname']
            bio =request.POST['agentdetails']

            user_profile.profileimg = profileimg
            user_profile.agentname = agentname
            user_profile.bio = bio 
                   
            user_profile.save()
            return redirect('account')
            
        elif request.FILES.get('image') != None:

            profileimg = request.FILES.get('image')
            agentname = request.POST['agencyname']
            bio =request.POST['agentdetails']

            user_profile.profileimg = profileimg
            user_profile.agentname = agentname
            user_profile.bio = bio 
                   
            user_profile.save()
        
        
        return redirect('account')
    else:
        user_profile.refresh_from_db()
        return render(request, 'account.html', context)

@login_required(login_url='signin')
def Houseupload(request):

    if request.method == 'POST':
        
        user = request.user.username
        house_name = request.POST['housename']
        main_img = request.FILES.get('mainimg')
        houseimg_one = request.FILES.get('houseimg1')
        houseimg_two = request.FILES.get('houseimg2')
        houseimg_three = request.FILES.get('houseimg3')
        houseimg_four = request.FILES.get('houseimg4')
        houseimg_five = request.FILES.get('houseimg5')
        details = request.POST['details']
        housetype = request.POST['housetype']
        location = request.POST['location']
        rentmonth = request.POST['rentmonth']
        phone_no = request.POST['phoneno']
        

        new_post =  Houseuploads.objects.create(user = user, house_name=house_name, main_img=main_img, houseimg_one=houseimg_one, houseimg_two=houseimg_two, houseimg_three=houseimg_three, houseimg_four=houseimg_four, houseimg_five=houseimg_five, details=details, housetype=housetype, location=location, rentmonth=rentmonth, phone_no=phone_no) 
        new_post.save() 
        return redirect('account')
    
    
    return render(request, 'houseuploads.html',)

def houses(request, id):
    images = Houseuploads.objects.filter(id=id)

    context ={
        'images':images, 
    }
    return render(request, 'house_details.html', context)

@login_required(login_url='/')
def logout(request):
    auth.logout(request)
    return redirect('/')

    