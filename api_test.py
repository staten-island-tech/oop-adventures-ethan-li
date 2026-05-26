import requests
import random

# def getRiddle(difficulty):
#     response = requests.get(f"https://api.apileague.com/retrieve-random-riddle?api-key=1f532a394a454ca5a7b997b4a8031c40&difficulty={difficulty.lower()}")
#     if response.status_code != 200:
#         print("Error fetching data!")
#         return None
    
#     data = response.json()

#     riddle = data['riddle']
#     answer = data['answer'].lower()
#     print(riddle)
#     print(answer)
#     list = [answer]
#     return list


# for words in getRiddle("hard"):
#     word = input("dlk")
#     for wasd in word:
#         if wasd in words:
#             print("yes")
#             break

def getRiddle(difficulty):
    response = requests.get(f"https://api.apileague.com/retrieve-random-riddle?api-key=1f532a394a454ca5a7b997b4a8031c40&difficulty={difficulty.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    

    data = response.json()
    answer_list = str(data['answer']).lower()
    riddle = data['riddle']
    answer = [answer_list]
    print(answer)
    return answer, riddle


difficulty_gen = random.randint(1, 3)
if difficulty_gen == 1:
    difficult = "easy"
elif difficulty_gen == 2:
    difficult = "medium"
elif difficulty_gen == 3:
    difficult = "hard"

x, y = getRiddle(difficult)

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")  
print("Difficulty: " + difficult.capitalize())
for words in x:
    question = input(y + " ").lower()
    for word in question:
        if word in words:
            print("Correct")
            break
        else:
            print("Wrong")
            break
    break