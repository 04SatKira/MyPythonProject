import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                    words = []
                    for line in file:
                        line = line.lower()
                        translator = str.maketrans('', '', string.punctuation)
                        line = line.translate(translator)
                        words.extend(line.split())
                    all_words[file_name] = words
        return all_words

    def find(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower() #Для корректного поиска вне зависимости от регистра
        for file_name, words in all_words.items():
            index = words.index(word)
            result[file_name] = index
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        word = word.lower() #Для корректного поиска вне зависимости от регистра
        for file_name, words in all_words.items():
            count = words.count(word)
            result[file_name] = count
        return result

#Пример использования (убедитесь, что файл test_file.txt существует)
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('text'))
print(finder2.count('text'))