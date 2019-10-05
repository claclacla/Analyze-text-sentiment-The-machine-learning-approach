import os
import re 

def load_reviews(path):
    reviews = []

    with open(path) as fp:
        for line in fp:
            reviews.append(line)
    
    return reviews
