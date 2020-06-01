j="dddd"
import subprocess
import sys

def install(package):
   subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('randomsentence')
import nltk
from randomsentence.sentence_maker import SentenceMaker
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')
sentence_maker = SentenceMaker()
tagged_sentence = sentence_maker.from_keyword_list(['i', 'shopping', 'go', 'will'])
print(tagged_sentence,"from insidddddddddddd")
