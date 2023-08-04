from wordcloud import WordCloud
from multidict import MultiDict

# Read the text from the file
with open('cv.txt', 'r') as file:
    text = file.read()

# Split the text into individual words
words = text.split()

# Create a multidict to store the word frequencies
word_dict = MultiDict()

# Iterate over each word and update the multidict
for word in words:
    word_dict.add(word, 1)

# Generate the wordcloud
wordcloud = WordCloud().generate_from_frequencies(word_dict)


# Save the wordcloud as an image file
wordcloud.to_file('wordcloud.png')

# Display the word cloud
wordcloud.to_image().show()


# Save the wordcloud as an image file
wordcloud.to_file('wordcloud.png')



