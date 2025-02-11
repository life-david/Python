from manim import *
import numpy as np

class FourierNote(Scene):
    def construct(self):
        # Tạo đường path của nốt nhạc (ví dụ đơn giản)
        note = self.create_note_path()
        self.play(Create(note))
        self.wait(0.5)
        self.remove(note)
        
        # Lấy mẫu các điểm từ path
        num_samples = 1000
        z = self.sample_points(note, num_samples)
        
        # Tính toán hệ số Fourier
        coefficients = self.calculate_fourier_coefficients(z)
        
        # Sắp xếp hệ số theo độ lớn
        sorted_coeffs = sorted(coefficients, key=lambda x: -np.abs(x[0]))
        
        # Tạo animation
        self.animate_epicycles(sorted_coeffs, num_samples, run_time=10)

    def create_note_path(self):
        # Tạo path nốt nhạc đơn giản bằng các đường cơ bản
        note = VMobject()
        note.set_points_as_corners([
            LEFT*2 + DOWN*2,
            LEFT*2 + UP*2,
            LEFT*2 + UP*2 + RIGHT*1,
            LEFT*1 + UP*2 + RIGHT*1,
            LEFT*1 + UP*1.5,
            LEFT*0.5 + UP*1,
            RIGHT*0.5 + UP*1,
            RIGHT*1 + UP*1.5,
            RIGHT*1 + UP*2,
            RIGHT*2 + UP*2,
            RIGHT*2 + DOWN*2,
            LEFT*2 + DOWN*2
        ])
        return note

    def sample_points(self, path, num_samples):
        return np.array([
            path.point_from_proportion(t) 
            for t in np.linspace(0, 1, num_samples)
        ])

    def calculate_fourier_coefficients(self, z):
        z_complex = z[:,0] + 1j*z[:,1]
        fft = np.fft.fft(z_complex)
        return list(zip(fft, np.fft.fftfreq(len(z_complex))))

    def animate_epicycles(self, coefficients, num_samples, run_time=5):
        time_tracker = ValueTracker(0)
        path = VMobject()
        path.set_stroke(RED, 2)
        
        # Khởi tạo các thành phần
        circles = VGroup()
        lines = VGroup()
        dot = Dot(color=RED)
        
        # Cập nhật vị trí theo thời gian
        def update_path(path):
            t = time_tracker.get_value()
            current_point = self.calculate_position(coefficients, t, num_samples)
            if len(path.points) == 0:
                path.start_new_path(current_point)
            else:
                path.add_line_to(current_point)
        
        # Thêm các thành phần vào scene
        self.add(circles, lines, dot, path)
        path.add_updater(update_path)
        
        # Animation
        self.play(
            time_tracker.animate.set_value(1),
            rate_func=linear,
            run_time=run_time
        )
        path.remove_updater(update_path)
        self.wait(2)

    def calculate_position(self, coefficients, t, num_samples):
        pos = complex(0,0)
        for coeff, freq in coefficients[:30]:  # Giới hạn số vòng tròn
            freq_scaled = freq * num_samples
            pos += coeff * np.exp(2j*np.pi*freq_scaled*t) / num_samples
        return np.array([pos.real, pos.imag, 0])