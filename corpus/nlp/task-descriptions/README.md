# NLP Task Description Review Brief - Clean Corpus

## Objective:
This brief outlines the purpose and key aspects of NLP Task Descriptions (NTDs)
used to train our Natural Language Processing (NLP) models.

You will use this information to assess the completeness, relevance, accuracy,
and overall usefulness of NTDs for training AI NLP models and returning correct
useful results after being trained on the NTPs..

## What is an NLP Task Description (NTD)?
An NTD is a document that details the specific task an NLP model needs to
learn. It provides various data formats and human-written descriptions that the
model will be trained on. This allows the model to understand the task, the
relevant terminology, and how to process natural language input related to that
task.

## Key Components of an NTD:
### Task Definition:
A clear and concise description of the specific NLP task. (e.g., generating
flowcharts from textual/spoken descriptions) it must explain the task as if the
listener has no knowledge or understanding of the content but they do know
about diagrams and flowcharts and the kind of content each is suited to.

## Data
This section should include:

### Explicit Data Description:
A detailed explanation of the data the NLP model should be able to interpret
and translate into the desired output format. (e.g., flowcharts) This should be
presented in a way that someone could verbally describe the data to another
person over the phone and the listener could draw the data and the diagram
would be correct.

### Raw Data:
This can be presented in various formats depending on the task (e.g., CSV for
tabular data, Mermaid or ASCII code for flowcharts)

### Mermaid Example:
A mermaid code example of the desired output (e.g., a flowchart
in mermaid code)

## User Requested Task/Data Descriptions
This section is headed "User-Requested Data Descriptions" and contains 5
actor/user data descriptions with headings "Data Description [1-5]", one per
actor. It provides textual/spoken descriptions of the task and its data from
various user/actor perspectives (e.g., software developer, project manager)

These descriptions should be diverse in phrasing and terminology to enrich
the training data and be written in a way that the listener could draw the
correct diagram from the description. The way each description is written
should be authentic to the actor who is requesting the diagram in terms of
detail, verbosity/terseness, formality and chosen wording.

The description should be as detailed as necessary to accurately convey the
information to be presented while considering the likely level of detail that
specific actor would provide.

This model is aimed at presentation of data in business & software
development documentation so the descriptions should be written in a way that
is appropriate for that context. Irrelevant conversational details should be
avoided in this corpus.

The likely use case for this model would be a plugin that allows the user to
highlight text in a document and have a flowchart of the process described in
the text generated or a vscode plugin that allows a user to right click on a
section of code or file and generate diagram options suitable for it.

Some degree of ambiguity or missing information is expected to reflect
real-world scenarios, the model should identify points of ambiguity or
missing data in the description and identify them for clarification.


## Validation & Scoring Criteria:
This section defines the expected outcome of the NLP model and establishes a
scoring system to evaluate its performance. This includes:
- **Expected Result:** A clear description of the correct output the model
  should generate for a given input.
- **Scoring Weights:** A breakdown of criteria used to evaluate the model's
  output, assigning weights to different aspects (e.g., component matching,
  semantic accuracy, completeness).
- **Clarifying Questions:** 5 example questions the NLP model could
  ask to clarify ambiguities or missing information in each user/actors
  task/data description, helping it arrive at between 1 and 3 possible
  solutions quickly.

  **Critical Criteria:**

  - *All 5 actors must be describing the same data*
  - *All 5 actors must be describing the same desired outcome from their own perspective*
  - *Each solution must fit the data*
  - *Each solution must accurately display the data*
  - *Each solution must be appropriate for the context it will be presented in
    and its intended use*

  The model has 3 available response templates when replying to a user request.
  When communicating in a clarifying question context, the model should try to
  lose the least amount of points possible while still returning a correct
  result. Scoring may differ between contexts but for now we should only
  consider the clarifying question context.

  **Response Templates:**
    - **Yes/No** questions:

      Questions that can be answered with a simple yes or no. (Score: -1)
    - **Multiple Choice** questions:

      The model should provide a question and a set of answers that help
      clarify any uncertainty and are relevant to the task and the context of the data, the actor
      and
      the request/description.

      Questions that provide up to 5 possible answers for the user to choose
      from. The model can set the number of responses allowed for the question.
      In many contexts the maximum allowed responses will be 1 (radio
      selector), but in other contexts it may be helpful to allow more than one
      response to be selected (check boxes).

       (Score: -1 per option)
    - **Open-ended** questions:

      These questions require a more detailed plain text/spoken answer to
      clarify the request or anything else required to reduce ambiguity or
      missing information. (Score: -10)

## Reviewing NLP Task Descriptions:
Reviewers should assess NTDs based on the following criteria:
- **Completeness:** Does the NTD include all essential components listed above?
  (Score: 0 - 25)
- **Relevance:** Does the data and its descriptions directly relate to the
  defined NLP task? (Score: 0 - 10)
- **Accuracy:** Is the data presented correctly and free of errors? (Score: 0 -
  25)
- **Usefulness for Training:** Does the NTD provide sufficient and diverse
  training data for the NLP model to learn the task effectively? (Score: 0 - 25)
- **Clarity:** Is the NTD well-structured and easy to understand? (Score: 0 - 10)
- **Consistency:** Are the data descriptions consistent with the expected
  outcome and scoring criteria? (Score: 0 - 25)

## Additional Notes:

It is important that these documents are accurate, detailed, and diverse to
ensure the NLP model can learn the task effectively. Reviewers should provide
constructive feedback to improve the quality of NTDs and enhance the
performance of NLP models before making any changes. It is critical that I
approve all changes to these documents before they are implemented.

## Conclusion:

Well structured and informative NTDs are crucial for training effective NLP
models. Reviewers play a vital role in ensuring these documents meet the
necessary standards for successful NLP model development.

Your feedback should be detailed, specific, and focused on improving the
quality and effectiveness of NTDs for training AI NLP models.

Return the results for each document in a table with the scoring criteria, the
score and a brief summary of your assessment for each category. There should
also be a final summary of the overall quality of the NTD and any
recommendations for improvement.
