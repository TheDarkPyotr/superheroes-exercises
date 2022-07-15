class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        dic_p = Counter(p)
        start = 0
        dic_s = {}
        #controllare se la lettera e valida per p
        #vedere se la lettera e già presente nel dizionario di supporto
        #se e gia presente la sequenza non e piu valida mi devo spostare con entrambi gli indici al succ
        #se invece la sequenza e presente in p e la seq e valida allora sposto start nel while intenro mano a mano
        res = []
        for i in range(len(p)):
            dic_s[s[i]] = 1 + dic_s.get(s[i],0)
        if dic_s == dic_p:
                res.append(start)
        for r in range (len(p),len(s)):  #i indice destro
            dic_s[s[r]] = 1 + dic_s.get(s[r],0)#usiamo get per evitare inizializzazione del dic
            dic_s[s[start]]-=1

            if dic_s[s[start]] == 0:
                dic_s.pop(s[start])

            start+=1

            if dic_s == dic_p:
                res.append(start)
        return res