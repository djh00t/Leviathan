import spacy
from spacy.lang.en import English
import spacy.cli

# Set the model name. 
# English options are:
# - en_core_web_sm (small model)
# - en_core_web_md (medium model)
# - en_core_web_lg (large model)
# - en_core_web_trf (transformer-based model)
MODEL = "en_core_web_trf"

# Download the model if it isn't available
spacy.cli.download(MODEL)

# Load the model
nlp = spacy.load('en_core_web_trf')

# Import the transformer-based model
import en_core_web_trf

# Load the transformer-based model
nlp = en_core_web_trf.load()

# Process some text
doc = nlp("This is a sentence.")

# Print the text and the predicted part-of-speech tags
print([(w.text, w.pos_) for w in doc])