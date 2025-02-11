from manim import *


class CreateText(Scene):
    def construct(self):
        t=Text("Mình tên là Đỗ Văn Đạt!")

        self.play(Write(t))