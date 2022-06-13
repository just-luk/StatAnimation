from manim import *
from scipy.io import wavfile


class StatRap(MovingCameraScene):
    def construct(self):
        self.camera.background_color = WHITE
        rate, data = wavfile.read('Stat_rap.wav')
        data = data[0:44100]
        y_vals = data[:, 0]
        length = data.shape[0] / rate
        print(length)
        x_vals = np.linspace(0, length, data.shape[0])
        image = ImageMobject("ksong.jpg")
        image.scale(2)
        image.move_to(ORIGIN)

        plane = NumberPlane(
            x_range=(0, x_vals.max()),
            y_range=(y_vals.min() - 1, y_vals.max() + 1),
            x_length=1000,
            y_length=15
        )
        plane.center()
        line_graph = plane.plot_line_graph(
            x_values=x_vals,
            y_values=y_vals,
            line_color=BLACK,
            stroke_width=4,
            add_vertex_dots=False
        )
        ln = Line(line_graph.get_left(), line_graph.get_right())
        point = Dot(line_graph.get_left())
        self.add(line_graph)

        def update_point(mob):
           mob.move_to(point.get_center())

        # start animation
        self.add_sound("Stat_rap.wav")
        self.play(self.camera.frame.animate.scale(0.5).move_to(point))
        self.camera.frame.add_updater(update_point)
        self.play(MoveAlongPath(point, ln, rate_func=linear))
        self.camera.frame.remove_updater(update_point)
        self.add_subcaption("Ayo what up, DJ mig-mig on the mic", duration=2.5)
        self.wait(5.5)
        self.play(FadeIn(image))
