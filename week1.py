#Week 1 Test

# For file with only numbers, you should only return one thing(i.e.the first 10 characters)

# For file with story,you NEED to return two things(i.e. a modified string AND a list)
#  you can return multiple values by simply return them separated by commas like the following
# def editor(fname):
#
#     return 'modifystring', [a,b,c,d]

# HINT: to call your function for the story.txt file, use the following command
# editor("./data/story.txt")
# return statement should be in the format below
# return 'modifystring', [a,b,c,d]



import re
from collections import Counter

def editor(fname):
    #YOUR CODE STARTS HERE
    with open(fname,'r') as file:
        content = file.read().strip()
        if content.isdigit():
            return 'first 10 digit is:' + content[:10]
        else:
            modified_string = content.lower().replace('\n', '')
            words = re.findall(r'\w+', modified_string)
            word_counts = Counter(words)
            top5_words = [word for word, count in word_counts.most_common(5)]
            return modified_string, top5_words















