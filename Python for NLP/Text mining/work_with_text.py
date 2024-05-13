import json


with open('run_results_albums.json', encoding='utf-8') as file_parsing:
    text_parsing = json.load(file_parsing)

with open('parsing.txt', 'w') as parsing_file:
    text_for_file = '; '.join([f'{key.capitalize()}: {value}' for key, value in text_parsing.items()])
    parsing_file.write(text_for_file)
    print(len(text_for_file))