class Codec:

    def encode(self, strs):
        """ Encode a list of string to a single string"""
        #Versione semplice: si poteva codificare la lunghezza
        #   e.g: 00000004ciao0000003bau....etc
        #semplifica la decodifica aumentando spazio

        result_string = ""
        for s in strs:
            result_string += s+"#"
        result_string = result_string[:-1] #Elimina # finale
        return result_string

    
    def decode(self, s):
        """Decode a string to a list of strings"""
        ## N.b: si poteva usare s.split("#") (??)
        word = ""
        string_list = []
        for pos in range(len(s)):
            if s[pos] != "#":
                word += s[pos]
            else:
                string_list.append(word)
                word = ""

        string_list.append(word) #Poiché l'ultimo el non ha #, aggiungo separatamente
        return string_list



strs1 = ["miao", "bauuuuuuuuuuuuuuuu", "ciao", "au"]
strs2 = [""]
strs3 = []

codec = Codec()
print(codec.decode(codec.encode(strs1)))
print(codec.decode(codec.encode(strs2)))
print(codec.decode(codec.encode(strs3)))