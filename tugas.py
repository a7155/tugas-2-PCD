import numpy as np
import imageio
import matplotlib.pyplot as plt

def analyze_image(image_path):
 
# Membaca gambar
  img = imageio.imread(image_path)

# Ekstrak channel warna
  red_channel = img [:, :, 0]
  green_channel = img[:, :, 1]
  blue_channel = img[:, :, 2]

# Konversi ke grayscale (rata-rata dari RGB)
  gray_img = np.mean(img, axis=2).astype(np.uint8)

# Konversi ke biner (thresholding)
  threshold = 128  # Sesuaikan nilai threshold sesuai kebutuhan
  binary_img = (gray_img > threshold).astype(np.uint8) * 255

# Tampilkan hasil
  plt.figure(figsize=(12, 4))
  plt.subplot(1, 6, 1)
  plt.imshow(img)
  plt.title('Gambar Asli')

  plt.subplot(1, 6, 2)
  plt.imshow(red_channel, cmap='gray')
  plt.title('Channel Merah')

  plt.subplot(1, 6, 3)
  plt.imshow(green_channel, cmap='gray')
  plt.title('Channel Hijau')

  plt.subplot(1, 6, 4)
  plt.imshow(blue_channel, cmap='gray')
  plt.title('Channel Biru')

  plt.subplot(1, 6, 5)
  plt.imshow(gray_img, cmap='gray')
  plt.title('Grayscale')

  plt.subplot(1, 6, 6)
  plt.imshow(binary_img, cmap='gray')
  plt.title('Biner')

  plt.show()
# Contoh penggunaan
image_paths = ["daun_pepaya.jpg", "daun_singkong.jpeg", "daun_kenikir.jpeg"]

for image_path in image_paths:
  analyze_image(image_path)