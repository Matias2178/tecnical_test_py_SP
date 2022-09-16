def repetition_word(text: str()):
    """
    Sumary:
        Display the number of repetitions of each word from the input text

    Args:
        text (str): input text
    
    Returns:
        repeated_word 
    """
    #clean special characters 
    especial_character = "|°¬!#$%&/()='?\\¿¡+*{}[]^`,;.:-_<>"
    
    for i in especial_character:
        text = text.replace(i,"")
        
    #make the text in lowercase
    text = text.lower()

    #make a list word
    word_list = text.split()

    word_dic = {}
    
    for i in word_list:
        if i in word_dic:
            word_dic[i] +=1
        else:
            word_dic[i] = 1
    for clave, valor in word_dic.items():
        print(clave,valor)
        