# -*- coding: utf-8 -*-
"""20cs3002_AI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AJeWDQ57MO9bsgGRX4vdKgVAMvTYYy5m
"""

import random as rd
import re
import math
import string

def pre_process_tweets(url):

    f = open(url, "r", encoding="utf8")
    tweets = list(f)
    list_of_tweets = []

    for i in range(len(tweets)):

        tweets[i] = tweets[i].strip('\n')
        tweets[i] = tweets[i][50:]
        tweets[i] = " ".join(filter(lambda x: x[0] != '@', tweets[i].split()))

        tweets[i] = re.sub(r"http\S+", "", tweets[i])
        tweets[i] = re.sub(r"www\S+", "", tweets[i])

        tweets[i] = tweets[i].strip()
        tweet_len = len(tweets[i])
        if tweet_len > 0:
            if tweets[i][len(tweets[i]) - 1] == ':':
                tweets[i] = tweets[i][:len(tweets[i]) - 1]

        tweets[i] = tweets[i].replace('#', '')
        tweets[i] = tweets[i].lower()
        tweets[i] = tweets[i].translate(str.maketrans('', '', string.punctuation))
        tweets[i] = " ".join(tweets[i].split())

        list_of_tweets.append(tweets[i].split(' '))

    f.close()

    return list_of_tweets

def k_means(tweets, k=4, max_iterations=50):

    centroids = []
    count = 0
    hash_map = dict()
    while count < k:
        random_tweet_idx = rd.randint(0, len(tweets) - 1)
        if random_tweet_idx not in hash_map:
            count += 1
            hash_map[random_tweet_idx] = True
            centroids.append(tweets[random_tweet_idx])

    iter_count = 0
    prev_centroids = []

    while (is_converged(prev_centroids, centroids)) == False and (iter_count < max_iterations):

        print("running iteration " + str(iter_count))
        clusters = assign_cluster(tweets, centroids)
        print(clusters)
        
        prev_centroids = centroids
        centroids = update_centroids(clusters)
        iter_count = iter_count + 1

    if (iter_count == max_iterations):
        print("max iterations reached, K means not converged")
    else:
        print("converged")

    sse = compute_SSE(clusters)

    return clusters, sse

def is_converged(prev_centroid, new_centroids):

    if len(prev_centroid) != len(new_centroids):
        return False

    for c in range(len(new_centroids)):
        if " ".join(new_centroids[c]) != " ".join(prev_centroid[c]):
            return False

    return True

def assign_cluster(tweets, centroids):

    clusters = dict()

    for t in range(len(tweets)):
        min_dis = math.inf
        cluster_idx = -1;
        for c in range(len(centroids)):
            dis = getDistance(centroids[c], tweets[t])

            if centroids[c] == tweets[t]:
                cluster_idx = c
                min_dis = 0
                break

            if dis < min_dis:
                cluster_idx = c
                min_dis = dis

        if min_dis == 1:
            cluster_idx = rd.randint(0, len(centroids) - 1)

        clusters.setdefault(cluster_idx, []).append([tweets[t]])
        last_tweet_idx = len(clusters.setdefault(cluster_idx, [])) - 1
        clusters.setdefault(cluster_idx, [])[last_tweet_idx].append(min_dis)

    return clusters

def update_centroids(clusters):

    centroids = []

    for c in range(len(clusters)):
        min_dis_sum = math.inf
        centroid_idx = -1

        min_dis_dp = []

        for t1 in range(len(clusters[c])):
            min_dis_dp.append([])
            dis_sum = 0
            for t2 in range(len(clusters[c])):
                if t1 != t2:
                    if t2 < t1:
                        dis = min_dis_dp[t2][t1]
                    else:
                        dis = getDistance(clusters[c][t1][0], clusters[c][t2][0])

                    min_dis_dp[t1].append(dis)
                    dis_sum += dis
                else:
                    min_dis_dp[t1].append(0)

            if dis_sum < min_dis_sum:
                min_dis_sum = dis_sum
                centroid_idx = t1


        centroids.append(clusters[c][centroid_idx][0])

    return centroids

def getDistance(tweet1, tweet2):

    intersection = set(tweet1).intersection(tweet2)
    union = set().union(tweet1, tweet2)
    return 1 - (len(intersection) / len(union))

def compute_SSE(clusters):

    sse = 0
    for c in range(len(clusters)):
        for t in range(len(clusters[c])):
            sse = sse + (clusters[c][t][1] * clusters[c][t][1])

    return sse

if __name__ == '__main__':

    data_url = '/content/drive/MyDrive/Health_Tweets/bbchealth.txt'

    tweets = pre_process_tweets(data_url)
    experiments = 5

    k = 3

    for e in range(experiments):

        print("------ Running K means for experiment no. " + str((e + 1)) + " for k = " + str(k))

        clusters, sse = k_means(tweets, k)

        for c in range(len(clusters)):
            print(str(c+1) + ": ", str(len(clusters[c])) + " tweets")

        print("--> SSE : " + str(sse))
        print('\n')
        k = k + 1

