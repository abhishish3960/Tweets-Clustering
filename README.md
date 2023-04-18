# Tweets-Clustering
The project includes implementation of K-means algorithm (an unsupervised learning algorithm) without using any libraries. The Objective of this project is to cluster the similar tweets based on similarity of words within the sentences.
At the end of each experiment for different values of k, sum of squared error (SEE) is computed. 
The algorithm uses Jaccard distance to compute the numerical distances betweeen two tweets.
Dynamic programming is also utilizied within the code in order to improve the computational running time of the program


Dataset Description

Abstract: The data was collected in 2015 using Twitter API. This dataset contains health news from more than 15 major health news agencies such as BBC, CNN, and NYT.
Each file is related to one Twitter account of a news agency. For example, bbchealth.txt is related to BBC health news.
Each line contains (tweet id|date and time|tweet). The separator is '|'. 
This text data has been used to evaluate the performance of topic models on short text data. However, it can be used for other tasks such as clustering.


K-Means

This is the most common unsupervised algorithm used to assign each data point to a class when the training data doesn’t include any classes or labels. 
The algorithm generates its own classes which are called clusters. After deciding on the k value, the first step is to randomly choose k number of centers.
Then all data points gets assigned to the closest cluster. 
Afterwards, the new center of each cluster is computed by calculating the average location of every data point in the cluster. 
The last two steps are repeated until the centers stop changing locations.


<img width="2082" alt="image" src="https://user-images.githubusercontent.com/99869699/232660457-2ec22504-8b44-4bc9-a3bb-3b9d2d4de452.png">


Objective Function - SSE

Accuracy of the algorithm cannot be computed in unsupervised algorithms since there are no classes or labels in the datasets. However, we can evaluate the quality of the clusters with an objective function. This function is called the sum of squared estimate of errors (SSE). It's basically the sum of all data points’ squared distances to their corresponding cluster center.
In my implementation I  could’ve stopped it when the centers stopped moving completely, however this might make the algorithm run for too many iterations, taking too much time.Hence I have taken max. Iterations 50.

Jaccard index

<img width="706" alt="image" src="https://user-images.githubusercontent.com/99869699/232660893-c58ad3ae-de1e-4d63-89de-26683576b063.png">

The Jaccard coefficient measures similarity between finite sample sets, and is defined as the size of the intersection divided by the size of the union of the sample sets.
