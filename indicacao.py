def ordem(relacao):
    maior = relacao[0]
    print(maior)

    for i in range (len(relacao)):

        if maior < relacao[i]:

            maior = relacao[i]
            
            print(f'{maior} relacao')

    #     if maior < relacao[i]:

    #         mais = relacao[i]

    #         print(f'{mais} esse é o maior')

    #     print(f'{maior} maior')


with open ("filmes_avaliacao.txt","r") as filmes:
    linhas = filmes.read()
    filme = linhas.split(';')
    lista = []

    for nota in filme:

        inf = nota.split(',')

        if (inf[0] != ''):

            lista.append(f'{inf[1]}')
            print(lista)

            maior = lista[0]

            for i in range (0, len(lista), 1):

                print(f'{lista[i]} - lista for')
                print(f'{maior} maior')

                if maior < lista[i]:

                    maior = lista[i]
                    
                    print(f'{maior} maior fim')

        #     with open ("filmes_indicacao.txt", "a") as arquivo:
        #         arquivo.write(f'{inf[0]},{avaliacao};')