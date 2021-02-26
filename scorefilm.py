# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:22:50 2021

@author: horna
"""

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import searborn as sns 
sns.set_style('white')
#%matplotlib inline #on notebook


column_names = ['user_id','item_id', 'rating', 'timestamp']
df = pd.read_csv('ratings.csv', sep='\t', names= column_names)
df.head()
film_titre= pd.read_csv("Id_titre_film")
film_titre.head()
df = pd.merge(df,film_titre,on='item_id')
df.head()

groupmean = df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
groupcount = df.groupby('title')['rating'].count().sort_values(ascending=False).head()
ratings = pd.DataFrame(groupmean)
ratings.head()
plt.figure(figsize=(12,4))
ratings['rating'].hist(bins=70)
sns.jointplot(x='rating', y='num of ratings', data=ratings, alpha=0.5)

fitselection= df.pivot_table(intex='user_id', columns='title', values='rating')
fitselection.head()

ratings.sort_values('number of ratings', ascending=False).head(10)
ratings.head()
spiderman_user_ratings = fitselection['spider-man']
batman_user_rating = fitselection['batman']
spiderman_user_ratings().head()

like_to_spiderman = fitselection.corrwith(starwars_user_ratings) #correlation with the movie
like_to_batma, = fitselection.corrwith(liarliar_user_rating)

#clean none values / use df and not a series
Kspiderman = pd.DataFrame(like_to_spiderman, columns=['Correlation']
Kspiderman.dropna(inplace=True) 
Kspiderman.head()      

kspiderman.sort_values('correlation', ascending =False).head(10)

#nb of ratings is important
kspiderman = kspiderman.join(ratings['number of ratings'])
kspiderman.head()
#then filter rating superior of 100
kspiderman[kspiderman['number of ratings']>100].sort_values('Correlation', ascending=False).head()

                