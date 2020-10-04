import requests

base_url = "https://www.breakingbadapi.com/api/"
file_name = "BBCharacters.tsv"

def getAllCharacter(base_url):
    try:
        resp = requests.get(base_url + "characters")
        resp_json = resp.json()

        string_to_save = "name\tnickname\tportrayed\tstatus\n"

        for x in resp_json:
            string_to_save += "{}\t{}\t{}\t{}\n".format(x["name"], x["nickname"], x["portrayed"], x["status"])
        return string_to_save
    except: return ""

def saveFile(string_to_save, file_name):
    try:
        file = open(file_name, "w")
        file.write(string_to_save)
        file.close()
        print("Arquivo salvo com sucesso :)")
        print("Nome do arquivo: {}".format(file_name))
    except:
        print("Não foi possivel escrever o arquivo, provavelmente ele está aberto em outro programa!")

characters = getAllCharacter(base_url)

saveFile(characters, file_name)