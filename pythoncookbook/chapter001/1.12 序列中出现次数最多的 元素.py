words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes',  'not', 'around', 'the',
    'eyes',  'dont\'t', 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', 'you\'re', 'under'
]
from collections import Counter

word_counts = Counter(words)
print(type(word_counts))
top_three = word_counts.most_common(3)
print(top_three)