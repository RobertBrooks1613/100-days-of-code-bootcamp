from bs4 import BeautifulSoup
import requests

def extract_numbers(string):
    return ''.join(filter(str.isdigit, string))

content = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(content.text, "html.parser")

# Find all 'titleline' elements
titlelines = soup.find_all("span", class_="titleline")

listed_titles_scores = []
highest_score = float('-inf')
highlight = ""
for i, titleline in enumerate(titlelines, 1):
    title = titleline.find('a')
    
    # Find the corresponding score (if it exists)
    link = title.get("href")
    score_elem = titleline.find_next("span", class_="score")
    score = score_elem.text if score_elem else "No score"
    
    listed_titles_scores.append(f"{i}: {title.text} - {score}\n link {link}\n")
    num = extract_numbers(score)
    if int(num) > highest_score:
        highlight = f"highlight: {i}: {title.text} - {score}\n link {link}\n"
        highest_score = int(num)

print(highlight + "\n")
for t in listed_titles_scores:
    print(t)


# with open("website.html", "r") as reader:
#     content = reader.read()

# soup = BeautifulSoup(content, "html.parser")

