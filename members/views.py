from django.shortcuts import render,redirect
from django.template import Template
from django.http import HttpResponse
from .forms import main_form,Login,doctor_blogs
from django.views.decorators.cache import never_cache
from .models import main_model,blog_post
# Create your views here.
def main(request):# so this is our main view where buttons are available for patients and doctor 
    return render(request,template_name='index.htm')
@never_cache
def patient(request): # this is our view from which the patient and doctor both can register and i am using different links for both of them pointing to same form fields
    url=request.build_absolute_uri()
    name=url.split('/')[-2]
    print(name)
    if request.method=='POST':
        r=request.POST.copy()
        if name=='doctors':
            r['user']=name
        form=main_form(r,request.FILES)
        if dict(form.data)['password']!=dict(form.data)['confirm_password']:# it is a check condition to check if password and confirm password are equal or not
            form.add_error('confirm_password',"Please try to match the password string")
        print(dict(form.data)['username'])
        obj=main_model.objects.filter(username=dict(form.data)['username'][0],user=name)# it is just to check wether the username already exists or not 
        if len(list(obj.values()))!=0:
            form.add_error('username',"The username already exists")
        if form.is_valid():
            form.save()
            form_ins=form.instance
            obj=main_model.objects.get(username=form.cleaned_data['username'],user=name)
            request.session['username']=obj.username
            request.session['user']=obj.user
            if name=="doctors":
                return render(request,'dashboard.htm',{'obj':obj,'form_ins':form_ins,'doc':name})
            else:
                return render(request,'dashboard.htm',{'obj':obj,'form_ins':form_ins})

        else:
            return render(request,'index.htm',{'form':form,'error':form.errors,'url':url})
    else:
        form=main_form()

    return render(request,'index.htm',{'form':form,'url':url})
@never_cache
def login(request): # And then we have a login view by which the user can reach to their dashboard 
    url=request.build_absolute_uri()
    name=url.split('/')[-2]
    print(name)
    if request.method=="POST":
        form=Login(request.POST)
        if form.is_valid():
            obj=main_model.objects.filter(username=dict(form.data)['username'][0],user=name,password=dict(form.data)['password'][0])
            if obj:
                obj=main_model.objects.get(username=dict(form.data)['username'][0],user=name)
                request.session['username']=obj.username# here we are saving the user session info
                request.session['user']=obj.user
                if name=="doctors":
                    return render(request,'dashboard.htm',{'obj':obj,'doc':name})
                else:
                    return render(request,'dashboard.htm',{'obj':obj})            
            else:
                form.add_error(None,'check either username or password is wrong')
    else:
        form=Login()
    return render(request,'index.htm',{'login':form,'error':form.errors,'url':url[:-5]})
    # Now lets see the working. In host link where i have hosted there is read only system due to which we can not register for that 
    # so i will show that in locahost
    # this problem is coming and it will require to use some other database and local database can not be useful
    # but with this login can be done 
    # so ending here
@never_cache
def to_show_doctors_blog(request):
    url=request.build_absolute_uri()
    name=url.split('/')[-2]
    view_or_post=url.split('/')[-1]
    print(view_or_post)
    if view_or_post=="view_posts":# checking if user is viewing or posting 
        if name=='doctors':# if viewing by doctor 
            username=request.session.get('username')
            obj=blog_post.objects.filter(username=username)#retriveing all the blogs posted by doctor
            return render(request,'blog_post.htm',{'obj':obj,'doc':True})# render them
        else:
            mh=blog_post.objects.filter(category='Mental Health',draft=False)
            hd=blog_post.objects.filter(category='Heart Disease',draft=False)
            cd=blog_post.objects.filter(category='Covid19',draft=False)
            im=blog_post.objects.filter(category='immunization',draft=False)# filtering different ccategory all blogs when viewing by patients
            return render(request,'blog_post.htm',{'mh':mh,'hd':hd,'cd':cd,'im':im,'pat':True})#rendering



    else:
        if request.method=="POST":# if posting 
            username=request.session.get('username')# here we retrieve them
            user=request.session.get('user')
            r=request.POST.copy()
            r['username']=username
            form=doctor_blogs(r,request.FILES)
            if form.is_valid():
                form.save()# here saving the form using username
                obj=main_model.objects.get(username=username,user=user)
                return render(request,'dashboard.htm',{'obj':obj,'doc':True})# here we open the users saved session dashboard after posting the blog
            else:
                return render(request,'blog_post.htm',{'form':form,'errors':form.errors,'url':url})# if error comoes
        else:
            form=doctor_blogs()
        return render(request,'blog_post.htm',{'form':form})# until sumbit button is  not pressed 

# showing mysql database tables 
#there are basically 2 tables
# as i was deploying on vercel which is serverless so mysql can not be integrated so i done using dbsqlite
# now showing html file
# now let see the working on local server
# if draft is true blogs can not be posted
# hence done