import numpy as np
import matplotlib.pyplot as plt

#sinus jest funkcją ciągłą więc możemy spróbkować ją
#w całej jej dziedzinie

#generujemy 0.1 sek sin o amplitudzie 230 i f = 50Hz

A = 1
f = 50
t = np.arange(0, 1, 0.001)  #Czas próbkowania od 0 do 0.1 sekundy z krokiem 0.0001 s
                              #im mniejszy krok próbkowania tym wykres bedzie bardziej dokładny

sinusoida = A * np.sin(2 * np.pi * f * t)

# Częstotliwości próbkowania
# dana częstotliwość próbkowania oznacza, że sygnał jest mierzony i rejerstrowany, czyli próbkowany
# f razy na sekundę
fs1 = 10e3
fs2 = 51
fs3 = 50
fs4 = 49

#probkowanie = np.arange(0, 0.1, 1/500)

#próbkowanie, czyli wyznaczanie konkretnych punktów naszej sinusoidy
sinusoida_fs1 = A * np.sin(2 * np.pi * f * np.arange(0, 1, 1 / fs1))
sinusoida_fs2 = A * np.sin(2 * np.pi * f * np.arange(0, 1, 1/fs2))
sinusoida_fs3 = A * np.sin(2 * np.pi * f  * np.arange(0, 1, 1 / fs3))
sinusoida_fs4 = A * np.sin(2 * np.pi * f  * np.arange(0, 1, 1 / fs4))

plt.figure()
plt.plot(t, sinusoida, 'b-', linewidth=2, label='Sinusoida ciągła')

plt.plot(np.arange(0, 1, 1 / fs1), sinusoida_fs1, 'b-', label='fs1 = 10 kHz')
plt.plot(np.arange(0, 1, 1 / fs2), sinusoida_fs2, 'go', label='fs2 = 51 Hz')
plt.plot(np.arange(0, 1, 1 / fs3), sinusoida_fs3, 'ro', label='fs3 = 50 Hz')
plt.plot(np.arange(0, 1, 1 / fs4), sinusoida_fs4, 'ko', label='fs3 = 49 Hz')


plt.xlabel('Czas (s)')
plt.ylabel('Amplituda (V)')
plt.title('Próbkowanie Sygnałów Analogowych')
plt.legend()
plt.grid(True)
plt.show()


'''
ten przykład świetnie pokazuje, jak nawet delikatna zmiana częśtotliwości
może zupełnie zmienić wygląd próbkowanego wykresu
żeby mniej wiecej oszacować jaki bedzie wygląd wykresu to trzeba
sinusoide spróbkować minimum 3 razy na okres
'''