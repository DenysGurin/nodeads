from django.db import models

from django.core.exceptions import ValidationError


def check_image(picture):
    if picture:
        if (not picture.name.endswith('.jpg') and 
            not picture.name.endswith('.png')):

            raise ValidationError("File is not a jpg or png. Please upload only jpg or png files")


class Group(models.Model):
    group = models.ForeignKey("self", related_name='groups', null=True, blank=True)
    picture = models.ImageField(upload_to='groups')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)

    def clean(self):
        check_image(self.picture)
        
    def __str__(self):
        return "id-%s name-%s"%(self.id, self.name)


class Element(models.Model):
    group = models.ForeignKey(Group, related_name='elements')
    picture = models.ImageField(upload_to='elements')
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, blank=True)
    created = models.DateField(auto_now_add=True)
    checked = models.NullBooleanField(default=False)


    def clean(self):
        check_image(self.picture)

    def __str__(self):
        return "id-%s name-%s"%(self.id, self.name)