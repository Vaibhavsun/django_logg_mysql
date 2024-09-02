from django.db import models
class main_model(models.Model):# so here we can see this our django models where we are writing all the fields required for storage
    user=models.CharField(default="patients",max_length=50)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    profile_pit=models.ImageField(upload_to='profile_pic')
    username=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    Address=models.TextField(max_length=200)
class blog_post(models.Model):# So here is model for posting blogs and fields required
    title=models.CharField(max_length=50,null=True)
    image=models.ImageField(upload_to='profile_pic')
    category=models.CharField(max_length=50)
    summary=models.CharField(max_length=2000)
    content=models.TextField(max_length=5000)
    draft=models.BooleanField(default=False)
    username=models.CharField(default="patients",max_length=50)
    

    