word_per_page = 0
pages = 0
while True:
    try:
        pages = int(input("Number of pages: "))
        word_per_page = int(input("Number of words per page: "))
        break
    except ValueError:
        print("Use numbers only")

total_words = pages * word_per_page
print(f"Your total words should roughly be : {pages * word_per_page}")
