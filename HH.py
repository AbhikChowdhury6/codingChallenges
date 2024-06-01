from random import randint
from multiprocessing import Pool



def runTrialsList(numTrials):
    numTries = []
    for _ in range(numTrials):
        trial = []
        trial.append(randint(0,1))
        trial.append(randint(0,1))
        while trial[-2:] != [1,1]:
            # a = trial[-2:]
            trial.append(randint(0,1))
        numTries.append(len(trial))
    return numTries

def runTrialsAvg(numTrials):
    numTries = []
    for _ in range(numTrials):
        trial = []
        trial.append(randint(0,1))
        trial.append(randint(0,1))
        while trial[-2:] != [1,1]:
            # a = trial[-2:]
            trial.append(randint(0,1))
        numTries.append(len(trial))
    return sum(numTries)/numTrials


#print(numTries[:100])
#print(max(numTries))
#print(sum(numTries)/len(numTries))

if __name__ == "__main__":
    numProcesses = 12
    with Pool(processes=12) as pool:
        numTrials = int(1e6)
        output = pool.map(runTrialsList, [numTrials]*12)
        outputList = []
        [outputList.extend(l) for l in output]
        print(sum(outputList)/(numTrials * 12))



