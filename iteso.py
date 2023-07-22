def number_to_word(num):
    vernacular_numbers = {
        1: 'idiope', 2: 'iyarei', 3: 'iuni', 4: 'ioŋon', 5: 'ikany',
        6: 'ikany-kape', 7: 'ikany-kaare', 8: 'ikanykauni', 9: 'eikanykaoŋon', 10: 'itomon',
        11: 'itomon-kanu-diope', 12: 'itomon\'aare', 13: 'itomon\'auni ', 14: 'itomon\'aaŋon', 15: 'itomon\'akany ',
        16: 'itomon akany\'kape ', 17: 'itomon akany\'kaare', 18: 'itomon akanyauni', 19: 'itomon akany aoŋon', 20: 'akais aare',
        30: 'akais auni', 40: 'akais aangon', 50: 'akais akany'
    }
    
    if num in vernacular_numbers:
        return vernacular_numbers[num]
    
    if 21 <= num <= 50 and num % 10 != 0:
        tens_digit = num // 10 * 10
        ones_digit = num % 10
        return f"{vernacular_numbers[tens_digit]}-{vernacular_numbers[ones_digit]}"
    
    return "Number out of range (1-50)"

def word_to_number(word):
    vernacular_numbers = {
        'idiope': 1, 'iyarei': 2, 'iuni': 3, 'ioŋon': 4, 'ikany': 5,
        'ikany-kape': 6, 'ikany-kaare': 7, 'ikanykauni': 8, 'eikanykaoŋon': 9, 'itomon': 10,
        'itomon-kanu-diope': 11, 'itomon\'aare': 12, 'itomon\'auni': 13, 'itomon\'aaŋon': 14, 'itomon\'akany ': 15,
        'itomon akany\'kape ': 16, 'itomon akany\'kaare': 17, 'itomon akanyauni': 18, 'itomon akany aoŋon': 19, 'akais aare': 20,
        'akais auni': 30, 'akais aangon': 40, 'akais akany': 50
    }
    
    # Handling the case where the word contains a hyphen
    if '-' in word:
        tens_word, ones_word = word.split('-')
        return vernacular_numbers[tens_word] + vernacular_numbers[ones_word]
    
    return vernacular_numbers.get(word.lower(), "Invalid word")

# Testing the functions
while True:
    user_input = input("Enter a number (1-50) or a word: ")
    
    if user_input.isdigit():
        num = int(user_input)
        print(number_to_word(num))
    else:
        print(word_to_number(user_input))
