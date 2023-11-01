from django.db import models
import uuid,os,datetime

#Create your models here.

def get_file_path(request, filename):
    orignial_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime,orignial_filename)
    return os.path.join('uploads/',filename)

class Category (models.Model):
    Category_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200 , null=True)
    image = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Products (models.Model):
    products_id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=200 , null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=20, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

class banner_images(models.Model):
    images = models.ImageField(upload_to=get_file_path, blank=True, null=True)
    status = models.BooleanField(default=False, help_text="0=default, 1=hidden")
    
    def __str__(self):
        return str(self.images)
    