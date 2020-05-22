![MOVIE HEADER]()
> A Movie Reccomender System Using ALS, KMeans Clustering, and Matrix Factorization

<p align="center">
  <img src="https://img.shields.io/badge/Maintained%3F-IN PROG-green?style=flat-square"></img>
</p>


## Table of Contents

- [Basic Overview](#basic-overview)
  - [Context](#context)
  - [Goal](#goal)
- [Data Overview](#data-overview)
  - [Visualizations](#visualizations)
- [Modeling](#modeling)
  - [ALS Model](#als-model)
- [Cold Starts](#cold-starts)
- [License](#license)



## Basic Overview


### Context


### Goal
Given a dataset of users, movies, and ratings our team was given the task to predict ratings for other users and movies. 
O
ur score was measured based on how well we predicted the ratings for the users' ratings compared to our test set. 

---

## Data Overview




### Visualizations




## Modeling


### ALS Model


## Cold Starts
Insert nan bar chart

After using our ALS model to predict ratings for users in which we had prior movie ratings for we ended with XXX nulls. After careful consideration on what the best approach was for filling in the nulls we landed on a combination of a user-user recomendation and item-item recomendation. 

To start, we filled in all nulls with the average rating of all movies in the training set, this value was 3.59. After running our model with the nan's=3.59 we expected our predictions for movie ratings to be more accurate and this was in fact confirmed. We knew that filling in the same predicted value for all movies is not neccessarily the most logical choice but here we were able to generate our base prediction. 

To further improve our model, we used a kNN model to group all of our users into 20 specific clusters. 






## License
[MIT ©](https://choosealicense.com/licenses/mit/)

