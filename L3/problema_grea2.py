"""un program incearca sa ghiceasca captcha-uri text in imagini cu zgomot
in urma unor filtrari, s-au obtinut 20 de fisiere JSON cate 1 per captcha, in folderul "date_captcha"
datele din fiecare JSON sunt organizate astfel:
{"char1": [[X_offset, char_X_size, pixel_distance], [...], [...], [...], [...]], "char2", ......}
deoarece un captcha are fix 5 caractere si oricare litera 'A'-'Z' poate apare de mai multe ori, pentru fiecare caracter s-au obtinut 5 posibile solutii de pozitionare.
Exemplu concret: 'A': [[25, 50, 6776], [24, 50, 6798], [26, 50, 6802], [27, 50, 6880], [23, 50, 6902]]
Noi trebuie sa extragem secventa de caractere care reprezinta un captcha ghicit, filtrand aceste date, dupa cum urmeaza:
- nu avem voie ca la o pozitie pe X determinata de primul numar din perechea de 3, sa am mai multe caractere in range-ul caracter anterior +- 30
- prima pozitie posibile care o vom selecta este cea cu distanta cea mai mica (data de al 3-lea numar)
- ulterior celelalte pozitii pica sau raman in functie de distanta fata de pozitiile selectate anterior"""

import json
import glob
import os

def process_captcha(json_file):
    with open(json_file, 'r') as f:
        data=json.load(f)

    all_positions=[]

    for char, positions in data.items():
        for pos in positions:
            x_offset, _, distance=pos
            all_positions.append((char, x_offset, distance))

    all_positions.sort(key=lambda x: x[2])

    selected=[]

    for char, x_offset, distance in all_positions:
        conflict=False
        for char_selected, x_selected, dist_selected in selected:
            if abs(x_offset-x_selected)<30:
                conflict=True
                break
        if not conflict:
            selected.append((char, x_offset, distance))

    selected.sort(key=lambda x: x[1])

    captcha=''.join(char for char, _, _ in selected)

    return captcha

json_files=[os.path.join("date_captcha", fn) for fn in os.listdir("date_captcha")]

results=[]
for file in json_files:
    captcha=process_captcha(file)
    results.append(captcha)

for result in results:
    print(result)