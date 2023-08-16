from translate import Translator

translator = Translator(to_lang="pl")

def translate_words(english_words):
    translated_pairs = []
    
    for word in english_words:
        translated_word = translator.translate(word).strip()
        translated_pairs.append(f"{word} - {translated_word}")
    
    return translated_pairs

input_filename = "input.txt"
output_filename = "output.txt"

try:
    with open(input_filename, "r", encoding="utf-8") as input_file:
        english_words = input_file.read().splitlines()
        
    translated_pairs = translate_words(english_words)
    
    with open(output_filename, "w", encoding="utf-8") as output_file:
        output_file.write("\n".join(translated_pairs))
        
    print("Translation completed successfully.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)
