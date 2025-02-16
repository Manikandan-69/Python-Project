"""
pip install transformers

The purpose of text generation is to automatically generate text that is indistinguishable from a text written by a human.

GPT-2 stands for Generative Pre-trained Transformer 2.
It is an open-source Natural Language Processing model created by OpenAI. 
It can generate paragraphs of text with state of the art performance on many language benchmarks. 
It is also used for machine translation, question answering, and text summarization.
"""

from transformers import pipeline
model=pipeline('text-generation',model='gpt2')

sentence=model('Hi.My Name is Manikandan, I am a Datascientist', 
               do_sample=True,
               top_k=30,
               temperature=0.8,
               max_length=150,
               num_return_sentence=2)

"""
model("Hi, My name is John Cena, I am here", ...)

The input text "Hi, My name is John Cena, I am here" is passed to the language model to generate text.

do_sample=True

Enables sampling instead of greedy decoding, meaning the model will pick words randomly (based on probabilities) rather than always choosing the most likely one.
This makes the output more diverse and creative.

top_k=50

Limits the sampling to the top 50 most probable words at each step, reducing the chance of selecting unlikely words.
This helps maintain quality while adding randomness.

temperature=0.9

Controls the randomness of predictions.
Lower values (e.g., 0.1 - 0.5) → More deterministic (chooses high-probability words).
Higher values (e.g., 0.9 - 1.5) → More creative and diverse (chooses less probable words sometimes).
0.9 adds some randomness but still keeps coherence.

max_length=100

The generated text will have a maximum of 100 tokens (words, subwords, or characters, depending on the tokenizer).

num_return_sentences=2

Generates two different completions based on the input text.

"""

print(sentence)