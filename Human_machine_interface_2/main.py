import random

import numpy as np
from matplotlib import pyplot as picture
from scipy.fft import rfft, rfftfreq, irfft

SAMPLE_RATE = 100 # частота дискретизации
DURATION = 10 # секунды
TARGET_FREQ = 2


def generate_white_noise(sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration)
    y = np.array([random.uniform(-1, 1) for _ in range(0, sample_rate * duration)])
    return x, y


def generate_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration)
    frequencies = x * freq
    y = np.cos((2 * np.pi) * frequencies)
    return x, y


def plot_picture(x, y, name):
    fig, ax = picture.subplots()
    ax.set_title(name)
    picture.plot(x, y)
    picture.show()


if __name__ == '__main__':
    x, y = generate_white_noise(SAMPLE_RATE, DURATION)
    x_func, y_func = generate_wave(TARGET_FREQ, SAMPLE_RATE, DURATION)
    plot_picture(x_func, y_func, 'График исходной функции')
    plot_picture(x, y, 'График шума')
    _, nice_tone = generate_wave(TARGET_FREQ, SAMPLE_RATE, DURATION)
    _, noise_tone = generate_white_noise(SAMPLE_RATE, DURATION)
    mixed_tone = nice_tone + noise_tone
    plot_picture(x, mixed_tone, 'График исходной функции с белым шумом')
    N = SAMPLE_RATE * DURATION
    yf = rfft(mixed_tone)
    xf = rfftfreq(N, 1 / SAMPLE_RATE)
    plot_picture(sorted(xf), np.abs(yf), 'Частотный спектр сигнала')
    points_per_freq = len(xf) / (SAMPLE_RATE / 2) # Максимальная частота составляет половину частоты дискретизации
    target_idx = int(points_per_freq * TARGET_FREQ)
    yf[0:target_idx] = 0
    yf[target_idx + 1:N] = 0
    plot_picture(xf, np.abs(yf), 'Частотный спектр сигнала после удаления ')
    new_y = irfft(yf)
    plot_picture(x, new_y, 'После обратного преобразования')
