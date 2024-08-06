import requests

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
