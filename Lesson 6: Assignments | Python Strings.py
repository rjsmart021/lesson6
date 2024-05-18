#Lesson 6: Assignments | Python Strings
Python_reviews = """This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.",
                  "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it."""
#Task_1
print(Python_reviews.count('good'))
print(Python_reviews.count('excellent'))
print(Python_reviews.count('bad'))
print(Python_reviews.count('poor'))
print(Python_reviews.count('average'))

PR1 = "This product is really good. I'm impressed with its quality."
PR2 = "The performance of this product is excellent. Highly recommended!" 
PR3 = "I had a bad experience with this product. It didn't meet my expectations."
PR4 = "Poor quality product. Wouldn't recommend it to anyone."
PR5 = "The product was average. Nothing extraordinary about it."""
A = PR1.upper()
B = PR2.upper()
C = PR3.upper() 
D = PR5.upper()
print(A)
print(B)
print(D)
print(C)
#Task_2
Python_review = [ "This product is really good. I'm impressed with its quality.", "The performance of this product is excellent. Highly recommended!", "I had a bad experience with this product. It didn't meet my expectations.", "Poor quality product. Wouldn't recommend it to anyone.", "The product was average. Nothing extraordinary about it." ]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
Z = Python_review.count(positive_words[1])
X = Python_review.count(negative_words[0])
print(Z)
print(X)
PR1a = ["This product is really good. I'm impressed with its quality."]
PR2a = ["The performance of this product is excellent. Highly recommended!"] 
PR3a = ["I had a bad experience with this product. It didn't meet my expectations."]
PR4a = ["Poor quality product. Wouldn't recommend it to anyone."]
PR5a = ["The product was average. Nothing extraordinary about it."]
list =[input()]
suma1 = PR1a.append(input("add to review?")[:30])
print(suma1)
suma2 = PR2a.append(input("add to review?")[:30])
print(suma2)
suma3 = PR3a.append(input("add to review?")[:30])
print(suma3)
suma4 = PR5a.append(input("add to review?")[:30])
print(suma4)