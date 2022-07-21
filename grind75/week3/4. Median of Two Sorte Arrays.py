def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
       
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2 #Dimensione partizione destra e sinistra

        #In A voglio il minore tra i due
        if len(B) < len(A):
            A, B = B,A

        left, right = 0, len(A)-1

        while True: #Poiché è garantito trovare la mediana, quando la troviamo ritorna
            
            #Per array A:
            #Vogliamo calcolare il valore di mezzo dell'array A
            #che useremo per calcolare la partizione sinistra 
            i = (left+right) // 2

            #Per array B:
            #Vogliamo lo stesso per l'array B: la partizione sinistra di B
            # avrà dimensione = half - len(partizione_Sx_A)
            # dove half è la dimensione della partizione sinistra dell'array mergiato (merge(A,B))
            j = half - i - 2 #-2 perchè è l'indice che lo delimita, -1 darebbe la dimensione

            #Ricavo gli estremi delle partizioni sinistre e destre trovate per A e B

            Aleft = A[i] if i >= 0 else float("-infinity")           #Se i troppo a sx
            Aright = A[i+1] if (i+1) < len(A) else float("infinity") #Se i+1 troppo a DX
            Bleft = B[j] if j >= 0 else float("-infinity")           #Se j troppo a sx
            Bright = B[j+1] if (j+1) < len(B) else float("infinity") #Se j+1 troppo a DX

            if Aleft <= Bright and Bleft <= Aright: #Partizione corretta

                #Caso pari
                if total % 2:
                    return min(Aright,Bright)
                
                #Caso dispari
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright: #Gli estremi ci dicono che la partizione SX di A è troppo grande
                #Quindi la riduciamo
                right = i - 1
            else:
                left = i + 1
                