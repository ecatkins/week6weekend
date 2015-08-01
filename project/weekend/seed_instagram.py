import json
import datetime
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
	print(len(posts))
	listed_posts =[]
	for post in posts:
		post_dict = {
		"created_time":post.created_time,
		"thumbnail_url":post.get_thumbnail_url(),
		"standard_url":post.get_standard_resolution_url(),
		"likes":post.likes,
		"location":post.location,
		"user":post.user,
		"type":post.type,
		"caption":post.caption,
		}
		listed_posts.append(post_dict)
	return listed_posts


# all_posts = instagram("hello",5,40.733661, -74.011023,1435276860,1435276860)
# print(all_posts)


def seed_model(num_time_periods):
	min_time = 1435276860
	max_time = 1435319940
	for x in range(1,num_time_periods):
		posts = instagram(20,100,40.733661, -74.011023,min_time,max_time)
		min_time += 3600/num_time_periods*24*x
		max_time += 3600/num_time_periods*24*x
		for post in posts:
			created_time = post['created_time']
			thumbnail_url = post['thumbnail_url']
			standard_url = post['standard_url']
			likes = len(post['likes'])
			latitude = post['location'].point.latitude
			longitude = post['location'].point.longitude
			user = post['user'].username
			post_type  = post['type']
			try:
				caption = post['caption'].text
			except:
				caption = ""
			new_entry = Instagram(created_time=created_time,thumbnail_url=thumbnail_url,standard_url=standard_url,likes=likes,latitude=latitude,longitude=longitude,user=user,post_type=post_type,caption=caption)
			try:
				new_entry.save()
			except:
				continue



			
			
			
			
			
			
			
			
		



# loop_instagram()

# June 26 2015
# Hudson River Park
# 12am-1159pm
# 40.733661, -74.011023

