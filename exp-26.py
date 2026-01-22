from transformers import pipeline
translator = pipeline("translation_en_to_fr")
output = translator("hello,how are you?")
print([output[0]],["translation_text"])