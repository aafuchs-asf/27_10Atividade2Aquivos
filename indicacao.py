
with open ("filmes_avaliacao.txt","r") as filmes:
    linhas = filmes.read()
    filme = linhas.split(';')
    lista = []
    filmes_top5 = []

    for nota in filme:

        inf = nota.split(',')

        if (inf[0] != ''):


            lista.append((inf[0], inf[1], float(inf[2])))
            print(lista)


    lista.sort(key = lambda x: (-x[2], x[1]))
    filmes5 = lista[:5]
    print(f'{filmes5} : top 5')



    with open ("filmes_indicacao.txt", "a") as arquivo:
        arquivo.write(f'{filmes5}')