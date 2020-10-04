import requests

base_url = "https://www.breakingbadapi.com/api/"

def getAllCharacter(base_url):
    resp = requests.get(base_url + "characters")
    resp_json = resp.json()

    string_to_save = ""

    for x in resp_json:
        string_to_save += "{}\t{}\t{}\t{}\n".format(x["name"], x["nickname"], x["portrayed"], x["status"])
    return string_to_save

def saveFile(string_to_save, file_name):
    file = open(file_name, "a")
    file.write(string_to_save)
    file.close()

characters = getAllCharacter(base_url)

saveFile(characters, "character.tsv")