from django.db import models
from django.utils.text import slugify
# Create your models here.


#Desk Model
class Desk(models.Model):
    title       =   models.CharField(max_length=100,verbose_name="عنوان")
    slug        =   models.SlugField(editable=False)
    created_at  =   models.DateField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at  =   models.DateField(auto_now=True,verbose_name="تاریخ ویرایش")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated_at']
        verbose_name="میزکار"
        verbose_name_plural="میزهای کار"

    def save(self,*args , **kwargs):
        value = self.title
        self.slug   =   slugify(value,allow_unicode=True)
        super().save(*args,**kwargs)


#TodoList Model
class TodoList(models.Model):
    desk        =   models.ForeignKey(Desk,on_delete=models.CASCADE,verbose_name="میزکار")
    task        =   models.TextField(verbose_name="وظیفه")
    task_date   =   models.DateField(null=True,verbose_name="تاریخ انجام وظیفه")
    created_at  =   models.DateField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at  =   models.DateField(auto_now=True,verbose_name="تاریخ ویرایش")

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['task_date','updated_at']
        verbose_name="وظیفه"
        verbose_name_plural="وظایف"