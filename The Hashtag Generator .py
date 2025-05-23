def generate_hashtag(s:str):
    if len(s) < 1:
        return False

    variavel = ''
    #
    maius = s.title()

    if len(maius) > 140:
        return False
    else:
        novo = maius.replace(" ", "")

        # print(novo)

        for i in range(len(novo)):

            if i == 0:
                variavel = "#" + novo
                return variavel




print(generate_hashtag("ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq"))
