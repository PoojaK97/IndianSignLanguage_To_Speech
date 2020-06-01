from two import *
from sacremoses import MosesTokenizer, MosesDetokenizer
# # from randomsentence.sentence_tools import SentenceTools
# from mosestokenizer import *
from nltk.tokenize.treebank import TreebankWordDetokenizer
# class SentenceTools:
#     def __init__(self):
#         self.detokenizer = MosesDetokenizer(lang='en')
#     def detokenize(self, tokens):
#         return self.detokenizer(tokens)
#     def detokenize_tagged(self, tagged_tokens):
#         return self.detokenize([token for token, tag in tagged_tokens])
# import doctest
# doctest.testmod()
# sentence_tools = SentenceTools()
# sentence_tools.detokenize_tagged(tagged_sentence)
mt, md = MosesTokenizer(lang='en'), MosesDetokenizer(lang='en')
print(md.detokenize([token for token, tag in tagged_sentence]))


