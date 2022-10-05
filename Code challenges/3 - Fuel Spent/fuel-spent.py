valores = input().split()

km_litro = 12 
tempo = int(valores[0])
velocidade_media = int(valores[1])

distancia = velocidade_media * tempo
litros = distancia / km_litro

print ('%.3f'%(litros))