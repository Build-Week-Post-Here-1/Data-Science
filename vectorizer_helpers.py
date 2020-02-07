import en_core_web_md
import spacy

#Create the nlp object
nlp = spacy.load("en_core_web_md")

def get_lemmas(text):
        """Return the Lemmas"""
        lemmas = []
        doc = nlp(text)

        for token in doc:
            if ((token.is_stop == False) and (token.is_punct == False)) and (token.pos_ != 'PRON'):
                lemmas.append(token.lemma_)

        return lemmas
