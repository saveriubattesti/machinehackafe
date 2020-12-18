from tinytag import TinyTag 
  
# Pass the filename into the 
# Tinytag.get() method and store 
# the result in audio variable 
video = TinyTag.get("RGB mp4.mp4") 
  
# Use the attributes 
# and display 
print("Title:" + str(video.dimensions)) 
print("Artist: " + str(video.artist)) 
print("Genre:" + str(video.genre)) 
print("Year Released: " + str(video.year)) 
print("Bitrate:" + str(video.bitrate) + " kBits/s") 
print("Composer: " + str(video.composer)) 
print("Filesize: " + str(video.filesize) + " bytes") 
print("AlbumArtist: " + str(video.albumartist)) 
print("Duration: " + str(video.duration) + " seconds") 
print("TrackTotal: " + str(video.track_total))