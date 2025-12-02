# Порівняльний аналіз алгоритмів сортування

## Алгоритми

1. **Built-in sorted()** (Timsort)
2. **sort()** (Timsort)
3. **Insertion Sort**
4. **Merge Sort**

## Результати

### Час виконання

Час виконання алгоритмів було виміряно за допомогою модуля `timeit` на різних наборах даних. Результати підтвердили, що:

- **Timsort** (вбудовані `sorted()` та `sort()`) є найефективнішими для більшості випадків.
- **Merge Sort** демонструє стабільну продуктивність, але поступається Timsort через додаткові витрати пам'яті.
- **Insertion Sort** є найменш ефективним для великих наборів даних, але працює добре для малих масивів.

### Набори даних

1. **small_random**: Маленький масив випадкових чисел.
2. **large_random**: Великий масив випадкових чисел.
3. **sorted**: Відсортований масив.
4. **reversed**: Масив відсортований в зворотньому порядку.
5. **duplicates**: Масив дублікатів.

### Результати тестування

#### small_random

- Built-in sorted: 0.000108 seconds
- Built-in sort(): 0.000145 seconds
- Insertion sort: 0.001241 seconds
- Merge sort: 0.003128 seconds

#### large_random

- Built-in sorted: 0.025011 seconds
- Built-in sort(): 0.024537 seconds
- Insertion sort: 9.384385 seconds
- Merge sort: 0.716558 seconds

#### sorted

- Built-in sorted: 0.000322 seconds
- Built-in sort(): 0.000345 seconds
- Insertion sort: 0.003969 seconds
- Merge sort: 0.037696 seconds

#### reversed

- Built-in sorted: 0.000341 seconds
- Built-in sort(): 0.000355 seconds
- Insertion sort: 0.167463 seconds
- Merge sort: 0.040837 seconds

#### duplicates

- Built-in sorted: 0.001523 seconds
- Built-in sort(): 0.001504 seconds
- Insertion sort: 0.059314 seconds
- Merge sort: 0.050075 seconds

## Часова складність

- **Timsort**: $O(n \log n)$ в середньому та найгіршому випадках.
- **Merge Sort**: $O(n \log n)$ в середньому та найгіршому випадках.
- **Insertion Sort**: $O(n^2)$ в середньому та найгіршому випадках.

## Висновки

1. **Built-in sorted() і sort()**:
   - Найшвидші алгоритми для всіх наборів тестових даних.
   - Ефективно обробляє як випадкові, так і частково відсортовані масиви.

2. **Insertion sort**:
   - Добре працює на маленьких масивах.
   - Дуже повільний на великих масивах.

3. **Merge sort**:
   - Стабільний алгоритм із продуктивністю $O(n \log n)$.
   - Повільніший за вбудовані через додаткові витрати пам'яті.

4. **Порівняння Merge sort і Insertion sort**:
   - **Insertion sort** значно повільніший на великих наборах даних через квадратичну складність $O(n^2)$.
   - **Merge sort** демонструє кращу продуктивність на великих наборах даних, але поступається Timsort.

