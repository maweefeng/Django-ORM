from django.db import models

# Create your models here.

class Aritcle(models.Model):
    aritcle_id = models.AutoField(primary_key=True)
    title = models.TextField()
    brief_content = models.TextField(default='这位同学很懒哦')
    content = models.TextField()
    publish_date = models.DateTimeField(auto_now=True)


class A(models.Model):
    onetoone = models.OneToOneField(Aritcle,on_delete = models.CASCADE)

class B(models.Model):
    foreign = models.ForeignKey(A,on_delete = models.CASCADE)

class C(models.Model):
    manytomany = models.ManyToManyField(B)


class AddressInfo(models.Model):
    address = models.CharField(max_length = 200,null = True,blank = True,verbose_name = '地址')
    pid = models.ForeignKey('self',null = True,blank = True,verbose_name = '自关联',on_delete =models.CASCADE)


    def __str__(self):
        return self.address