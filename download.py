import pytube
from sys import exit
from os import getcwd
from decorate import *
from pytube import YouTube



class Video():
	def __init__(self, path):
		self.link 	= inputf("[=] youtube link> 		: ", "blue")
		self.driver = YouTube(self.link)
		self.path	= path
		
	def __video_streams__(self):
		self.streams = {"144p": 17, "360p": 18,"720p": 22, "1080p": 137}
		video_stream = self.driver.streams
		available_streams = set()
		
		# Using the binary search algortihm
		# for searching the available streams
		for stream in video_stream:
			for available_stream in self.streams.keys():
				if available_stream in str(stream):
					available_streams.add(available_stream)
		
		return available_streams
		
	def download_video(self):
		streams 		= list (self.__video_streams__())
		prompt			= "type [" + "  ".join(streams) + "] : "
		video_quality	= inputf(prompt, "blue")
		itag			= self.streams[video_quality]
		
		# accessing the specific video stream.
		# and downloading it on the given path
		obj = self.driver.streams
		obj.get_by_itag(int (itag)).download(self.path)
		
	def download_audio(self):
		stream = self.driver.streams
		stream.get_by_itag(140).download(self.path)
		
	def _video_info(self):
		author		 = self.driver.author
		length		 = self.driver.length
		title		 = self.driver.title
		views	   	 = self.driver.views
		publish_date = self.driver.publish_date
		
		return (author, length, title, views, publish_date)
		
	def print_info(self):
		author, length, title, views, publish_date = self._video_info()
		start_line = end_line = " "*16 + "+" + "-"*(len(title)+10) + "+"
		printf(start_line, "green")
		printf(f'''
			author          => {author}
			video length    => {length}
			video name      => {title}
			views           => {views}
			publish date    => {publish_date}
		''', "cyan")
		printf(end_line, "green")
		
		
		
	def Download(self):
		self.type	= inputf("[=] type for [V]ideo  [A]udio 	: ", "blue")
		self.print_info()
		if self.type == "A" or self.type == "A".lower():
			self.download_audio()
		self.download_video()
		
if __name__ == "__main__":
	try:
		printf(f"[+] Default path of the video : {getcwd()}", "magenta")
		path 	= inputf("[=] path of the video> 		: ", "blue")
		if not path:
			path = getcwd()
		Video(path).Download()
		printf("[---Video Downloaded---]", "green")
	except KeyboardInterrupt:
		printf("\nexiting...", "yellow")
		exit()
	except pytube.exceptions.RegexMatchError:
		print_error("Maybe you have entered a wrong link "
						"we cannot found the entred link ")
		exit()
		
	except AttributeError:
		print_error("there is some issue in download video"
				"try with another video quality")
		exit()
	
	except ModuleNotFoundError:
		os.system("pip install pytube")
		exit()
	
	except Exception as e:
		print_error(e)
		exit()
