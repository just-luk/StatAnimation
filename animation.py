from manim import *
from scipy.io import wavfile

audio_name = "Stat_rap_part2.wav"


class StatRap(Scene):
    def construct(self):
        rate, data = wavfile.read(audio_name)
        data = np.array([int((x + y) / 2) for x, y in data])
        FRAME_LEN = 4410
        values = data[0:FRAME_LEN]

        image = ImageMobject("ksong.jpg")
        image.scale(2)
        image.move_to(ORIGIN)

        interval = np.linspace(values.min(), values.max(), 20)
        hist, _ = np.histogram(values, bins=interval)
        chart = BarChart(
            hist,
            y_length=1,
            x_length=10,
            y_axis_config={"color": BLACK,
                           "decimal_number_config": {"fill_opacity": 0.0}},
            x_axis_config={"color": BLACK},
        )

        # start animation
        self.add_sound(audio_name)
        self.add(chart)
        self.add_subcaption("Ayo what up, DJ mig-mig on the mic", duration=2.5)
        for x in range(0, len(data), FRAME_LEN):
            self.wait(FRAME_LEN / rate)
            values = data[x:x+FRAME_LEN]
            interval = np.linspace(values.min(), values.max(), 20)
            hist, _ = np.histogram(values, bins=interval)
            hist = [1 if a == 0 else a for a in hist]
            chart.change_bar_values(hist)
