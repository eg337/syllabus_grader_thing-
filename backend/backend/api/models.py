from django.db import models

# Create your models here.
class Grade_Calc(models.Model):
    input_file1 = models.FileField(default="models.py")
    input_data1 = models.CharField(max_length = 300, default = "")
    input_file2 = models.FileField(default="models.py")
    input_data2 = models.CharField(max_length = 300, default = "")
    output_filename = models.CharField(max_length = 300, default = "")
    created_at = models.DateTimeField(auto_now_add = True)