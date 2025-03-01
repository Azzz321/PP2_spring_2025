def writesome(list_of_elements):
    with open("text.txt", '+a') as f:
        text = "\n"
        for i in list_of_elements:
            text+=str(i)+' '
        f.write(text)
        f.close()
    
 

writesome([14353535, 8, 67534, "qwerty","zxcvbnmm,kytrdf",34,34])