from django.contrib import admin

# Register your models here.
from simplemooc.core.models import Course

#Classe para personalização do admin
class CourseAdmin(admin.ModelAdmin):

	list_display = ['name', 'slug', 'start_date', 'created_at']
	search_fields = ['name', 'slug']
	prepopulated_fields = {'slug' : ('name',)}


admin.site.register(Course, CourseAdmin)