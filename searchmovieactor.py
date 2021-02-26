# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:44:22 2021

@author: horna
"""
#we use Imbd API

import imdb
moviesDB = imdb.IMDb()
#print(dir(moviesDB))


def searchMovie():

#on va mettre un imput -----
    search = input("Taper le titre du film ou de la série que vous rechercher: ")
    str(search)
#Recherche film
    movies = moviesDB.search_movie(search)

    print('Searching for :' + search)

    for movie in movies:
        title = movie['title']
        year  = movie['year']
        print(f'{title}-{year}')
    
    print(movies[0].keys()) 
    




#FILM RENSEIGNEMENT

    id = movies[0].getID()
    movie = moviesDB.get_movie(id)

    title = movie['title']
    year = movie['year']
    rating = movie['rating']
    directors = movie['directors']
    casting = movie['cast']

    print('Info du film :')
    print(f'rating : {rating}')
    directStr = ' '.join(map(str,directors))
    print(f'directors: {directStr}')

    actors = ','.join(map(str, casting))
    


#---------------------------

#ACTEUR 

   
        
    id = casting[0].getID()
    person = moviesDB.get_person(id)
    bio = moviesDB.get_person_biography(id)

    name = person['name']

    birthDate= person['birth date']
    height = person['height']
    trivia = person['trivia']
    titreRef = bio['titlesRefs']

    print(f'name: {name}')
    print(f'birth date: {birthDate}')
    print(f'height: {height}')
    print(f'trivia: {trivia[0]}')

    titreRef = ','.join(map(str, titreRef))
    

#------------------------
#10 movies bien et nul
    top = moviesDB.get_top250_movies()
    bottom = moviesDB.get_bottom100_movies()

    print('top 5 movies:')
    for movie in top[0:9]:
        print(movie)
        print()
        print('Bottom 5 movies:')
    for movie in bottom[0:9]:
        print(movie)
    return search, print(f'actors: {actors}'),print(f'bio title refs:{titreRef}')



searchMovie()








