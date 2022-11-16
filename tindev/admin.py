from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User as CustomUser, Candidate, Recruiter

class CandidateInline(admin.StackedInline):
    model = Candidate
    can_delete = False
    verbose_name_plural = "candidate"

class RecruiterInline(admin.StackedInline):
    model =  Recruiter
    can_delete = False
    verbose_name_plural = "recruiter"

class UserAdmin(BaseUserAdmin):
    inlines = (CandidateInline, RecruiterInline)

# Register your models here.
# admin.site.unregister(User)
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Candidate)
admin.site.register(Recruiter)
