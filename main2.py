from moviepy.editor import *
# from tkinter.filedialog import *

# video=askopenfilename()
clip=VideoFileClip("E:\\videos").subclip(10,20)
clip=clip.volumex(0.8)
txt_clip=TextClip("Doremon ",fontsize=70,color="white")
txt_clip=txt_clip.set_position("center").set_duration(10)
video=CompositeVideoClip([clip,txt_clip])
video.write_videofile(Doremon_edited.webm)






