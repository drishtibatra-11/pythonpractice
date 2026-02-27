#wap to input scores of n students and print runner up score
scores=list(map(int,input("enter scores: ").split()))
scores=list(set(scores))
scores.sort()
print("runner up score: ",scores[-2])