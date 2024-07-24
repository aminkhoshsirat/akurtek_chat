from django.db import models


class SiteDetailModel(models.Model):
    title = models.CharField(max_length=1000)
    logo = models.ImageField(upload_to='site_detail/logo')
    description = models.CharField(max_length=1000)
    non_profile_image = models.ImageField('site_detail/image')