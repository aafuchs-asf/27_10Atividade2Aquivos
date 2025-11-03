def continuar():
    try:
        while True:
            exitQuest = input('Deseja adicionar outro item a lista?(S/N) ').upper().capitalize()[0]

            if exitQuest == "S":

                return True
            
            elif exitQuest == "N":

                return False
            
            else:
                print('Valor informado invalido! Tente novamente.')

    except IndexError:
        print('Valor invalido!')


with open ("filmes.txt","a") as filme:
    x = True
    while x: 
        
        nome = input('Nome do filme: ')
        data = input('Ano do filme: ')

    
        filme.write(f'{nome},{data};')

        x = continuar()


