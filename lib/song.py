class Song:
  # Class attributes
  count = 0
  genres = []
  artists = []
  genre_count = {}
  artist_count = {}
  
  def __init__(self, name, artist, genre):
    # Instance attributes
    self.name = name
    self.artist = artist
    self.genre = genre
    
    # Update music library when a song is created
    self.add_song_to_count()
    self.add_to_genres()
    self.add_to_artists()
    self.add_to_genre_count()
    self.add_to_artists_count()
  
  def add_song_to_count(self):
    # Increment the total of songs
    Song.count += 1
  
  def add_to_genres(self):
    # Add genre only if it is not already in list
    if self.genre not in Song.genres:
      Song.genres.append(self.genre)

  def add_to_artists(self):
    # Add the artist only if they are not already in the list
    if self.artist not in Song.artists:
      Song.artists.append(self.artist)
  
  def add_to_genre_count(self):
    # Count how many songs are in each genre
    if self.genre in Song.genre_count:
      Song.genre_count[self.genre] += 1
    else:
      Song.genre_count[self.genre] = 1
  
  def add_to_artists_count(self):
    # Count how many songs are by each artist
    if self.artist in Song.artist_count:
      Song.artist_count[self.artist] += 1
    else:
      Song.artist_count[self.artist] = 1

    
