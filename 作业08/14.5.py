import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 读取音频文件
sample_rate, audio_data = wavfile.read('your_audio_file.wav')

# 进行快速傅立叶变换
fft_result = np.fft.fft(audio_data)

# 计算频率
frequencies = np.fft.fftfreq(len(fft_result), d=1/sample_rate)

# 绘制傅立叶变换的结果
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(fft_result))
plt.title('Fast Fourier Transform of the Audio Signal')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()