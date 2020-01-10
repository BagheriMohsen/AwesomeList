from django.db import models

# Create your models here.
class Desk(models.Model):
    title       =   models.CharField(max_length=100)
    slug        =   models.SlugField()
    created_at  =   models.DateField(auto_now_add=True)
    updated_at  =   models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['updated_at']


class TodoList(models.Model):
    desk        =   models.ForeignKey(Desk,on_delete=models.CASCADE)
    task        =   models.TextField()
    task_date   =   models.DateField(null=True)
    created_at  =   models.DateField(auto_now_add=True)
    updated_at  =   models.DateField(auto_now=True)

    def __str__(self):
        return self.task

    class Meta:
        ordering = ['task_date','updated_at']