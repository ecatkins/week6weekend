from django.db import models

class Instagram(models.Model):
	event = models.CharField(max_length=50,default="gay")
	created_time = models.DateTimeField()
	thumbnail_url = models.CharField(max_length = 300)
	standard_url = models.CharField(max_length = 300)
	likes = models.IntegerField()
	latitude = models.DecimalField(max_digits=8,decimal_places=6)
	longitude = models.DecimalField(max_digits=8,decimal_places=6)
	user = models.CharField(max_length=50)
	post_type  = models.CharField(max_length=20)
	caption = models.TextField()


