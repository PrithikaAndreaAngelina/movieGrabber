import requests
import json

url="https://movie-database-imdb-alternative.p.rapidapi.com/"

parameters= {
    's': '',
    'page': '1',
    'r': 'json' 
}

movie = input('Enter movie name: ')

parameters['s']=movie


headers = {
    'x-rapidapi-key': "Enter your API key: ", #API key can be obtained by subscribing to the below host
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
}

result=requests.request('GET',url,headers=headers,params=parameters)

response_dict=json.loads(result.text)
Title= response_dict["Search"][0]['Title']
Year=response_dict["Search"][0]['Year']
imdbID=response_dict["Search"][0]['imdbID']
Type=response_dict["Search"][0]['Type']
Poster=response_dict["Search"][0]['Poster']

print("Title of the movie:", Title )
print('Movie Year:', Year)
print("imdb ID:", imdbID)
print("Type:",Type)
print("Poster: ",Poster)
