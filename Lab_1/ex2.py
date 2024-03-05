import numpy as np
import matplotlib.pyplot as plt

'''
wykonać rekonstrukcje sygnału z punktu 1A za pomocą funkcji sampling


sygnał o fs = 10kHz nazywamy pseudo analogowym, ponieważ
jego częstotliwość próbkowania jest na tyle duża i przez to
dokładna, że sygnał wydaje się być ciągłym

bo ogólnie sygnał analogowy to sygnał, który przyjmuje wartości w sposób
ciągły w czasie/przestrzenie
'''

pi = np.pi
t2 = 4 * pi
f1 = 5
T1 = 1 / f1

x1 = np.arange(0, t2 + 1 / f1, 1 / f1)
y1 = np.sin(x1)

f2 = f1 * 10
T2 = 1 / f2

x2 = np.arange(0, t2 + 1 / f2, 1 / f2)
y2 = np.zeros(len(x2))

'''
w tym fragmencie kodu następuje  rekonstrukcja naszej sinusoidy
'''
for i in range(len(x2)): #iteracja przez kolejne argumenty, tj. punkty czasow
    y = 0
    for j in range(len(x1)):
        #rekonstrukcja poprzez funkcje sampling zaklada, że
        #znamy okresy sygnału orginalengo i próbkowanego
        #oraz punkty czasowe (argumenty), które pokrywają się z naszą
        #orginalną funkcją
        b = pi / T1 * ((i - 1) * T2 - (j - 1) * T1)
        sb = 1
        if b != 0:
            sb = np.sin(b) / b
        y = y + y1[j] * sb
    y2[i] = y

plt.plot(x1, y1, 'r-o', label='y1') #sygnał orginalny
plt.plot(x2, y2, 'g-x', label='y2') #sygnał zrekonstruowany
plt.legend()
plt.show()
