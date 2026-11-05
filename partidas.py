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

    selected_opt = input("Selecione a opção desejada: ")
    if(selected_opt == str(3)):
        has_selected_3 = True
        print("Até à próxima partida!")
        break
    elif(selected_opt == str(1)):
        addition = 0
        median = 0
        index = 0
        worst_points = PONTOS_MAXIMOS
        worst_map = "PLACEHOLDER"
        classification = "PLACEHOLDER"
        for map in mapas:
            print("Partida " + str(index) + ": " + map + " - " + str(pontos[index]))
            if(pontos[index] < worst_points):
                worst_points = pontos[index]
                worst_map = map
            addition += pontos[index]
            index += 1
        median = addition // 2
        if(median < 50):
            classification = "Novato"
        elif(median >= 50 and median < 75):
            classification = "Experiente"
        elif(median >= 75):
            classification = "Lendário"
        print("Média: " + str(median))
        print("Pior pontuação: " + worst_map + " (" + str(worst_points) + " pontos)")
        print("Classificação: " + classification)
    elif(selected_opt == str(2)):
        if (len(mapas) < MAX_PARTIDAS):
            new_map = input("Insira o mapa que deseja registar: ")
            mapas.append(new_map)
            new_points = input("Insira a pontuação obtida: ")
            pontos.append(new_points)
        else:
            print("Limite atingido.")
