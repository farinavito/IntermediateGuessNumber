with open("score.txt", "r") as score_file:
    old_scores_raw = score_file.read()
old_scores_raw = old_scores_raw.split("\n")

old_scores = []
for i in old_scores_raw[:-1]:
    old_scores.append(int(i))
    old_scores.sort()

top_3_scores = old_scores[:3]
print(f"Top 3 results so far: {top_3_scores}")

import random
secret_num = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Ugibaj stevilo med 1 in 100: "))
    attempts += 1

    if guess < secret_num:
        print("Ugibaj visje")
    elif guess > secret_num:
        print("Ugibaj nizje")
    else:
        print(f"Bravo, uganil si v {attempts} poizkusih.")
        break

with open("score.txt", "a") as score_file:
    score_file.write(f"{attempts}\n")