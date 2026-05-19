import requests

def getRiddle(difficulty):
    response = requests.get(f"https://api.apileague.com/retrieve-random-riddle?api-key=1f532a394a454ca5a7b997b4a8031c40&difficulty={difficulty.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()

    riddle = data['riddle']
    answer = data['answer'].lower()
    print(riddle)
    print(answer)
    list = [answer]
    return list


for words in getRiddle("hard"):
    word = input("dlk")
    for wasd in word:
        if wasd in words:
            print("yes")
            break
