class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower()
                    line = ''.join(e for e in line if e.isalnum() or e.isspace())
                    words.extend(line.split())
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in [w.lower() for w in words]:
                result[name] = words.index(word.lower()) + 1
        return result

    def count(self, word):
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word.lower())
        return result

finder = WordsFinder('test_file.txt')
print(finder.get_all_words())  # All words
print(finder.find('TEXT'))  # Position of 'TEXT'
print(finder.count('teXT'))  # Count of 'teXT'