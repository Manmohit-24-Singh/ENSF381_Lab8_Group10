import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:
    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')
    print(f"Successfully fetched content from {url}")
except Exception as e:
    print(f"Error fetching content: {e}")

print('-'*50)
print("Page Content")
print(soup.prettify())


print('-'*50)
h_count = sum(len(soup.find_all(f"h{i}")) for i in range(1, 7))
l_count = len(soup.find_all("a"))
p_count = len(soup.find_all("p"))
print("Webpage Analysis")
print(f"Number of headings: {h_count}")
print(f"Number of links: {l_count}")
print(f"Number of paragraphs: {p_count}")



print('-'*50)
page_text = soup.get_text().lower()
kwrd = input("Enter a keyword: ").strip().lower()
kwrd_count = page_text.count(kwrd)
print("Keyword Search Result")
print(f"The keyword '{kwrd}' appears {kwrd_count} times on the webpage.")


print('-'*50)
text = ""
for char in page_text:
    if char.isalpha() or char.isspace():
        text += char

words = text.split()
wrd_counts = {}
for i in words:
    if len(i) > 1:
        if i in wrd_counts:
            wrd_counts[i] += 1
        else:
            wrd_counts[i] = 1

top_words = []
for i in range(5):
    frequent_word = None
    frequent_count = 0
    for j, k in wrd_counts.items():
        if k > frequent_count:
            frequent_word = j
            frequent_count = k
    top_words.append((frequent_word, frequent_count))
    del wrd_counts[frequent_word]

print("Top 5 Most Frequently Used Words")
for i, j in top_words:
    print(f"{i}: {j}")


print('-'*50)
longest_paragraph = ""
max_word_count = 0

for i in soup.find_all("p"):
    text = i.get_text(strip=True)
    words = text.split()
    word_count = len(words)

    if word_count >= 5 and word_count > max_word_count:
        longest_paragraph = text
        max_word_count = word_count
print("Longest Paragraph")
print(longest_paragraph)
print(f"Word Count: {max_word_count}")


import matplotlib.pyplot as plt
labels = ['Headings', 'Links', 'Paragraphs']
values = [h_count, l_count, p_count]
plt.bar(labels, values)
plt.title('Group 10')
plt.ylabel('Count')
plt.show()