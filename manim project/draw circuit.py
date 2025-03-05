from manim import *

class ColoredCircuit(Scene):
    def construct(self):
        # Tạo template circuitikz
        template = TexTemplate()
        template.add_to_preamble(r"\usepackage[siunitx, RPvoltages, american]{circuitikz}")
        
        # Tạo mạch điện với các thành phần tách biệt
        circuit = Tex(
            r"""
            \begin{circuitikz}
                \draw (0,0) 
                to[isource, l=$I_0$, v=$V_0$] (0,3) -- (2,3)
                node[circ](nodeA){};
                \draw (nodeA)
                to[R=$R_1$, i>_=$I_1$] (2,0) -- (0,0);
                \draw (nodeA) -- (4,3)
                to[R=$R_2$, i>_=$I_2$] (4,0) -- (2,0);
            \end{circuitikz}
            """,
            tex_template=template,
            stroke_width=3,
            fill_opacity=0.5,
            tex_environment="circuitikz"
        ).scale(1.2)
        
        # Tô màu các thành phần
        current_color = RED
        resistor1_color = YELLOW
        resistor2_color = BLUE
        
        # Tìm và tô màu các thành phần
        def colorize(pattern, color):
            for item in circuit.get_parts_by_tex(pattern):
                item.set_color(color)
        
        colorize(r"I_0", current_color)
        colorize(r"R_1", resistor1_color)
        colorize(r"R_2", resistor2_color)
        colorize(r"I_1", current_color)
        colorize(r"I_2", current_color)
        
        # Animation
        self.play(DrawBorderThenFill(circuit), run_time=2)
        
        # Hiệu ứng cho nguồn dòng
        current_source = circuit.get_parts_by_tex(r"I_0")[0]
        self.play(
            current_source.animate.set_color(RED_B),
            Flash(current_source, color=RED, flash_radius=0.5),
            run_time=1.5
        )
        
        # Hiệu ứng cho điện trở R1
        r1 = circuit.get_parts_by_tex(r"R_1")[0]
        self.play(
            Indicate(r1, scale_factor=1.2, color=YELLOW_D),
            run_time=2
        )
        
        # Hiệu ứng cho dòng điện I2
        i2 = circuit.get_parts_by_tex(r"I_2")[0]
        self.play(
            Circumscribe(i2, color=BLUE, fade_out=True),
            run_time=2
        )
        
        # Hiệu ứng tổng thể
        self.play(
            circuit.animate.shift(UP*0.5).set_opacity(0.8),
            rate_func=there_and_back,
            run_time=3
        )
        self.wait(2)