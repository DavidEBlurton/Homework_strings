python_reviews = ["This product is really good. I'm impressed with its quality.",
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.", 
"This was a poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."]
keywords = ["good", "excellent", "bad", "poor", "average"]
for review in python_reviews:
    for word in keywords:
        if word in review:
            x = review.replace(word, word.upper())
            print(x)