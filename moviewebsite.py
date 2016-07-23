import webbrowser

class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.youtube_trailer_url = youtube_trailer

	def show_trailer(self):
		webbrowser.open(self.youtube_trailer_url)
