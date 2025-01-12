import random
""" Задача "Функциональное разнообразие" """

# first = 'Мама мыла раму'
# second = 'Рамена мало было'
# result_1 = list(map(lambda x,y: x == y , first, second))
# print(result_1)


"""Замыкание"""
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for item in data_set:
                f.write(str(item) + '\n')
        return data_set
    return write_everything


# class MysticBall:    
#     def __init__(self, words):        
#         self.words = words

#     def __call__(self):       
#         return random.choice(self.words)
    
write = get_advanced_writer('example.txt')
print(write)
