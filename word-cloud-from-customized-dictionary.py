# Import the necessary libraries
import matplotlib.pyplot as plt

# Import the `WordCloud` class from the `wordcloud` library
# The `wordcloud` library is a popular Python library used for generating word clouds, which are visual representations of text data where the size of each word corresponds to its frequency or importance in the text.
from wordcloud import WordCloud

# Define a word dictionary
word_dict = {'AWS':100, 'Business Continuity':30, 'Linux':30,'Database':30, 'Consulting & Delivery':40, 'Oracle':30, 'Terraform':20, 'Data Analytics':20, 'Python':20, 'Machine Learning':10, 'Migration':40, 'Cloud Advisory':50, 'FinOps':40, 'Automation/IaC':30, 'Cloud Architect':80, 'DBA':40, 'Project Management':30, 'Customer Engagement':60}

# Specify the font path
font_path = "/System/Library/Fonts/Monaco.ttf"


# Create a WordCloud object with the font path specified
wordcloud = WordCloud(width=1000, height=500, font_path=font_path).generate_from_frequencies(word_dict)

# Set the size of the figure (plot) to 15 inches in width and 8 inches in height
plt.figure(figsize=(15, 8))

# Display the word cloud image on the plot
plt.imshow(wordcloud)

# Remove the axis labels and ticks from the plot
plt.axis('off')

# Display the plot with the word cloud
plt.show()


