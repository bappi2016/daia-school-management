from django.db import models
from django.shortcuts import reverse,get_object_or_404
# Create your models here.




class Teacher(models.Model):
    teachers_name = models.CharField(max_length=32,help_text="Enter a Teachers Name here")
    teachers_speciality = models.CharField(max_length=32,help_text="Enter a Teachers Speciality.e.g. Drawing Instructor")
    teachers_description = models.TextField(max_length=1200,help_text="Enter a Teachers Description")
    teachers_image = models.ImageField(blank=True, null=True)
    

    def __str__(self):
        return self.teachers_name

class Classes(models.Model): # imagine this is our Product Model and category is our Teacher Model  
    class_name = models.CharField(max_length=120,help_text="Enter the class Name here")
    class_duration = models.CharField(max_length=30,help_text="Enter class duration",default='1 Year')
    # A classes(product) belongs to a teacher(category), but a teacher can have many classes
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE,related_name='teachers',blank=True, null=True)
    available_seats = models.PositiveIntegerField(default=30)
    class_description = models.TextField(max_length=500,blank=True,null=True)
    course_description = models.TextField(max_length=2500,blank=True,null=True)
    course_type = models.CharField(max_length=20,help_text="Enter the course type here,e.g. Basic")
    class_iamge = models.ImageField(blank=True, null=True)
    class_iamge_detail = models.ImageField(blank=True, null=True)
    class_added_at = models.DateField(auto_now=False)
    student_ages = models.IntegerField()
    tution_fee = models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.class_name

    def get_absolute_url(self):
        return reverse("class_detail", kwargs={"pk": self.pk})



    
    
