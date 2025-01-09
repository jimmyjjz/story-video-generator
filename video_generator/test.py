#from moviepy import VideoFileClip, CompositeVideoClip, ImageClip
#from moviepy.video.io.bindings import PIL_to_npimage
import misc
import scene_manager
from animateable import Animateable
from moviepy import *
class e:
    def ball(self, d, e=False):
        return "ee"
p=e()
p.ball(1,2)

clip=VideoFileClip("orange_juice_video.mp4").subclipped(20,22)
'''
thing=ImageClip("tti.png",transparent=False,duration=5)
thing.mask=ImageClip("tti_mask.png",is_mask=True)
'''
'''
thing1=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=2),misc.four_formation[0][0],misc.four_formation[0][1])
thing2=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=2),misc.four_formation[1][0],misc.four_formation[1][1])
thing3=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=2),misc.four_formation[2][0],misc.four_formation[2][1])
thing4=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=2),misc.four_formation[3][0],misc.four_formation[3][1])
thing1.establish()
thing2.establish()
thing3.establish()
thing4.establish()
'''
thing1=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=1),scene_manager.three_formation[0][0],scene_manager.three_formation[0][1])
thing2=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=1),scene_manager.three_formation[1][0],scene_manager.three_formation[1][1])
thing3=Animateable(ImageClip("assets\\testimage.png",transparent=False,duration=1),scene_manager.three_formation[2][0],scene_manager.three_formation[2][1])
thing1.establish()
thing2.establish()
thing3.establish()
cvc1=CompositeVideoClip([misc.create_transparent_image(1),thing2.clip]).with_position("center")
cvc2=CompositeVideoClip([misc.create_transparent_image(1),thing1.clip]).with_position("center")
li=[]
li.append(cvc1)
li.append(cvc2)
#final_product = CompositeVideoClip([clip,thing1.clip,thing2.clip,thing3.clip,thing4.clip])
e=concatenate_videoclips(li)
print(e.w)
final_product = CompositeVideoClip([clip,e])
final_product.write_videofile(
    "output.mov",
    codec="dnxhd",
    ffmpeg_params=[
        "-b:v", "36M",  #36 Mbps
        "-pix_fmt", "yuv422p",
    ]
)