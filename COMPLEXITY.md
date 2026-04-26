🚀 DSA LAB FINAL SUMMARY (FORMULAS + RULES)
1️⃣ Big-O Meaning

Big-O describes how runtime grows when input size increases. 

NOTES

n = input size (array length / number of nodes / elements).

Example
If input doubles → runtime change shows complexity.

2️⃣ Most Important Time Complexities
Complexity	Meaning	Example
O(1)	Constant	Array access
O(log n)	Logarithmic	Binary Search
O(n)	Linear	Linear Search
O(n log n)	Efficient sorting	Merge Sort
O(n²)	Quadratic	Bubble Sort
O(2ⁿ)	Exponential	Fibonacci recursion

Order (Fast → Slow)

O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)

TIME_COMPLEXITY

3️⃣ Main Rules to Calculate Big-O
Single Loop
for i in range(n)

➡ O(n)

Two Separate Loops
for i in range(n)
for j in range(n)
O(n) + O(n) = O(2n) = O(n)
Nested Loops
for i in range(n)
    for j in range(n)
O(n × n) = O(n²)
Three Nested Loops
O(n³)
Halving Input
n = n // 2
O(log n)

(Binary search)

n work repeated log n times
O(n log n)
4️⃣ Simplification Rules (VERY IMPORTANT)

Ignore constants

O(2n) → O(n)

Ignore smaller terms

O(n² + n) → O(n²)

Examples

O(3n + 10) → O(n)
O(n² + 100n + 5) → O(n²)

TIME_COMPLEXITY

5️⃣ Big-O Calculation Steps
Step 1

Identify n

Example

n = len(arr)
Step 2

Count loop repetitions.

Step 3

Sequential code → ADD

O(n) + O(n)
Step 4

Nested code → MULTIPLY

O(n × n)
Step 5

Drop constants and smaller terms.

6️⃣ Binary Search Important Formula
mid = (low + high) // 2

Search reduces

n → n/2 → n/4 → n/8

Time complexity

O(log n)

NOTES

7️⃣ Bubble Sort Important Formula

Number of passes

n - 1

Total comparisons

n(n - 1) / 2

Worst case complexity

O(n²)
8️⃣ Linear Search

Checks every element.

Worst comparisons

n

Time complexity

O(n)
9️⃣ Array Operation Complexities
Operation	Complexity
Access	O(1)
Search	O(n)
Insert	O(n)
Delete	O(n)
🔟 Quick Mental Tricks

If input becomes 10× bigger

Runtime change	Complexity
10× slower	O(n)
100× slower	O(n²)
Almost same	O(log n)
🧠 6 Things to Always Remember in Exam

1️⃣ Single loop → O(n)
2️⃣ Nested loops → O(n²)
3️⃣ Halving problem → O(log n)
4️⃣ Sequential code → ADD
5️⃣ Nested code → MULTIPLY
6️⃣ Keep only largest term

⭐ Ultimate 1-Line Formula
Sequential → ADD
Nested → MULTIPLY
Keep largest term