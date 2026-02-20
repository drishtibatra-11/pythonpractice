#input a list of scores for n students .find the runner up scores
n=int(input("Enter how many numbers: "))
scores = list(map(int, input("Enter the scores: ").split()))
unique_scores = list(set(scores))
unique_scores.sort(reverse=True)
if len(unique_scores) > 1 :
    print("Runner-up score is:", unique_scores[1])
else:
    print("There is no runner-up not found .")