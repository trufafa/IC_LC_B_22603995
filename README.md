# Registo de Partidas
## Mafalda Pinto, a22603995
 Um programa dedicado a registar *mapas* e **pontuações** de partidas.

### Como correr:

Para correr o script no terminal, utilize o seguinte comando:

```$ ./partidas.py```

Necessitará de permissão para correr este script. Utilize o comando embaixo para a obter:

```$ chmod 777 partidas.py```

### Partidas iniciais:

| |Partida 1 |Partida 2 |Partida 3 |
|--|--|--|--|
| Mapa| Deserto | Floresta | Vulcão |
| Pontuação | 45 | 80 | 62 |
| Pontuação (em hexadecimal)| 0x2D | 0x50 | 0x3E |

```mermaid
flowchart TB
    Start((Opção 2 Selecionada - Início)) -->  NewMapCheck{Número de Mapas Atual é Maior que o Máximo Permitido?}
    NewMapCheck -- Sim --> PrintMaxMapError[Print 'Limite Atingido']
    NewMapCheck -- Não --> NewMapInput[/Pede Input de Novo Mapa/]
    NewMapInput -->  AppendMapList[Adiciona Novo Mapa à Lista de Mapas]
    AppendMapList --> PrintNewMap[Print Novo Mapa na Consola]
    PrintNewMap --> NewPointsInput[/Pede Input de Nova Pontuação/]
    NewPointsInput --> NewPointsCheck{Pontuação Dada Excede Limite de Pontos?}
    NewPointsCheck -- Não --> AppendPointsList[Adiciona Nova Pontuação à Lista de Pontuações]
    NewPointsCheck -- Sim --> PrintNewPointsError[Print Nova Pontuação na Consola]
    AppendPointsList --> PrintNewPointsSuccess[Print Nova Pontuação na Consola]
    PrintNewPointsError --> PrintInvalidPointsError[Print Avisando Que A Pontuação É Inválida]
    PrintInvalidPointsError --> NewPointsInput
    PrintNewPointsSuccess --> FinalPrintRegistered((Print Partida Registrada - Fim))

