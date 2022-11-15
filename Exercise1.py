# Adapt the code above to generate a 1000 character long string with weights based on the previous two characters.
#  Make HTTP requests for internet reqources.
import urllib.request

# The URL of a text version of Alice in Wonderland.
book_url = 'https://www.gutenberg.org/files/11/11-0.txt'

# Get the book.
book = list(urllib.request.urlopen(book_url))

# Decode the lines and strip line endings.
book = [line.decode('utf-8-sig').strip() for line in book]

# Get the whole book in one big string.
sbook = ''.join(book[26:]).lower()

chars = 'abcdefghijklmnopqrstuvwxyz '

# Create the weights - count the occurences of each character in the whole book.
weights = [sbook.count(c) for c in chars]

# Create the weights -  including the previous character as part of the weighting system.
triwght = {c: {d: {e: sbook.count(c + d + e) for e in chars} for d in chars} for c in chars}

# Start with space.
triples = ' '

# Do the following N-1 times.
for i in range(1, 2001):
    # Get the weights where the previous character is the last 2 character in twos.
    wt = triwght[triples[-2]]
    # Turn wt into a list, ordered by chars.
    wt = [wt[c] for c in chars]
    # Randomly pick the next character using those weights.
    nextc = random.choices(chars, weights=wt, k=1)[0]
    # Append the character to twos.
    triples = triples + nextc

# not working!
print(triples)

