# AI Diagram Agent

I want to build an AI agent that can generate system, software, process, org,
gannt diagrams/charts/graphs (hereafter referred to as "diagrams") and other
diagrams used in documentation to help better explain what the writer is trying
to communicate.

The agent can take user provided description, data and or content, interpret it
and generate visual representations in a form that is helpful, accurate and
improves the ease of understanding of the subject matter.

As a first step, the agent should be able to generate mermaid formatted
markdown code that can be rendered by mermaid.js. Later on we may add other
methods which provide richer more dynamic visualisation options.

I want to use a combination of machine learning, natural language processing, a
knowledge base and a rules engine to generate the diagrams. The agent should be
able to learn from user feedback and improve over time.

I don't want to use 3rd party API's or services, but I am happy to use open
source libraries, models, corpii and tools.

I prefer python as the backend language of choice, but I am open to other
languages if a compelling argument can be made for their use. Frontend can be
in any language or framework that is best suited to the task.

pep8, conventional commits, semver and google style guide should be followed.

FAISS in standalone python library mode should be used for vector database.
MySQL should be used for the main database. S3 should be used for file storage.
The application will be deployed using fluxcd, helm, kubernetes and docker.

I want to use:
    - gihub actions for CI/CD
    - pytest for testing
    - fastapi for the API
    - pydantic for data validation
    - sqlalchemy for the ORM
    - mermaid for the diagrams
    - FAISS for the vector database
    - MySQL for the main database
    - S3 for file storage
    - fluxcd for deployment
    - helm for package management
    - kubernetes for container orchestration
    - docker for containerization
    - gymnasium for reinforcement learning
    - comet for model tracking documentation and collaboration
    - Google python style guide

Diagram types which must be available at MVP (same as mermaid-py library):
    - Flow Chart
    - Sequence Diagram
    - State Diagram
    - Entity Relationship Diagram
    - User Journey
    - Pie Chart
    - Requirement Diagram
    - Mindmap

These are all currently available using the mermaid-py pip library. I want to offer all of the options that mermaid.js provies before we move to version 1.0.0

Lets start with Flowchart, and Pie Chart options and once we have them working we can pad out the rest.

## Data Analysis

The agent will interpret the content provided and decide if it has a better
than 50% chance of one of 3 visual options it will provide being chosen
(The "certainty threshold") as the basis of any further iteration.

If it does, the agent will move into the suggestion phase.

If it does not, the agent will move into the question and answer phase.

If no initial content/data is provided, the agent will move straight into
the question and answer phase.

The agent should save anonymized and sensitive information scrubbed content to
a vector database for reinforcement learning and model optimization purposes.

## Question and Answer Phase

The question and answer ("needs analysis") phase will be a conversation between
the user and the agent. The agent will ask a question and the user will provide
a response. This will continue until the agent crosses the certainty
threshold and can move into the suggestion phase.

Where content has been provided, the agent should aim to ask 3 or less
clarifying questions in order to cross the certainty threshold and have enough
information to move into the suggestion phase.

Where no content has been provided or the content provided was significantly
insufficient, the agent should aim to ask 6 or less clarifying questions in
order to cross the certainty threshold and have enough information to move into
the suggestion phase.

The agent should save anonymized and sensitive information scrubbed content
question & answer data to a vector database for reinforcement learning and
model optimization purposes.

## Suggestion Phase

Once the agent has crossed the certainty threshold, it will provide the user
with between 1 and 3 visual options based on the content and clarifying
questions provided.

The user can then:
  - choose one (or more) of the options provided
  - choose one (or more) of the options with some clarifying feedback/modifications or;
  - provide feedback on a totally different approach which will re-commence the data
    analysis and question and answer phase.

If an option is chosen without feedback, the agent will move into the content
delivery phase.

If an option is chosen with feedback, the agent will move into the
feedback/iteration phase.

If a totally different approach is chosen, the agent will move back into the
data analysis phase to see if it can cross the certainty threshold with data it
already has.

The agent should save anonymized and sensitive information scrubbed content
suggestion phase data to a vector database for reinforcement learning and
model optimization purposes.

## Feedback/Iteration Phase

The feedback/iteration phase is the fine tuning phase for the final product. We
already have the basis of the visual representation, now we are just tweaking
it to make it perfect.

The agent will provide the user with a visual representation based on the
chosen option. The user can then provide feedback on specific details like the
orientation of the diagram, the size of the nodes, the color of the nodes, the
font size, the font color, the line thickness, the line color, the background
color, the layout, the spacing, the alignment, the text, the labels, the title,
the legend, the key, the scale, the units, the data, the source, the author,
the date, the version, the license and notes.

The agent will then make the changes and provide the user with the updated
visual representation. This process will continue until the user is satisfied
or the agent has reached the maximum number of iterations.

The agent should aim to gain approval to generate the content within 3 or less
iterations. If the agent has not gained approval within 10 iterations, it
should move back into the suggestion phase using the information gained from
the feedback/iteration phase.

Once the user is happy with the visual representation, the agent will move into
the content delivery phase.

The agent should save anonymized and sensitive information scrubbed content
from the feedback/iteration phase to a vector database for reinforcement
learning and model optimization purposes.

## Content Delivery Phase

The content delivery phase is the final phase of the process. The agent will
provide the user with the final visual representation. The user can then select
the format they would like the visual representation in. The agent will then
provide the user with the visual representation in the selected format.

By default, the agent will provide the user with the visual representation in a
mermaid formatted markdown code that can be rendered by mermaid.js. The user
can then copy and paste the code into their documentation.

The user can choose to download the diagram in the following formats:
    - svg
    - png
    - pdf

Generated files will be uploaded to s3. A presigned URL will be provided to the user
to download the file(s). The download link will expire in 48 hours.

## User Interface

The agent will have a CLI and a web interface. The CLI will be a simple text
based interface. The web interface will be a simple form based interface with
streaming content delivery so the application can be updated in real time.

Both CLI and web interface must use the same API. No logic or functionality
other than authentication and presentation should be contained in any interface.

The user must be able to upload CSV, DOCX, XLSX and TXT files with the content
they want to visualize as well as just pasting the text into the chat box.

Previous chats must be saved and accessible to the user.

Users must be able to signin, signup, view & save preferences and logout.

OpenID should be used for authentication providing authentication with:
    - Google
    - Microsoft
    - Apple

## API

The agent will be accessible via an API. The API will be a RESTful API using
FastAPI.

You will need to design the API schema. Make it simple to use and understand.
Make sure it has a standards compatible /health endpoint for monitoring. The
health endpoint must run the following checks:
    - Check the status of the database connection
    - Check the status of the model
    - Check the status of the vector database
    - Check the status of the s3 connection
    - Check the status of unit tests

All must pass for the health endpoint to return a 200 status code.

API oauth key based authentication will be used for API access.


## NLP Models:
Lets use an open source NLP model and then fine tune/train/embeddings it
further as it is used with further learnings. Feedback loops with scores of
results, user input and product the model generates should all be fed back into
the model so it can learn what users do and don't want. It can also learn more
about the terminology wrapped around the work it is doing.

Ambiguity in language should use the same certainty threshold as well as the
question & answer process used in the rest of the workflow. Asking questions
that help the model cross the certainty threshold is the way we will deal with
any ambiguity. 

We will also train on the results of this process.

## Certainty Threshold

Higher scores will be provided for questions/steps that get the model past the
certainty threshold with the least questions/interactions for the user.

I think Markov decision process and Q-learning are going to be the right way to
implement this but I'm happy to be to be told something else is going to be
more effective. This process should be visualized using comet so progress can
be tracked.

The simplest example of certainty would be selection of diagram type. Some
diagrams are better suited to a specific data type. For instance if the content
was a description of an organisational hierarchy a pie chart would definitely
not work, nor would a line chart but a state diagram or a flowchart might work.

# User Interface

The interface is going to be a simple chat interface, similar to Gemini or chat
GPT. If the user can type and explain what they want then they should be able
to use it.

It would be good if users can upload png, csv, docx, xlsx and txt files that
the agent can use to generate the diagrams. The agent should be able to read
the files and ask questions about the content in order to generate the diagram.

In the chat interface, start with simpler diagrams and add complexity only if
the user confirms or requests it. This avoids overwhelming them. The agent can
ask questions while providing options (multiple choice?) to help determine the
complexity of the diagram required while also guiding the user towards the best
option. 

## Data Security and Privacy

Sensitive and identifying data will be redacted and left blank before it is
sent to training. Where the entire document is financial or personally
identifying, that data won't be trained on.

Users will absolutely own the output of the agent. We will reserve the right to
train on the interactions and data they provide. We need to clearly communicate
what we view personally identifying and confidential data in our documentation.

## Knowledge Base/Training Corpus
The knowledge base is for the agent and will be a base corpus of documentation,
manuals and examples of final product using mermaid formatted markdown. It will
be used to train the agent on what the final product should look like and the
rules of the system.

A rules engine will be used that defines how the agent should interpret and be
scored on how it interprets the content. The rules engine will be trained on
the knowledge base.

Model Interperatability via LIME or SHAP will be used to explain the decisions
the model makes. This will be used to help improve the model and to help users
understand why the model made the decisions it did.

## Data Validation

Before passing content to the model, implement rules/checks to catch things
like malformed CSV files or extremely long text blocks (to prevent the model
from getting overwhelmed).

## Domain Adaptation

The model should be able to adapt to different domains within the context of
creating high quality diagrams using mermaid formatted markdown. It is not
anticipated we will need to know dates that events happened in history or other
generalized knowledge.

The model should be able to adapt to different contexts that the data might
come from or is trying to communicate. For instance, a flowchart for a software
project might look different to a flowchart for a business process.

## A/B Testing

Base NLP models, rules engines and other parts of the system will be A/B tested
on an ongoing basis. We will use the results of these tests to improve the
agent and to make dynamic self-adjustments to the system as required.

## Unit/CI/CD Testing

Unit tests will be run as GitHub actions on every merge to the main branch and
push to non-main branches. End to end tests will be run on every release and on
demand for developers own environments. We will use pytest for testing.

## Standards for presentation

UML is one standard for certain types of charts. We should use it and any other
standards that are relevant to each diagram/information type. We should also be
able to generate the diagrams in a format that can be used by other tools like
draw.io, lucidchart, omnigraffle, visio, etc.

## Performance Expectations

The agent should be able to generate conversation content and clarifying
questions within 3 seconds. The agent should be able to generate suggestions in
5 seconds. The agent should be able to generate feedback/iterations in 10
seconds. The agent should be able to generate final content for delivery in 15
seconds.

## Future Features

    - Real time collaboration
    - draw.io integration
    - Office365 integration
    - Google Docs integration
    - Confluence integration
    - Jira integration
    - Wordpress integration
    - Save as:
        - markdown
        - visio
        - omnigraffle
        - draw.io
        - lucidchart

## Required SDLC Document Set
    - SDLC Plan
    - Project Plan
    - Technical Architecture
    - API Schema
    - Design Documents
    - Deployment Documentation
    - User Guides

