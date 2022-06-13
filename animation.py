from manim import *
from scipy.io import wavfile


class StatRap(Scene):
    def construct(self):
        rate, data = wavfile.read('Stat_rap.wav')
        data = data[0:10]
        values = data[:, 0]
        
        image = ImageMobject("ksong.jpg")
        image.scale(2)
        image.move_to(ORIGIN)
        chart = BarChart(
            values,
            y_length=6,
            x_length=10
        )

        

        # start animation
        self.add_sound("Stat_rap.wav")
        self.add_subcaption("Ayo what up, DJ mig-mig on the mic", duration=2.5)
        self.wait(5.5)
        self.play(FadeIn(image))
