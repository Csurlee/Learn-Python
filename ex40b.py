class Song(object):

    def __init__(self, lyrics):
    	self.lyrics = lyrics

    def sing_me_a_song(self):
    	for line in self.lyrics:
    		print(line)

easter_day = Song(["Lallallalla and laaaa",
				   "Eastern is the best",
				   "session of the world "])

separator = Song(["-#-#-#-#-#-#-#-#-#-#-#-#-#-"])

happy_bday = Song(["Happy birthday to you.",
				   "I dont't want to get sued",
				   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
						"With pockets full of shells"])

easter_day.sing_me_a_song()

separator.sing_me_a_song()

happy_bday.sing_me_a_song()

separator.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
