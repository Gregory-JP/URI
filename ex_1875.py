def time(t):
	return {'R':0,
		'G':1,
		'B':2}.get(t, 0)

casos_teste = int(input())

for i in range(casos_teste):
	qtd_gols = int(input())
	times = [0, 0, 0]
	for i in range(qtd_gols):
		t_marcou, t_sofreu = [x for x in input().split()]
		t_marcou = time(t_marcou)
		t_sofreu = time(t_sofreu)
		if t_marcou == 2 and t_sofreu == 0:
			times[t_marcou] += 2
		elif t_marcou == 0 and t_sofreu == 2:
			times[t_marcou] += 1
		elif t_marcou < t_sofreu:
			times[t_marcou] += 2
		elif t_marcou > t_sofreu:
			times[t_marcou] += 1
		
	if times[0] == times[1] and times[1] == times[2]:
		print('trempate')
	elif times[0] > times[1] and times[0] > times[2]:
		print('red')
	elif times[1] > times[0] and times[1] > times[2]:
		print('green')
	elif times[2] > times[0] and times[2] > times[1]:
		print('blue')
	else:
		print('empate')
