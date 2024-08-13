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
    2. [Wearable Technology Class in The Fashion School at ASU](#fashionclass)
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
TL;DR We found that fine-tuning LLMs on responses from empathetic human listeners improved their performance on emotional reasoning tasks and that fine-tuning on poor listeners degraded their performance.

Emotionally contextualized responses from chatbots have been shown to improve users’ trust in systems. In this work, we fine-tuned 4 different LLMs on the PAIR (Prompt-Aware margIn Ranking)  dataset, which consists of conversational responses annotated by expert counselors as reflecting “good listening” or “bad listening”

We then evaluated those models’ performance on a random sample of 500 questions from the SocialIQA dataset. We found that fine-tuning on interactions with good listeners improved accuracy across all models, and accuracy was degraded when fine-tuning on interactions with poor listeners.

The code can be found here: https://github.com/AbhikChowdhury6/LLMsModelingGoodListeners

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/fineTuningGL.png?raw=true" width="600">



### Future Task Rewards in Multiagent Reinforcement Learning (RL)<a name="futuretasks"></a>

TL;DR We extended an RL paper from DeepMind, which proposed incorporating rewards from potential future tasks to incentivize an agent not to generate negative side effects. Our extension was to apply this technique to multiagent environments.

When building agents to carry out complex real-world tasks, it is often difficult to program how to complete a desired task, and so instead, the field of Reinforcement Learning (RL) provides a framework for agents to discover how to complete tasks given their capabilities in an environment and get rewards. While RL can be a powerful tool that enables
agents to discover skills that would be intractable to program manually, the learned behaviors can also lead to a number of unintended consequences. One category of these unintended consequences is referred to as Negative Side Effects (NSE).

The problem of NSEs arises when trying to describe what change you would like an agent to cause, and in this case, one must also ensure that the agent also knows all of the
changes you would not like to cause. For example, if the shortest path to accomplishing a described goal has the potential of knocking over a vase, breaking a wall, or crashing a car in the process, then the agent would do those things since they may not have explicitly been told everything not to do.

To address this the original paper proposed the future task approach which considers the current task as part of a sequence of unknown tasks and provides an auxiliary reward to the current agent for the potential to complete various future tasks. We rebuilt the environment and agents and reward functions using OpenAI Gym, utilizing their PettingZoo multiagent framework.

We found that introducing another agent into the environment did not degrade the agents ability to avoid certain negative side effects, but aspects of the original environment reward system, casted doubt on the validity of those results to the team.

The code can be found here: https://github.com/wgrier-asu/teamSAi

The presentation can be found here: https://docs.google.com/presentation/d/1iIqESR-mCCwjwUynaICx2lK2DRKtYrp4ygw-gEcjrXI

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/multiAgent.gif?raw=true" width="300">


### Continuous Glucose Monitoring Modeling <a name="glucose"></a>

This project aimed to classify a window of blood sugar data with whether there was a meal during that time.

The training data was originally formatted as a time series of blood sugar levels and markers for meal times, segmented windows of meals and non meals. I generated some standard features for the meal and not meal data to assist the classifier with the small amount of data. I tested an SVM classifier with various kernels using k-fold cross-validation.

The code can be found here https://github.com/AbhikChowdhury6/CGMcomp

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/CGM.png?raw=true" width="300">

### Wrist-worn Camera Object Identification <a name="llms"></a>

I implemented a concept into a series of devices that could capture camera views from the wrist. We developed an end-to-end object recognition demo using TensorFlow, validating the device's use as a memory augmentation. This work enabled $500k+ in grants and counting to continue research and multiple patents.

The code can be found here: https://github.com/AbhikChowdhury6/handcam

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/handcamProto.jpg" width="300">
<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/keys10229.jpg" width="300">

### Sleep Tracker Data Analysis <a name="qssleep"></a>


Aligned sleep data from 3 wrist-based sleep trackers, a smart ring, and an under-mattress tracker.  Analyzed inconsistencies in predicted sleep stages and performance for tracking polyphasic sleep.

At the time, the Amazon halo band (purple) and pillow app for sleep tracking on the Apple watch (blue) didn’t register naps, the Oura ring 2 (green) did not attempt to predict sleep stages during naps, the Fitbit Charge 4 (orange) would attempt sleep stage tracking for longer naps around two hours or more, and the Withings sleep pad (red) was good at tracking, but of course could not sense naps not taken in bed.

The presentation can be found here: https://docs.google.com/presentation/d/1ItZ8jAxl0TGqR20lN6VzB8wObBdyKx0Q8bgiz4pZ7_0/edit?usp=sharing 
and code here: https://github.com/AbhikChowdhury6/qsPrez

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/sleepAnalysis.png">

### CPR Practice App Algorithm Development <a name="cprapp"></a>
A mobile app used to train hundreds of people on how to do hands-only CPR, my contribution being the accelerometer signal processing to derive the depth and frequency of compression.

## Data Engineering<a name="dataengineering"></a>


### Kubernetes Network Configuration<a name="kubentwork"></a>

### Hybrid Cloud Setup<a name="hybridcloud"></a>

## Talks and Awards<a name="talks"></a>
I did some projects

### Vision Hack Computer Vision Hackathon in Moscow (Russia) -  Most Innovative Award <a name="visionhack"></a>

Represented Arizona State University for the VIsionHack computer vision hackathon in Moscow Russia. The competition focused on identifying objects in video clips relevant to self-driving cars. Our team prioritized using classical machine learning techniques for explainability and won the most innovative award. 

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/russiaAward.jpg?raw=true" width="600">

### Bias in NLP Talk for LA Tech for Good Equity in Data Workshop Series <a name="biasinnlp"></a>
In 2021, I presented common Biases in Natural Language Processing systems and common approaches to address them for LA Tech For Good’s spring cohort. The presentation can be found here. https://docs.google.com/presentation/d/1zwXn2MowSf9qtVjamijvSSwvJ7sJleuu-Hu3Di8ZAOw/

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/laTechForGood.png?raw=true" width="600">

### “DIY Wearables” Workshop Conducted at Media Lab<a name="dataengineering"></a>
For the 2019 Community Biosummit at the MIT Media Lab, I ran a workshop where participants made a breathing sensor chest strap. The sensor had a variety of transient effects and I wrote code for processing the signal.

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/wearablesWorkshopMIT.jpg?raw=true" width="600">

## Stakeholder Engagement and Business<a name="business"></a>

### Eyes On - Augmenting Nonvisual Travel Using Haptic Interfaces<a name="eyeson"></a>

I implemented multiple devices In collaboration with Bryan Duarte, whose PhD research involved building and testing haptic wearables to augment non visual travel. During the course of the research we ran human factors studies with individuals who were blind.

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/eyesOnPoster.jpg?raw=true" width="600">

### Wearable Technology Class in The Fashion School at ASU <a name="fashionclass"></a>

In Spring of 2020 I co-instructed a wearable technology class in Fashion department at Arizona State University. Funded with a grant from the Global Sports Institute, students developed minimum viable products and pitched solutions for sport-related problems. 

## Other Work on Wearable Devices<a name="wearables"></a>

### Resonea - Wearable Microphone for Sleep Analysis <a name="resonea"></a>

Resonea, a biosignal processing company, developed an algorithm to detect various sleep features from audio data from users smart phones. I built a wearable sensor platform that integrated into their existing signal processing pipeline. 

<img src="https://github.com/AbhikChowdhury6/codingChallenges/blob/main/portfolioImages/resonea.jpg?raw=true" width="300">

### Compression Sleeve for Basketball Analysis <a name="basketballsleeve"></a>
I built a data logging platform into a compression sleeve as a platform for algorithms to analyze free throws. I wrote software for firmware and data validation. (pictured is a different motion sensor I designed using similar sensors.) basketball