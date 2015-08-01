from django.db import models

class Instagram(models.Model):
	created_time = models.DateTimeField()
	thumbnail_url = models.CharField(max_length = 300)
	standard_url = models.CharField(max_length = 300)
	likes = models.IntegerField()
	latitude = models.IntegerField()
	longitude = models.IntegerField()
	user = models.CharField(max_length=50)
	post_type  = models.CharField(max_length=20)
	caption = models.TextField()


