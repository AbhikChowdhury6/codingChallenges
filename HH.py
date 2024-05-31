from random import randint

numTrials = int(1e6)

numTries = []

for _ in range(numTrials):
    trial = []
    trial.append(randint(0,1))
    trial.append(randint(0,1))
    while trial[-2:] != [1,1]:
        # a = trial[-2:]
        trial.append(randint(0,1))
    numTries.append(len(trial))


#print(numTries[:100])
print(sum(numTries)/len(numTries))