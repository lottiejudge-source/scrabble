import unittest

class ScrabbleConvertorTest(unittest.TestCase):
    def test_result_of_one_letter(self):
        self.assertEqual(letter_to_point_convertor('A'), 1)
        self.assertEqual(letter_to_point_convertor('B'), 3)
        self.assertEqual(letter_to_point_convertor('Z'), 10)

    def test_result_of_multiple_letters(self):
        self.assertEqual(letter_to_point_convertor('AA'), 2)      
        self.assertEqual(letter_to_point_convertor('BB'), 6)
        self.assertEqual(letter_to_point_convertor('Hazmat'), 20)
    
    def test_result_of_double_letter_square(self):
        self.assertEqual(letter_to_point_convertor('De*sk'), 10)
        self.assertEqual(letter_to_point_convertor('Z*ebra'), 26)

    def test_result_of_triple_letter_square(self):
        self.assertEqual(letter_to_point_convertor('De**sk'), 11)
        self.assertEqual(letter_to_point_convertor('Z**ebra'), 36)

    def test_result_of_double_word_square(self):
        self.assertEqual(letter_to_point_convertor('Hall', ))


def letter_to_point_convertor(word):
    scrabble_points_dictionary = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 4, 'O': 1, 
        'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4, 'W': 4,
        'X': 8, 'Y': 4, 'Z': 10
    }
    word = word.upper()
    result = 0
    
    for i, letter in enumerate(word):
        if letter == '*' and word[i+1] != '*':
            replacement_letter = word[i-1]
            word = word.replace('*', replacement_letter )
        elif letter =='*' and word[i+1] == '*':
            replacement_letter = word[i-1]
            word = word.replace('*', replacement_letter  )
            print(word)


    for letter in word:
        result += scrabble_points_dictionary[letter]
        
    

    
    return result


if __name__ == '__main__':
    unittest.main()



# Double letter (doubles the value of the letter)
# A double letter will be represented with an asterisk after the letter. he*llo would make a double letter on the e.
# Triple letter (triples the value of the letter)
# A triple letter will be represented with two asterisks after the letter. he**llo would make a triple letter on the e.
# Double word (double the value of the word after letter rules have been applied)
# A double word is represented by the word ending in (d)
# Triple word (triple the value of the word after letter rules have been applied)
# A triple word is represented by the word ending in (t)
# A blank (the letter given will score 0)
# A blank tile will be represented with a caret after the letter or asterisk is the letter has a double or triple letter value. he^llo would mean the e scores 0.
# Bonus 50!
# If the word is a seven letter word an additional 50 points are awarded.