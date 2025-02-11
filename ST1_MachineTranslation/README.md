# AmericasNLP 2025 Shared Task on Machine Translation into Indigenous Languages

Welcome to the Machine Translation Shared Task into Indigenous Languages! We are excited to host the **4th iteration** of the Shared Task. 


# Table of Contents
1. [Registration](#registration)
2. [Important Dates](#important_dates)
3. [Shared Task Description: Tasks and Rules](#shared-task-description-tasks-and-rules)
4. [Languages](#languages)
5. [Links to Prior Iterations](#links-to-prior-iterations)
6. [Contact](#contact)
7. [Baseline System](#baselines)

## Registration

Please use the following link to indicate your interest in participating: https://forms.gle/gXRoa9pr6K75Tgce7

## Important Dates
- Release of training and development sets: January 30th, 2025
- Release of baseline systems and baseline results: February 15th, 2025
- Release of test inputs: March 1st 2025
- Submission of results (shared task deadline): March 25th, 2025
- Announcement of winners: April 4th, 2025
- Submission of system descriptions papers: April 8th, 2025
- Notification of acceptance: April 11th, 2025
- Camera-ready papers due: April 14th, 2025
- Workshop: May 4th, 2025



## Shared Task Description: Tasks and Rules:

We are making some exciting changes and additions to the Shared Task for 2025!

**New for 2025**:

- [New languages!](#languages)
- [New translation direction: translation into Spanish](#new-translation-directions)


### New Translation Directions

For 2025, we are expanding the shared task to include both translation into an Indigenous language (from Spanish) **as well as** translation from an Indigenous language into Spanish. These different directions will be represented as two tracks within the shared task:

- **Track 1**: Systems which translate from Spanish into an Indigenous language (Es-XX)
- **Track 2**: Systems which translate from an Indigeous language into Spanish (XX-Es)


### Rules

The Machine Translation Shared Task will be broken down into 2 separate competitions:

- **Track 1** : Machine translation from Spanish into an Indigenous language (*similar to prior ST iterations*)
- **Track 2** : Machine translation from an Indigenous language into Spanish

Participants can submit to as many tracks as they wish. The same system can be submitted to multiple tracks if desired.

The following rules apply to all tracks:

1. Training on the development set is **not** allowed. Specifically, the dev set should only be used to evaluate a current model; as a rule of thumb, the model outputs at inference time should be consistent with or without access to the development set. If you have any questions or would like to clarify a specific approach, please contact the organizers!   
2. Using the [AmericasNLI](https://aclanthology.org/2022.acl-long.435.pdf) test set for hyperparameter tuning or any form of decision making is not allowed. 
3. Evaluation will be done using the `evaluate.py` script. The final order of teams will be selected using average **ChrF++** across all languages. Note that prior years have used *ChrF*. We accept submissions that do not cover all languages -- in these cases, the average ranking for these systems will be calculated using a *ChrF++* of `0.0` for each unsupported language. In this case, please reach out if you would like your system omitted from the overall rankings -- we still encourage you to submit a system description paper in this case!
4. We will **not** allow multiple submissions which rely on the same model (by same, we mean the same exact weights and architecture). As an example, if a submitted system relies on a specific model (say Model A), a second submission which relies on a new model (Model B) for some languages, but falls back to Model A given dev set performance, is not allowed. In this case, there are two allowed possibilites: (1) submit Model B as an independent submission with no fallback to Model A or (2) withdraw the original submission of Model A, and submit the system which relies on both Model A and Model B as a single submission. As a rule of thumb, two submissions from the same team should not have the same exact performance for a given language unless by chance.
5. **(New for 2025)**: While we will accept and present results from all submissions, only submissions which rely solely on models with **open-source weights** will be considered in the final shared task ranking.



## Languages

We are excited to add two new languages for the 2025 Shared Task: `Wayuunaiki (guc)` and `Awajun ()`, 

The complete list of languages is below:

| ISO| Language |
---|---|
 -| **Awajun**
aym | Aymara 
bzd |Bribri
cni | Asháninka 
ctp | Chatino 
grn | Guarani 
guc | **Wayuunaiki**
hch | Wixarika 
nah | Nahuatl 
oto | Otomí 
quy | Quechua 
shp | Shipibo-Konibo 
tar | Rarámuri 

## Links to Prior Iterations

For reference to the prior shared tasks, winning submissions, and further analysis on the data and results, please see the prior Findings and system description papers, linked below:

| Year | Findings | System Description Papers |
|--|--|--|
| 2021| [Findings](https://aclanthology.org/2021.americasnlp-1.23/) | [Submitted Systems](https://aclanthology.org/volumes/2021.americasnlp-1/) |
| 2023| [Findings](https://aclanthology.org/2023.americasnlp-1.23/) | [Submitted Systems](https://aclanthology.org/volumes/2023.americasnlp-1/) |
| 2024| [Findings](https://aclanthology.org/2024.americasnlp-1.28/) | [Submitted Systems](https://aclanthology.org/volumes/2024.americasnlp-1/) |


## Contact

We are more than happy to answer any questions regarding the workshop or shared task, please email us at [americas.nlp.workshop@gmail.com](malito:americas.nlp.workshop@gmail.com). Alternatively, [join our Slack channel](https://join.slack.com/t/americasnlp/shared_invite/zt-2c3lstrpe-n6DXqZyGVXVqDaGiM7mbHA).



## Baselines

Baseline systems to be announced soon!

