MAX_PARTIDAS = 8
PONTOS_MAXIMOS = 100
mapas = ["Deserto", "Floresta", "Vulcão"]
pontos = [45, 80, 62]

has_selected_3 = False

while(has_selected_3 == False):
    print("===== REGISTO DE PARTIDAS =====")
    print("1 - Ver estatísticas")
    print("2 - Registar partida")
    print("3 - Sair")
    print("4 - Apagar partida")

    selected_opt = input("Selecione a opção desejada: ")
    if(selected_opt == str(3)):
        has_selected_3 = True
        print("Até à próxima partida!")
        break
    elif(selected_opt == str(1)):
        if(len(mapas) == 0):
            print("Ainda não há partidas.")
            break
        addition = 0
        median = 0
        index = 0
        worst_points = PONTOS_MAXIMOS
        worst_map = "PLACEHOLDER"
        classification = "PLACEHOLDER"
        for map in mapas:
            print("Partida " + str(index + 1) + ": " + map + " - " + str(pontos[index]))
            if(pontos[index] < worst_points):
                worst_points = pontos[index]
                worst_map = map
            addition += pontos[index]
            index += 1
        median = addition // len(mapas)
        if(median < 50):
            classification = "Novato"
        elif(median >= 50 and median < 75):
            classification = "Experiente"
        elif(median >= 75):
            classification = "Lendário"
        print("Média: " + str(median))
        print("Pior pontuação: " + worst_map + " (" + str(worst_points) + " pontos)")
        print("Classificação: " + classification)
        print("Últimas três pontuações: " + str(pontos[-3:]))
        print("Pontuações de trás para a frente: " + str(pontos[::-1]))
    elif(selected_opt == str(2)):
        if (len(mapas) > MAX_PARTIDAS):
            print("Limite atingido.")
        else:
            new_map = input("Insira o mapa que deseja registar: ")
            mapas.append(new_map)
            print("Mapa: " + new_map)
            new_points = int(input("Insira a pontuação obtida: "))
            while(new_points > PONTOS_MAXIMOS):
                print("Pontuação: " + str(new_points))
                print("Pontos inválidos. Tente novamente.")
                new_points = int(input("Insira a pontuação obtida: "))
            pontos.append(new_points)
            print("Pontuação: " + str(new_points))
            print("Partida registada.")
    elif(selected_opt == str(4)):
        if(len(mapas) == 0):
            print("Ainda não há partidas.")
            break
        index = 0
        for map in mapas:
                    print("Partida " + str(index + 1) + ": " + map + " - " + str(pontos[index]))
                    index += 1
        discarded_map = int(input("Selecione a partida que deseja apagar: "))
        while(discarded_map > index or discarded_map <= 0):
            discarded_map = int(input("Índice Inválido. Tente novamente: "))
        mapas.pop(discarded_map - 1)
        pontos.pop(discarded_map - 1)
        print("Partida apagada. Lista atualizada de partidas: ")
        index = 0
        for map in mapas:
                            print("Partida " + str(index + 1) + ": " + map + " - " + str(pontos[index]))
                            index += 1
