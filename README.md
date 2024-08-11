# Table of contents
1. [Data and ML](#dataml)
    1. [Fine-tuning LLMs for Improved Emotional Reasoning](#llms)
    2. [Future Task Rewards in Multiagent Reinforcement Learning](#futuretasks)
    3. [Continuous Glucose Monitoring Modeling](#glucose)
    4. [Wrist-worn Camera Object Identification](#handcam)
    5. [Sleep Tracker Data Analysis](#qssleep)
    6. [CPR Practice App Algorithm Development](#cprapp)
2. [Data Engineering](#dataengineering)
    1. [Kubernetes Network Configuration](#kubentwork)
    2. [Hybrid Cloud Setup](#hybridcloud)
3. [Talks and Awards](#talks)
    1. [Vision Hack Computer Vision Hackathon in Moscow (Russia) -  Most Innovative Award](#visionhack)
    2. [Bias in NLP Talk for LA Tech for Good Equity in Data Workshop Series](#biasinnlp)
    3. [“DIY Wearables” Workshop Conducted at Media Lab](#wearablesworkshop)
4. [Stakeholder Engagement and Business](#business)
    1. [Eyes On - Augmenting Nonvisual Travel Using Haptic Interfaces](#eyeson)
    2. [Co-Instructed Wearable Technology Class in The Fashion School at ASU](#fashionclass)
5. [Other Work on Wearable Devices](#wearables)
    1. [Resonea - Wearable Microphone for Sleep Analysis](#resonea)
    2. [Compression Sleeve for Basketball Analysis](#basketballsleeve)
    3. [Sound Responsive Dress](#sounddress)
6. [Modeling Dynamics](#dynamics)
    1. [Unsafe Trajectory Modeling](#unsafetrajectories)
    2. [Optimal Stock Policy Simulation](#stocksimulation)


## Machine Learning and Data Analysis <a name="dataml"></a>
I did some projects

### Fine-tuning LLMs for Improved Emotional Reasoning <a name="llms"></a>
We found that fine-tuning LLMs on responses from empathetic human listeners improved their performance on emotional reasoning tasks and that fine-tuning on poor listeners degraded their performance. 

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/fineTuningGL.png?raw=true" width="600">



### Future Task Rewards in Multiagent Reinforcement Learning <a name="futuretasks"></a>

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/multiAgent.gif?raw=true" width="300">


### Continuous Glucose Monitoring Modeling <a name="glucose"></a>

This project aimed to classify a window of blood sugar data with whether there was a meal during that time.

The training data was originally formatted as a time series of blood sugar levels and markers for meal times, segmented windows of meals and non meals. I generated some standard features for the meal and not meal data to assist the classifier with the small amount of data. I tested an SVM classifier with various kernels using k-fold cross-validation.

The code can be found here https://github.com/AbhikChowdhury6/CGMcomp

https://github.com/AbhikChowdhury6/CGMcomp
<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/CGM.png?raw=true" width="300">

### Wrist-worn Camera Object Identification <a name="llms"></a>
<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/handcamProto.jpg" width="300">

### Sleep Tracker Data Analysis <a name="qssleep"></a>


Aligned sleep data from 3 wrist-based sleep trackers, a smart ring, and an under-mattress tracker.  Analyzed inconsistencies in predicted sleep stages and performance for tracking polyphasic sleep.

At the time, the Amazon halo band (purple) and pillow app for sleep tracking on the Apple watch (blue) didn’t register naps, the Oura ring 2 (green) did not attempt to predict sleep stages during naps, the Fitbit Charge 4 (orange) would attempt sleep stage tracking for longer naps around two hours or more, and the Withings sleep pad (red) was good at tracking, but of course could not sense naps not taken in bed.

The presentation can be found here: https://docs.google.com/presentation/d/1ItZ8jAxl0TGqR20lN6VzB8wObBdyKx0Q8bgiz4pZ7_0/edit?usp=sharing and code here: https://github.com/AbhikChowdhury6/qsPrez

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/sleepAnalysis.png" width="300">

### CPR Practice App Algorithm Development <a name="cprapp"></a>
A mobile app used to train hundreds of people on how to do hands-only CPR, my contribution being the accelerometer signal processing to derive the depth and frequency of compression.

## Talks and Awards<a name="talks"></a>
I did some projects

### Vision Hack Computer Vision Hackathon in Moscow (Russia) -  Most Innovative Award <a name="visionhack"></a>

Represented Arizona State University for the VIsionHack computer vision hackathon in Moscow Russia. The competition focused on identifying objects in video clips relevant to self-driving cars. Our team prioritized using classical machine learning techniques for explainability and won the most innovative award. 

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/russiaAward.jpg?raw=true" width="600">

### Bias in NLP Talk for LA Tech for Good Equity in Data Workshop Series <a name="biasinnlp"></a>
In 2021, I presented common Biases in Natural Language Processing systems and common approaches to address them for LA Tech For Good’s spring cohort. The presentation can be found here. 1zwXn2MowSf9qtVjamijvSSwvJ7sJleuu-Hu3Di8ZAOw

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/laTechForGood.png?raw=true" width="600">

### “DIY Wearables” Workshop Conducted at Media Lab<a name="dataengineering"></a>
For the 2019 Community Biosummit at the MIT Media Lab, I ran a workshop where participants made a breathing sensor chest strap. The sensor had a variety of transient effects and I wrote code for processing the signal.

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/wearablesWorkshopMIT.jpg?raw=true" width="600">
