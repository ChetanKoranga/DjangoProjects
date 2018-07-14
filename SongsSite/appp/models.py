from django.db import models
class album(models.Model):
	artist = models.CharField(max_length = 200)
	album_title = models.CharField(max_length = 500)
	Song_genre = models.CharField(max_length = 100)
	album_cover = models.ImageField(upload_to="profile_image", blank=True)

	def __repr__(self):
		return self.album_title + '-' + self.artist

class song(models.Model):
	album = models.ForeignKey(album, on_delete=models.CASCADE)
	file_type = models.CharField(max_length = 100)
	song_title = models.CharField(max_length = 250)
	favorite = models.BooleanField(default = False)
	def __repr__(self):
		return self.song_title
