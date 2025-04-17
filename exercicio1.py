TEMPERATURA_NORMAL = 15
temperatura = float(input('Qual a temperatura atual? ').replace(',','.'))

if temperatura <= TEMPERATURA_NORMAL:
    print('Sistema de refrigeração está dentro da faixa de temperatura segura.')
else:
    print('É necessário a manutenção do sistema de refrigeração')