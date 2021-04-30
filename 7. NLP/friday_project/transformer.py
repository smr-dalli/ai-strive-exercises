from transformers import pipeline

# sent_analysis = pipeline('sentiment-analysis')
# result = sent_analysis("I really like this product.")[0]
# print(result['score'])

def translate(text):
    translators = pipeline('translation_en_to_de')
    text = translators(text)
    return text




