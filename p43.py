#Find the Runner-Up Score
n = int(input("Enter the number of scores: "))
scores = list(map(int, input("Enter the scores separated by space: ").split()))

unique_scores = list(set(scores))
unique_scores.sort(reverse=True)

if len(unique_scores) >= 2:
    runner_up_score = unique_scores[1]
    print(f"The Runner-Up Score is: {runner_up_score}")
else:
    print("There is no Runner-Up Score.")