from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from first_app import forms
from first_app.forms import signupform,signin,userform,post_ads,tracker_form,aids
from first_app.models import user_signup,ads_post,track
from django.contrib import messages


from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# from first_app.mypython import myfunction



@login_required
def special(request):
    # messages.info(request, 'Your password has been changed successfully!')
    # HttpResponse("Logged in Successfully!!")
    return HttpResponseRedirect(reverse('index'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



# Ceate your views here.
def index(request):
    # my_dict = {'test':"Testing Done"}
    return render(request,'first_app/content.html',)

def content(request):
    return render(request,'first_app/content.html',)


def signupw(request):
    messages.success(request, "signup Successfully!")
    return render(request,'first_app/signup.html',)

def signin(request):
    return render(request,'first_app/index.html',)

def postad(request):
    return render(request,'first_app/ads.html',)

def tattadaa(request):
    return render(request,'first_app/tattadaa.html',)

# def show_ads(request):
#     # if request.method=="GET"
#     #     a=request.GET.get('val',none)
#     ads=ads_post.objects.order_by('title')
#     return render(request,'first_app/showads.html',{'ads':ads})
def show_ads(request):
    ads=ads_post.objects.order_by('-post_id')
    return render(request,'first_app/showads.html',{'ads':ads,})

def divissionadd(request):
    adds=ads_post.objects.order_by('-post_id')
    a=None
    i=0
    if request.method=="POST":
        a=request.POST.get('dist')
    for ad in adds:
        if ad.divission == a:
            i=i+1

    return render(request,'first_app/divissionadd.html',{'adds':adds,'a':a,'i':i})

def search(request):
    adds=ads_post.objects.order_by('-post_id')
    b=None
    c=None
    i=0
    if request.method=="POST":
        b=request.POST.get('district')
        c=request.POST.get('catagory')
    for ad in adds:
        if ad.district == b and ad.category == c:
            i=i+1

    return render(request,'first_app/search.html',{'adds':adds,'b':b,'c':c,'i':i})


def addetails(request):
    trackit=track.objects.all()[:1].get()
    add=trackit.tarcker
    tracked=ads_post.objects.filter(post_id=add)
    return render(request,'first_app/addetails.html',{'tracked':tracked,})


def hell(request):
    return render(request,'first_app/addetails.html',)

# def middetails(request):
#     return render(request,'first_app/addetails.html',)



def signupforms(request):

    registred=False

    if request.method =="POST":
        user_form=userform(data=request.POST)
        signup_form=signupform(data=request.POST)

        if user_form.is_valid() and signup_form.is_valid():

            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=signup_form.save(commit=False)
            profile.user=user
            profile.save()

            registred=True


        else:
            print(user_form.errors,signup_form.errors)
    else:
        user_form=userform()
        signup_form=signupform()

    return render(request,'first_app/signup.html',
                            {'user_form':user_form,
                             'signup_form':signup_form,
                             'registred':registred}
                                )




def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                # print("Login successful")
                messages.success(request, "Logged in Successfully!")
                return HttpResponseRedirect(reverse('index'))


            else:
                return HttpResponse("Acount not Active")
        else:
            print("Anauthorised Entry")
            return HttpResponse("Invalid login request")
    else:
        return render(request,'first_app/index.html')



def adposting(request):
    posted=False

    if request.method =="POST":
        #user_form=userform(data=request.POST)
        posting=post_ads(data=request.POST)

        if posting.is_valid():

            ads=posting.save(commit=False)
            #profile.user=user

            if 'picture' in request.FILES:
                ads.picture=request.FILES['picture']
                ads.picture2=request.FILES['picture2']
                ads.picture3=request.FILES['picture3']
            else:
                print("No Images Found!")


            ads.save()

            posted=True

        else:
            print(posting.errors)
    else:
        #user_form=userform()
        posting= post_ads()

    return render(request,'first_app/ads.html',
                            {'post_ads':post_ads,
                             'posted':posted}
                                )




def aiding(request):      #this one is for getting post id of any post and then redirect to addetailspage
    a=1
    if request.method=="POST":
        a=int(request.POST.get('id'))
        t=track.objects.all()[:1].get()
        t.tarcker=a
        t.save()
        return redirect('link:addetails')


    else:
        return render(request,'first_app/showads.html')
