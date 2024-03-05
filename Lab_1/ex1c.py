import numpy as np
import matplotlib.pyplot as plt

A = 1
t = np.arange(0, 1, 0.001)

f1 = 5
f2 = 105
f3 = 205

fs = 100

i = 1

for f in range(0, 301, 5):
    sinusoida = A * np.sin(2 * np.pi * f * 1)
    print("iteration: " + str(i) + " frequency: " +
           str(f) + " " + str(sinusoida))
    i = i + 1

sinusoida_f1 = A * np.sin(2 * np.pi * f1 * np.arange(0, 1, 1 / fs))
sinusoida_f2 = A * np.sin(2 * np.pi * f2 * np.arange(0, 1, 1 / fs))
sinusoida_f3 = A * np.sin(2 * np.pi * f3  * np.arange(0, 1, 1 / fs))


plt.figure()

plt.plot(np.arange(0, 1, 1 / fs), sinusoida_f1, 'bo', label='fs1 = 5 kHz')
plt.plot(np.arange(0, 1, 1 / fs), sinusoida_f2, 'go', label='fs2 = 105 Hz')
plt.plot(np.arange(0, 1, 1 / fs), sinusoida_f3, 'ro', label='fs3 = 205 Hz')

plt.xlabel('Czas (s)')
plt.ylabel('Amplituda (V)')
plt.title('Próbkowanie Sygnałów Analogowych')
plt.legend()
plt.grid(True)
plt.show()

