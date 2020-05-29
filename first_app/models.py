from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class user_signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    Name=models.CharField(max_length=264)
    Mobile=models.CharField(max_length=11)
    #Email=models.EmailField(max_length=264)
    #Password=models.CharField(max_length=264)
    Address=models.CharField(max_length=264)
    District=models.CharField(max_length=264)
    Zip=models.CharField(max_length=264)

    def __str__(self):
         return self.user.username



DIVISSION_CHOICE = (
    ('Dhaka','Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ('Khulna','Khulna'),
    ('Mymensingh','Mymensingh'),
    ('Sylhet','Sylhet'),
    ('Barishal',' Barisal'),
    ('Chattagram','Chattagram'),
    ('Rangpur','Rangpur')
)

DISTRICT_CHOICE = (
    ('Dhaka','Dhaka'),
    ('Rajshahi', 'Rajshahi'),
    ('Khulna','Khulna'),
    ('Mymensingh','Mymensingh'),
    ('Sylhet','Sylhet'),
    ('Barishal',' Barisal'),
    ('Chattagram','Chattagram'),
    ('Rangpur','Rangpur'),
    ('Jessore','Jessore'),
    ('Jamalpur','Jamalpur'),
    ('Tangail','Tangail'),
    ('Lakshmipur','Lakshmipur'),
    ('Shatkhira','Shatkhira'),
    ('Bagerhat','Bagerhat'),
    ('Kishorgonj','Kishorgonj'),
)

CATAGORY_CHOICE=(
    ('Family','Family'),
    ('Bachelor Mess','Bachelor Mess'),
    ('Female Mess','Famale Mess'),
    ('Office','Office'),
    ('Others','Others'),

)



class ads_post(models.Model):

    def number():
        obj = ads_post.objects.order_by('-post_id')
        no=None
        for ob in obj:
            no=ob.post_id
            break
        if no == None:
            return 1
        else:
            return no + 1

    post_id = models.IntegerField(unique=True,default=number)
    #user = models.OneToOneField(User,on_delete=models.CASCADE)
    #postid=models.Autofield()
    title=models.CharField(max_length=264)
    picture=models.ImageField(blank='True')
    picture2=models.ImageField(blank='True')
    picture3=models.ImageField(blank='True')
    category=models.CharField(max_length=264,choices=CATAGORY_CHOICE,default="Family")
    bed=models.CharField(max_length=264)
    bath=models.CharField(max_length=264)
    kitchen=models.CharField(max_length=264)
    area=models.CharField(max_length=264)
    district=models.CharField(max_length=264,choices=DISTRICT_CHOICE,default="Dhaka")
    divission=models.CharField(max_length=264,choices=DIVISSION_CHOICE,default="Dhaka")
    address=models.CharField(max_length=264)
    description=models.CharField(max_length=264)
    cost=models.IntegerField()
    mobile=models.CharField(max_length=264)

    def __str__(self):
         return self.title


class track(models.Model):
    tarcker=models.IntegerField(default=0)

    def __str__(self):
        return "hell"
