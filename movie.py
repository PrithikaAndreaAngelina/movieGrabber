import requests

url="https://movie-database-imdb-alternative.p.rapidapi.com/"

parameters= {
    's': '',
    'page': '1',
    'r': 'json' 
}

movie = input('Enter movie name: ')

parameters['s'] = movie
print(parameters['s'])


headers = {
    'x-rapidapi-key': "ENTER_YOUR_API_KEY", #API key can be obtained by subscribing to the below host
    'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com"
}

result=requests.request('GET',url,headers=headers,params=parameters)

print(result.text)
