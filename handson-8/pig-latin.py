def pig_latin(word):
    vowels = "aeiouAEIOU"
    punctuation = "! ,;:-.?'"  
    word = word.lower().strip(punctuation)  
    if word[0] in vowels:
        return word + "way"
    else:
        first_vowel_index = next((i for i, letter in enumerate(word) if letter in vowels), None)
        if first_vowel_index is not None:
            return word[first_vowel_index:] + word[:first_vowel_index] + "ay"
        else:
            return word + "ay"  
        
def translate_to_pig_latin(sentence):
    words = sentence.split()
    translated_sentence = " ".join(pig_latin(word) for word in words)
    return translated_sentence

def main():
    print("Pig Latin Translator")
    while True:
        text = input("Enter text: ")
        print("English:\t" + text)
        print("Pig Latin:\t" + translate_to_pig_latin(text))
        continue_choice = input("Continue? (y/n): ")
        if continue_choice.lower() != 'y':
            print("Bye!")
            break

if __name__ == "__main__":
    main()
