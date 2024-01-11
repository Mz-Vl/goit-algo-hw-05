# Summary of Algorithm Search Speed

## Results for Article 1

### Rabin-Karp
- Time for the existing substring: 0.0295 sec
- Time for the non-existing substring: 0.0568 sec

### Knuth-Morris
- Time for the existing substring: 0.0083 sec
- Time for the non-existing substring: 0.0221 sec

### Boyer-Moore
- Time for the existing substring: 0.0013 sec
- Time for the non-existing substring: 0.0051 sec

## Results for Article 2

### Rabin-Karp
- Time for the existing substring: 0.0398 sec
- Time for the non-existing substring: 0.0892 sec

### Knuth-Morris
- Time for the existing substring: 0.0162 sec
- Time for the non-existing substring: 0.0425 sec

### Boyer-Moore
- Time for the existing substring: 0.0023 sec
- Time for the non-existing substring: 0.0078 sec

## General Conclusions

1. **Boyer-Moore** demonstrated the best performance for both articles in all cases. It proved to be the fastest algorithm among the compared ones.

2. **Knuth-Morris** also showed good results, especially for Article 1, where it outperformed Rabin-Karp.

3. **Rabin-Karp** was less efficient compared to other algorithms for these specific texts.

4. The speed of algorithms depends on the specific content and substrings, and they may behave differently for different input data.

5. Consider the requirements of the specific task and data characteristics when choosing a substring search algorithm.
