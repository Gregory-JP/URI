salario = float(input())

if salario >= 0 and salario <= 400:
    reajuste = (15*salario) / 100
    novosalario = salario + reajuste
    
    print('Novo salario: {:.2f}'.format(novosalario))
    print('Reajuste ganho: {:.2f}'.format(reajuste))    
    print('Em percentual: 15 %')    

if salario >= 400.01 and salario <= 800.00:
    reajuste = (12*salario) / 100
    novosalario = salario + reajuste

    print('Novo salario: {:.2f}'.format(novosalario))
    print('Reajuste ganho: {:.2f}'.format(reajuste))    
    print('Em percentual: 12 %')    
        
if salario >= 800.01 and salario <= 1200.00:
    reajuste = (10*salario) / 100
    novosalario = salario + reajuste
    
    print('Novo salario: {:.2f}'.format(novosalario))
    print('Reajuste ganho: {:.2f}'.format(reajuste))    
    print('Em percentual: 10 %')    

if salario >= 1200.01 and salario <= 2000.00:
    reajuste = (7*salario) / 100
    novosalario = salario + reajuste
    
    print('Novo salario: {:.2f}'.format(novosalario))
    print('Reajuste ganho: {:.2f}'.format(reajuste))    
    print('Em percentual: 7 %')    

if salario > 2000.00:
    reajuste = (4*salario) / 100
    novosalario = salario + reajuste
    
    print('Novo salario: {:.2f}'.format(novosalario))
    print('Reajuste ganho: {:.2f}'.format(reajuste))    
    print('Em percentual: 4 %')