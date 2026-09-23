from django.db import models
class Student(models.Model):

    name=models.CharField(
        max_length=100
    )

    roll_no=models.IntegerField()

    age=models.IntegerField()

    student_class=models.CharField(max_length=20)
    
    email=models.EmailField(
        blank=False
    )

    address=models.TextField(
        blank=False
    )

    def __str__(self):

        return self.name