"""

Estraiamo dalla lista gli elementi non numerici!

"""

lista = [1, 2, 3, "quattro", "cinque", "sei", "sette", "otto", "nove", "dieci"]


def fcerca_testo(elenco):
    risposta = list(filter(lambda x: not isinstance(x, int), elenco))
    return(risposta)


print("Vediamo cosa dice la documentazione di questo file...", __doc__)
print(fcerca_testo(lista))
