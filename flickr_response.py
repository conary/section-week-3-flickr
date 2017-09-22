
# with automaticaly closes the file outside of its indent (scope)
import json

class Photo(object):
	def __init__(self, photo_diction):
		self.owner = {
			'username': photo_diction['owner']['username'],
			'realname': photo_diction['owner']['realname'],
			'location': photo_diction['owner']['location']
		}
		self.title = photo_diction['title']['content']
		
		self.tags = []
		for tag in photo_diction['tags']['tag']:
			self.tags.append(tag['raw'])


#	self.tags = []
#	tag.list = photo_diction['tags']['tag']
#	for tag_diction in tag_list:
#		tag_raw = tag_diction['raw']
#		self.tags.append(tag_raw)


self.id = photo_diction['id']
self.date_taken = photo_diction['dates']['taken']
self.url = 
self.license



with open("sample_diction.json", "r") as f:
	f_string = f.read()
	response_diction = json.loads(f_string)
pd = response_diction['photo']
photo = Photo(pd)



