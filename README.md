# Simple-Django-Authentication
Hello all..Hope all of you doing good..
okay this is my first updation in git hub so if you feel any inconvinience in my readme.md page ..I apologize..ok lets start
I just created a simple authentication system in django which was written in python
Iam only concentrated in backend ...Iam not put any effort for front end...so if you are intrested you can add some styles and fonts etc...
ok lets dive in the concept of authentication...
django  provides a default authentication functions which lives in django.contrib.auth module on that place we can import
the functions like authenticate,login,logout....

step1:
    creating a django project and creating an app,add the app name in INSTALLED_APPS of settings.py  file.. 
    
step 2:
    create a new file forms.py in the root directory of your app...then import the required things and specially
    an UserCreationForm for sign up page...
    
step 3:
    update in views.py
    just import the required modules...then write a functions for the following four
    home,signup,login,logout
    
step 4:
     creating a templates folder in the under the app directory and creating a new folder under templates folder in the name of your app for 
     django convention...this is the place where we store all the html pages which is going to render..
     
step 5:
      update in app level/urls.py
      import the views ,then creating the routes for all the four functions...then run the server..
      
      
     
                                                       Thankyou...
      
      
