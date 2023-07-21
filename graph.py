import matplotlib.pyplot as plt
from datetime import date, datetime

# Dados para o gráfico
x = [5, 4, 5]
y = [100, 200, 300]

# Criando o gráfico
plt.plot(x, y)
plt.title('Some Title')
plt.xlabel('Year')
plt.ylabel('Some measurements')

# Pega a data e hora atuais
today = date.today()
currentTime = datetime.now().strftime("%H%M")

# Salva o arquivo com a data e hora atuais
file = f'{today.isoformat()}_{currentTime}.png'
plt.savefig(file)
print(f'File saved as {file}')