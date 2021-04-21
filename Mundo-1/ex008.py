distancia = float(input('\033[1;97mDigite uma distância em metros: '))
print(f'A medida de {distancia:.1f} metros corresponde a:')
km = distancia / 1000
hm = distancia / 100
dam = distancia / 10
dm = distancia * 10
cm = distancia * 100
mm = distancia * 1000
print(f'{km}KM')
print(f'{hm}HM')
print(f'{dam}DAM')
print(f'{dm:.0f}DM')
print(f'{cm:.0f}CM')
print(f'{mm:.0f}MM')
