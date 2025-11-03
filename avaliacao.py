def nota():
    try:
        while True:
            avaliacao = int(input(f'Avalie o filme {inf[0]} de 0 a 10: '))

            if avaliacao >= 0 or avaliacao <= 10:

                return str(avaliacao)
            
            else:
                print('Valor informado invalido! Tente novamente.')

    except ValueError:
        print('Valor invalido!')


with open ("filmes.txt","r") as filmes:
    linhas = filmes.read()
    filme = linhas.split(';')


    for i in filme:
        
        inf = i.split(',')

        if (inf[0] != ''):

            avaliacao = str(nota())


            with open ("filmes_avaliacao.txt","a") as arquivo:
                arquivo.write(f'{inf[0]},{avaliacao};')

       


