from os.path import exists


# function to create new categories for the webscrapper to search for
def createCategories():
    categories = []

    print('Enter the first keyword or phrase to search for: ', end='')
    categories.append(str(input()))

    print('Enter the second keyword or phrase to search for: ', end='')
    categories.append(str(input()))

    print('Enter the third keyword or phrase to search for: ', end='')
    categories.append(str(input()))

    print('Enter the fourth keyword or phrase to search for: ', end='')
    categories.append(str(input()))

    print('Enter the fifth keyword or phrase to search for: ', end='')
    categories.append(str(input()))

    with open('newsdata.txt', 'w+') as f:
        for category in categories:
            f.write(category)
            f.write('\n')


def main():
    dataPath = './newsdata.txt'

    # If no categories are saved, prompt the user to select 5 categories
    if not exists(dataPath):
        createCategories()


if __name__ == "__main__":
    main()
