from geopy.geocoders import Nominatim
import math

paper = [["Avenida Ruy Rodrigues 394 Campinas", "HT Papéis Barão"],
         ["Avenida José Cristóvão Gonçalves 247 Campinas", "Comércio de Aparas de Papel São Jorge"],
         ["Avenida Santa Isabel 2300 Campinas", "Ecoponto / Ponto Verde"],
         ["Rodovia Lix da Cunha 911 Campinas", "GMV Recycle"],
         ["Rua Doutor João Quirino do Nascimento 218 Campinas", "Gardim Aparas de Papéis"],
         ["Rua Clark 55 Valinhos", "Comércio de Aparas de Papel São Francisco Ltda"],
         ["Rua Antônio Felamingo 959 Valinhos", "Papéis Suleste"],
         ["Avenida Rosa Belmiro Ramos 225 Valinhos", "Santa Clara Recicláveis"],
         ["Rua Paulo Roberto Soares 511 Hortolândia", "PEV Adelaide"],
         ["Rua dos Manacás 169 Hortolândia", "Reciclagem Cantareira"]]

plastic = [["Rodovia Lix da Cunha 911 Campinas", "GMV Recycle"],
           ["Rua Itaóca 562 Campinas", "CBJ Reciclagem de Plásticos"],
           ["Rua Manoel Gomes Ferreira 42 Campinas", "Ecoponto Vila União"],
           ["Rua Estácio de Sá 577 Campinas", "Cooperativa de Recicláveis Santa Genebra"],
           ["Avenida Engenheiro Antônio Francisco de Paula Souza 3371 Campinas", "Sucatas Coisa Nova"],
           ["Avenida Maria Emília Alves dos Santos de Angelis 759 Campinas", "GSK APARAS DE PLÁSTICOS E PAPELÃO"],
           ["Rua Francisco Ceará Barbosa 451 Campinas", "Latasa Reciclagem"],
           ["Avenida João Antunes dos Santos 723 Valinhos", "EURIPLAST"],
           ["Avenida Vice Prefeito Anesio Capovilla 1091 Valinhos", "RM Recicláveis"],
           ["Avenida Rosa Belmiro Ramos 225 Valinhos", "Santa Clara Recicláveis"],
           ["Avenida das Melissas 286 Hortolândia", "Camp-Plast Sucatas Milouchine"]]

glass = [["Rua Saldanha da Gama 77 Campinas", "Ponto Verde - Vila Costa e Silva"],
         ["Avenida Engenheiro Antônio Francisco de Paula Souza 3371 Campinas", "Sucatas Coisa Nova"],
         ["Avenida Júlio de Mesquita 199 Campinas", "Jopac"],
         ["Avenida Marechal Rondon 2296-2382 Campinas", "Ecoponto Jardim Eulina"],
         ["Avenida Santa Isabel 2300 Campinas", "Ecoponto / Ponto Verde"],
         ["Avenida Rosa Belmiro Ramos 225 Valinhos", "Santa Clara Recicláveis"],
         ["Rua Pedro Alves Pego 1090 Valinhos", "Centro de Reciclagem"],
         ["Rua Rancho Fundo 96-270 Vinhedo", "Centro de Reciclagem"],
         ["Rua das Violetas 113 Hortolândia", "Casa Moradia - Centro de Reciclagem"]]

metal = [["Rua Açu 28 Campinas", "MD - Reciclagem de Metais"],
         ["Rua Flávio Telles 170 Campinas", "Eurometal Reciclagem e Comércio de Materiais"],
         ["Avenida Presidente Juscelino 287 Campinas", "Sucatas e Metais BS"],
         ["Rua Guaiçara 354 Campinas", "Sucatas e Metais 2 Irmãos"],
         ["Rua Domingos Cazotti 380 Campinas", "Marconatto & Urtado"],
         ["Avenida Rosa Belmiro Ramos 225 Valinhos", "Santa Clara Recicláveis"],
         ["Avenida Joaquim Alves Corrêa Valinhos", "Josevan Sucatas"],
         ["Rua dos Manacás 169 Hortolândia", "Reciclagem Cantareira Papeis E Sucatas"],
         ["Rua Nara Leão 661 Hortolândia", "Ciclo Gestão de Resíduos"]]

organic = [["Avenida Ruy Rodrigues 394 Campinas", "HT Papéis Barão - Coleta e reciclagem de resíduos"],
           ["Rodovia Lix da Cunha 911 Campinas", "GMV Recycle"],
           ["Avenida Santa Isabel 2300 Campinas", "Ecoponto / Ponto Verde"],
           ["Rua Saldanha da Gama 77 Campinas", "Ponto Verde - Vila Costa e Silva"],
           ["Rua Dante Suriani 2-382 Campinas", "Ecoponto Jardim Pacaembu"],
           ["Avenida Marechal Rondon 2296-2382 Campinas", "Ecoponto Jardim Eulina"],
           ["Rua João Bissoto Filho 2245 Valinhos", "Ecoponto Municipal"],
           ["Rua Nara Leão 661 Hortolândia", "Ciclo Gestão de Resíduos"],
           ["Rua Paulo Roberto Soares 511 Hortolândia", "PEV Adelaide"]]


def calculateDistance(lat1, lon1, lat2, lon2):
    rad = math.pi / 180
    dLat = lat2 - lat1
    dLon = lon2 - lon1
    r = 6372.795477598
    a = (math.sin(rad * dLat / 2)) ** 2 + math.cos(rad * lat1) * math.cos(rad * lat2) * (math.sin(rad * dLon / 2)) ** 2
    distance = 2 * r * math.asin(math.sqrt(a))
    return distance


def getCoordinates(local):
    geoLocator = Nominatim(user_agent="APS", timeout=5)
    location = geoLocator.geocode(local)
    aux = [location.latitude, location.longitude]
    return aux


def checkLists(userLocal, typeSelected):
    distanceList = []
    shortestDistance = 0
    if typeSelected == 1:
        for item in paper:
            local = getCoordinates(item[0])
            # position 0 = latitude
            # position 1 = longitude
            distanceList.append(calculateDistance(local[0], local[1], userLocal[0], userLocal[1]))
        shortestDistance = min(distanceList)

    elif typeSelected == 2:
        for item in plastic:
            local = getCoordinates(item[0])
            distanceList.append(calculateDistance(local[0], local[1], userLocal[0], userLocal[1]))
        shortestDistance = min(distanceList)

    elif typeSelected == 3:
        for item in glass:
            local = getCoordinates(item[0])
            distanceList.append(calculateDistance(local[0], local[1], userLocal[0], userLocal[1]))
        shortestDistance = min(distanceList)

    elif typeSelected == 4:
        for item in metal:
            local = getCoordinates(item[0])
            distanceList.append(calculateDistance(local[0], local[1], userLocal[0], userLocal[1]))
        shortestDistance = min(distanceList)

    elif typeSelected == 5:
        for item in organic:
            local = getCoordinates(item[0])
            distanceList.append(calculateDistance(local[0], local[1], userLocal[0], userLocal[1]))
        shortestDistance = min(distanceList)

    return distanceList.index(shortestDistance)


#  Ele faz uma lista com cada distancia e vê a menor

userAddress = ""


def getUserAddress(userStreet, userNumber, userCity):
    return userStreet + " " + userNumber + " " + userCity


def search(address, typeOfLixo):
    userCoordinates = getCoordinates(address)
    bestLocal = []
    if typeOfLixo == 1:
        bestLocal = paper[checkLists(userCoordinates, typeOfLixo)]
    elif typeOfLixo == 2:
        bestLocal = plastic[checkLists(userCoordinates, typeOfLixo)]
    elif typeOfLixo == 3:
        bestLocal = glass[checkLists(userCoordinates, typeOfLixo)]
    elif typeOfLixo == 4:
        bestLocal = metal[checkLists(userCoordinates, typeOfLixo)]
    elif typeOfLixo == 5:
        bestLocal = organic[checkLists(userCoordinates, typeOfLixo)]

    link = "google.com/maps/dir/" + address.replace(" ", "+") + "/" + bestLocal[0].replace(" ", "+")
    bestLocal.append(link)
    return bestLocal
