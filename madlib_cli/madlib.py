def read_template(path):
    try:
        with open(path) as file :
            content = file.read()
            return content
    except :
        raise FileNotFoundError 

def parse_template(contents):
    string_content = str(contents)
    key_word = []
    check_in_brackets = False
    out_s_brachets = "" 
    temp_word_string = ""
    for character in string_content:
        if character == '{':
            out_s_brachets  += character
            check_in_brackets = True
        elif character == '}':
            out_s_brachets  += character
            check_in_brackets = False
            key_word.append(temp_word_string)
            temp_word_string = ""
        elif check_in_brackets:
            temp_word_string += character
        else:
            out_s_brachets += character
    
    
    return (out_s_brachets, tuple(key_word))

def merge(content,key_word):
    final_reusalt = content.format(*key_word)
    return   final_reusalt 


def the_game(path):
    print('''
    ========================================
    ===                                  ===
    ===      welcome to Mad Lib CLi      ===
    ===                                  ===
    ========================================

    Mad Libs is a word game\n where user need to input different words .\n At the end you will get a story from user input \n 
    *************** let's go***************** 
    ''')
    read = read_template(path)
    actual_stripped, actual_parts = parse_template(read)
    final_word=[]
    for  i in actual_parts:
        in_user = input(f"please enter : {i} ==> ")
      
        final_word.append(in_user)
    story =merge(actual_stripped,final_word)

    with open(f"{path}_Story ", "w")  as  file :
        file.write(story)
    print("="*50)
    print("Your beautiful story is  :-")
    print(story)
    print("Good Bye ")

the_game("assets/make_me_a_video_game_template.txt")