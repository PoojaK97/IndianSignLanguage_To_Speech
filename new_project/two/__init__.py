j="dddd"
import subprocess
import sys

def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('randomsentence')
import nltk
from randomsentence.sentence_maker import SentenceMaker
from randomsentence.grammar_check import GrammarCorrector
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
sentence_maker = SentenceMaker()
corrector = GrammarCorrector()
tagged_sentence = sentence_maker.from_keyword_list(['i', 'shopping', 'go', 'will'])
tagged_sentence = corrector.correct(tagged_sentence)
print(tagged_sentence,"from insidddddddddddd")
