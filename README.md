video_file_directory_to_mp3_python_linux
=================================

convert video files or oudio files (e.x mp4, wav, flv) in a directory to mp3 files.
It will optimize to to the best quality.
It is a direct conversion mp4 -> mp3.
There are no middle conversions like mp4->wav->mp3.
It uses Variable bitrate for maximum quality

Install
libmp3lame.so.0
ffmpeg

How to Run?
python '/path/to/Main.py' '/path/to/YourVideoAndAudioDirectoryDirectory'

Output
creates a new directory that ends with _Converted_mp3_files in the same place
of the video files directory

Bugs
it was tested on mp4, wav, flv and not on other formats
