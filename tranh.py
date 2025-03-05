import matplotlib.pyplot as plt

# Tọa độ các điểm của hình vuông
x = [0, 100, 100, 0, 0]
y = [0, 0, 100, 100, 0]

plt.plot(x, y, 'b-', linewidth=2)  # Vẽ đường viền hình vuông màu xanh
plt.fill(x, y, 'cyan', alpha=0.5)  # Tô màu xanh nhạt
plt.xlim(-10, 110)
plt.ylim(-10, 110)
plt.gca().set_aspect('equal')  # Giữ tỷ lệ 1:1
plt.grid()
plt.show()
