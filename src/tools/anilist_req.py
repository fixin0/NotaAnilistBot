import requests
import json
def get_info_anime(_animeName):
    url = f"https://graphql.anilist.co"
    query = """
    query ($name: String){
          Media (search: $name, type: ANIME) {
                id
                title {
                    english
                    romaji
                    
                }

                description
          }
    }


"""
    var = {"name": _animeName}

    response = requests.post(url, json= {"query": query, "variables": var })
    data = response.json()
    
    return data["data"]["Media"]["id"]

def get_info_user(_username):
     url = f"https://graphql.anilist.co"
     query = """
    query ($username: String) {
        User(name: $_username) {
            siteUrl
        }
    }
    """
     var = {"name": _username}
     response = requests.post(url, json= {"query": query, "variables": var })
     data = response.json()

     if response.status_code == 200:
        data = json.loads(response.text)
        return data['data']['User']['siteUrl']
     else:
         return f' Maybe this is what you are looking for: https://www.anilist.co/user/{_username}'


