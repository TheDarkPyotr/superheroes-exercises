class Solution:
    def minWindow(self, input: str, target: str) -> str:
        
        start = 0
        right = 0
        limit = len(input)

        dic_target = Counter(target)                # Contatore lettere target
        dic_input = collections.defaultdict(int)    # Contatore lettere input (vuoto)
        lenght = len(dic_target)                    # Contatore caratteri target
        valido = True                               # Flag validità numero caratteri
        
        res = (float('inf'), 0, 0)                  # Risultato (lunghezza, indice inizio, indice fine)
        
        while right < limit:

            if input[right] in dic_target:
                dic_input[input[right]] += 1

            valido = True
            if len(dic_input) == lenght:            # Se raggiunto dimensione ideale
                for k in dic_input:                 # Per ogni car in dic_input
                    if dic_input[k] < dic_target[k]:# Se numero car in input < car in target
                        valido = False              # Sottostringa non più valida
            else:
                valido = False                      #Altrimenti non più valida

            while start <= right and valido is True: # Se numero caratteri è valido, controllo se in sequenza
                
                if right - start + 1 < res[0]:
                    res = (right - start + 1, start, right) # Aggiorno lunghezza minima
                
                if input[start] in dic_target:
                    dic_input[input[start]] -= 1      # Riduco sottostringa

                start += 1                            #Riduco finestra [start:right]
                for k in dic_input:                   
                    if dic_input[k] < dic_target[k]:  # Se numero caratteri non combacia
                        valido = False                # Invalido sequenza

            right += 1                                # Aumento finestra a DX
            
        return "" if res[0] == float("inf") else input[res[1]:res[2] + 1]