import matplotlib.pyplot as plt
import numpy as np


np.random.seed(19680801)
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set_xlabel('entry a')
ax.set_ylabel('entry b')
plt.show()

with open('run_results_albums.json', encoding='utf-8') as file_parsing:    text_parsing = json.load(file_parsing)
with open('parsing.txt', 'w') as parsing_file:
    text_for_file = '; '.join([f'{key.capitalize()}: {value}' for key, value in text_parsing.items()])
    parsing_file.write(text_for_file)
    print(len(text_for_file))
