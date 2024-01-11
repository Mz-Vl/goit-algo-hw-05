# На основі виконання кожного з трьох алгоритмів визначено найшвидший алгоритм для кожного з двох текстів.
#
# Зроблено висновки щодо швидкостей алгоритмів для кожного тексту окремо та в цілому.
# Висновки оформлено у вигляді документа формату markdown.

import timeit

from Boyer_Moore_algorithm import *
from Knuth_Morris_Pratt_algorithm import *
from Rabin_Karp_algorithm import *

article_1_path = "articles/article_1.txt"
article_2_path = "articles/article_2.txt"

with open(article_1_path, "r", encoding="utf-8") as file_1, open(article_2_path, "r", encoding="utf-8") as file_2:
    content_1 = file_1.read()
    content_2 = file_2.read()


real_sub_string_a1 = "while (integers[Math.min(jumpStep, arrayLen"
not_real_sub_string_a1 = "що дійсно не існує в тексті,"

real_sub_string_a2 = "B-дерево (b-tree) – це структура даних представлена збалансованим, сильно розгалудженим"
not_real_sub_string_a2 = "також не існує в тексті,"


def run_algorithm(search_function, content, real_substring, not_real_substring):
    time_exist = timeit.timeit(lambda: search_function(content, real_substring), number=5)
    time_not_exist = timeit.timeit(lambda: search_function(content, not_real_substring), number=5)
    return time_exist, time_not_exist


# Rabin-Karp
rabin_karp_search_times_1 = run_algorithm(rabin_karp_search, content_1, real_sub_string_a1, not_real_sub_string_a1)
rabin_karp_search_times_2 = run_algorithm(rabin_karp_search, content_2, real_sub_string_a2, not_real_sub_string_a2)

print(f"Rabin Karp search times (article 1): {rabin_karp_search_times_1}")
print(f"Rabin Karp search times (article 2): {rabin_karp_search_times_2}")

# Knuth Morris
kmp_search_times_1 = run_algorithm(kmp_search, content_1, real_sub_string_a1, not_real_sub_string_a1)
kmp_search_times_2 = run_algorithm(kmp_search, content_2, real_sub_string_a2, not_real_sub_string_a2)

print(f"\nKnuth Morris search times (article 1): {kmp_search_times_1}")
print(f"Knuth Morris search times (article 2): {kmp_search_times_2}")

# Boyer-Moore
boyer_moore_search_times_1 = run_algorithm(boyer_moore_search, content_1, real_sub_string_a1, not_real_sub_string_a1)
boyer_moore_search_times_2 = run_algorithm(boyer_moore_search, content_2, real_sub_string_a2, not_real_sub_string_a2)

print(f"\nBoyer-Moore search times (article 1): {boyer_moore_search_times_1}")
print(f"Boyer-Moore search times (article 2): {boyer_moore_search_times_2}")
