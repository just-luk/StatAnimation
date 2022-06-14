# from pydub import AudioSegment
# time = 36 * 1000 + 12 * 1000 + 4 * 1000 + 2 * 1000 + 0.5 * 1000 + 0.5 * 1000
# sound = AudioSegment.from_wav("Stat_rap.wav")
# sound1 = sound[:time]
# sound2 = sound[time:]
# sound1.export("Stat_rap_part1.wav", format="wav")
# sound2.export("Stat_rap_part2.wav", format="wav")
from moviepy.editor import *
video1 = VideoFileClip("audio_files/part1.mp4").subclip(0, 36)
video2 = VideoFileClip("audio_files/part2.mp4").subclip(0, 12)
video3 = VideoFileClip("audio_files/part3.mp4").subclip(0, 4)
video4 = VideoFileClip("audio_files/part4.mp4").subclip(0, 2)
video5 = VideoFileClip("audio_files/part5.mp4").subclip(0, 0.5)
video6 = VideoFileClip("audio_files/part6.mp4").subclip(0, 0.5)
video7 = VideoFileClip("audio_files/part7.mp4")
final = concatenate_videoclips([video1, video2, video3, video4, video5, video6, video7])
final.write_videofile("Stat_rap.mp4")