def email_valido (email): # Função de verificação de email 
	return '@' in email	and '.' in email
	
def eh_par(n):  #  Função para verificar se um número é par  
	return n % 2 == 0

def fatorial(n): # Função para calcular o fatorial 
    if n == 0:
    return 1
return n * fatorial(n - 1)	

def quadrado(n): # Função verificar quadrado   
	return n ** 2

def eh_positivo(n): # Função de é positivo
	return n > 0
	
def verificar_maioridade(idade):
	return 'maior de idade'
	if idade >= 18:
	
else:
        return 'menor de idade'

def classificar_temperatura(temp):
    if temp < 0:
		return 'frio'
	elif 0 <= temp <= 25:
		return 'moderado'	   
	else:
     return 'quente'	
	
def avaliar_nota(nota):   
	if nota >= 7:
		return 'aprovado'

    elif 5 <= nota < 7:  
		return 'recuperacao'

	else:	   
		return 'reprovado'


def pode_votar(idade):
	if idade >= 18:	   
		return 'voto obrigatório'

	elif 16 <= idade < 18:
		return 'voto facultativo'

	else:
	return 'não pode votar'
		
def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
		
    elif estrelas == 4:    
	return 'bom'

elif estrelas == 3:
        return 'regular'

    elif estrelas == 2:
        return 'ruim'

    elif estrelas == 1:      
		return 'péssimo'

	else:             
		return 'valor inválido'	

		def test_email_valido(): 
			
			assert email_valido("teste@email.com") == True 
			assert email_valido("email.com") == False 
			assert email_valido("teste@com") == False 
			
		def test_eh_par(): 
				
	assert eh_par(4) == True
	 assert eh_par(5) == False 
				 
		 def test_fatorial(): 
			assert fatorial(0) == 1 
			assert fatorial(5) == 120 
					
		def test_quadrado(): 
			assert quadrado(3) == 9 
			assert quadrado(-3) == 9 
						
		def test_eh_positivo(): 
							
		assert eh_positivo(5) == True 
		assert eh_positivo(-5) == False 
		assert eh_positivo(0) == False 
		
		def test_verificar_maioridade(): 
		assert verificar_maioridade(18) == 'maior de idade' 
		assert verificar_maioridade(17) == 'menor de idade' 
		
		def test_classificar_temperatura(): 
		
		assert classificar_temperatura(-10) == 'frio' 
		assert classificar_temperatura(10) == 'moderado' 
		assert classificar_temperatura(30) == 'quente' 
		
		def test_avaliar_nota(): 
		assert avaliar_nota(7) == 'aprovado' 
		assert avaliar_nota(6) == 'recuperacao' 
		assert avaliar_nota(4) == 'reprovado' 
		
		def test_pode_votar(): 
			
			assert pode_votar(18) == 'voto obrigatório' 
			assert pode_votar(17) == 'voto facultativo' 
			assert pode_votar(15) == 'não pode votar' 
			
			def test_avaliar_produto(): 
				
				assert avaliar_produto(5) == 'excelente' 
				assert avaliar_produto(4) == 'bom' 
				assert avaliar_produto(3) == 'regular' 
				assert avaliar_produto(2) == 'ruim' 
				assert avaliar_produto(1) == 'péssimo' 
				assert avaliar_produto(0) == 'valor inválido'
		
