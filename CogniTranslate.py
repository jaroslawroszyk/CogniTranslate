from translate import Translator

class CogniTranslateTool:
    def __init__(self, input_filename, output_filename, language):
        self.translator = Translator(to_lang=language)
        self.input_filename = input_filename
        self.output_filename = output_filename

    def translate_words(self, english_words):
        translated_pairs = []
        
        for word in english_words:
            translated_word = self.translator.translate(word).strip()
            translated_pairs.append(f"{word} - {translated_word}")
        
        return translated_pairs

    def translate_and_save(self):
        try:
            with open(self.input_filename, "r", encoding="utf-8") as input_file:
                english_words = input_file.read().splitlines()
            
            translated_pairs = self.translate_words(english_words)
            
            with open(self.output_filename, "w", encoding="utf-8") as output_file:
                output_file.write("\n".join(translated_pairs))
            
            print("Translation completed successfully.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("An error occurred:", e)

def main():
    input_filename = "input.txt"
    output_filename = "output.txt"

    language = input("Enter the target language code (default is 'pl'): ") or "pl"
    cogniTranslateTool = CogniTranslateTool(input_filename, output_filename, language)
    cogniTranslateTool.translate_and_save()

if __name__ == "__main__":
    main()
