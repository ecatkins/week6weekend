import json
import datetime
import random
from weekend.models import Instagram

# https://github.com/Instagram/python-instagram


# CLIENT INFO
# CLIENT ID	ff5eee26a1654d73ac173672f97c8c52
# CLIENT SECRET	5773a33ea1bd483d90d0ad41e96e8fde
# WEBSITE URL	http://localhost
# REDIRECT URI	http://localhost
# SUPPORT EMAIL	ecatkins@gmail.com
#access_token=31620180.ff5eee2.d5c5869e313445ffa7851204f3a2a5a7

#http://jelled.com/instagram/access-token

from instagram.client import InstagramAPI




def instagram(q,count,lat,lon,min_timestamp,max_timestamp):
	access_token = "31620180.ff5eee2.d5c5869e313445ffa7851204f3a2a5a7"
	client_secret = "5773a33ea1bd483d90d0ad41e96e8fde"
	api = InstagramAPI(client_id='be79976fa36248de874ed129a060ae37')
	posts = api.media_search(q,count,lat,lon,min_timestamp,max_timestamp)
	listed_posts =[]
	for post in posts:
		post_dict = {
		"created_time":post.created_time,
		"thumbnail_url":post.get_thumbnail_url(),
		"standard_url":post.get_standard_resolution_url(),
		"location":post.location,
		"user":post.user,
		"type":post.type,
		"caption":post.caption,
		}
		listed_posts.append(post_dict)
	return listed_posts

# instagram(20,2,40.733661, -74.011023,1435276860,1435319940)



# all_posts = instagram("hello",5,40.733661, -74.011023,1435276860,1435276860)
# print(all_posts)

# max_y = 40.752454

# max_x = -73.970446

# min_y  = 40.705276

# min_x = -74.019694

def random_coordinate(min_latitude,max_latitude, min_longitude, max_longitude):
	latitude = random.uniform(min_latitude,max_latitude)
	longitude = random.uniform(min_longitude,max_longitude)
	return (latitude,longitude)

# random_coordinate(40.705276,40.752454,-74.019694,-73.970446)



def seed_model(event,min_time,min_latitude,max_latitude, min_longitude, max_longitude,num_time_periods,count):
	for x in range(1,num_time_periods):
		max_time = min_time + 3600*24/num_time_periods
		latitude, longitude = random_coordinate(min_latitude,max_latitude, min_longitude, max_longitude)
		posts = instagram(20,count,latitude,longitude,min_time,max_time)
		min_time += 3600/num_time_periods*24
		for post in posts:
			created_time = post['created_time']
			thumbnail_url = post['thumbnail_url']
			standard_url = post['standard_url']
			latitude = post['location'].point.latitude
			longitude = post['location'].point.longitude
			user = post['user'].username
			post_type  = post['type']
			try:
				caption = post['caption'].text
			except:
				caption = ""
			new_entry = Instagram(event=event,created_time=created_time,thumbnail_url=thumbnail_url,standard_url=standard_url,latitude=latitude,longitude=longitude,user=user,post_type=post_type,caption=caption)
			try:
				new_entry.save()
			except:
				continue


# seed_model("gay_pride",1435291200,40.705276,40.752454,-74.019694,-73.970446,288,50)


# seed_model("wwc",1436500800,40.705276,40.752454,-74.019694,-73.970446,250,50)

			
			
			
			
			
			
		



# loop_instagram()

# June 26 2015
# Hudson River Park
# 12am-1159pm
# 40.733661, -74.011023

