from django.contrib import admin

# Register your models here.

from app.models import User, Requst 


#class RequstAdmin(admin.ModelAdmin):

    #fields = ['title','content','pub_date'] 


#admin.site.register(Requst,RequstAdmin)

admin.site.register(User)
admin.site.register(Requst)
