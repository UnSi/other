import re

"""
\d - any digit  0-9
\D - any non-digit 
\w - any alphabet symbol (characters from a to Z, digits from 0-9, and the underscore _ character)
\W - any non alphabet symbol
\s - breakspace(white space, обычный пробел)
\S - non breackspace

[0-9] - аналогично \d
[A-Z][a-z]+ - первая большая, остальные маленькие. + - сколько угодно последнего символа.
"""

my_text = "vasya aaaa 1972, Kolya - 1972: Olesya 1981, aaaaa@intel.com," \
         "bbbbbbbbbbbbb@intel.com, Petya gggg, 1992, cccccc@yahoo.com" \
         "ddddddddddd@intel.com, vasya@yandex.net, hello hello, Misha#43 1984, " \
         "Vladimir 1977, Irina, 2001, annnnn@intel.net, yeeeee@yandex.com," \
         "oooooooooooooo@hotmail.gov, ggggggggggggggg@gov.gov, tutututut@giv.hot, " \
         "Вфы-в3ф.ы@фыв.ыв.sd-f, Вфы-в3ф.ы@фывsada"

text_look_for = r"yandex"
text_look_for = r"\d\d\d\d"
text_look_for = r"[0-9]{4}"
text_look_for = r"\w+"
text_look_for = r"[A-Z][a-z]+"
text_look_for = r"[\w\.-]+@(?!intel\.com)[\w-]+\.[\w\.-]+"
all_results = re.findall(text_look_for, my_text)
print(all_results)