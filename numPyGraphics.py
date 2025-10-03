import numpy as np
import matplotlib.pyplot as plt

# funcao linear = F(x) = 22 + x

x = np.array([[1],[2],[3]])
y = np.array([[23],[24],[25]])

plt.title("Titulo do Gráfico")
plt.xlabel("Legenda do X")
plt.ylabel("Legenda do Y")
plt.plot(x, y, color="red", linestyle="--")
plt.legend()
plt.show()
