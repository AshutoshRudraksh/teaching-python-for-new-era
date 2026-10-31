# Lesson 1 exercises: teacher solutions

For Ashutosh only, to check Vineet's work fast. Expected outputs are exact.

## Exercise 1: Introduce a patient
```python
name = "Meena"
age = 35
print(name, "is", age, "years old")
```
Output: `Meena is 35 years old` (his names and ages may differ, the sentence shape is what matters)

## Exercise 2: A week of visits
```python
visits = [14, 11, 18, 9, 16, 7, 5]
print(sum(visits))
print(len(visits))
```
Output: `80` and `7`

## Exercise 3: Average waiting time
```python
waiting_minutes = [10, 25, 15, 30, 20]
print(sum(waiting_minutes) / len(waiting_minutes))
```
Output: `20.0`

## Exercise 4: The busiest day
```python
for v in visits:
    print("Day count:", v)
```
Output: seven lines, Day count 14, 11, 18, 9, 16, 7, 5

## Exercise 5: Only the long waits
```python
for w in waiting_minutes:
    if w >= 20:
        print(w)
```
Output: `25`, `30`, `20`

## Exercise 6: Read the records
```python
for patient in patients:
    print(patient["name"], patient["condition"])
```
Output: five lines, Ravi Diabetes through Kiran Blood pressure. A comma between the fields is fine either way.

## Exercise 7: Senior patients list
```python
seniors = []
for patient in patients:
    if patient["age"] >= 50:
        seniors.append(patient["name"])
print(seniors)
print(len(seniors))
```
Output: `['Arun', 'Kiran']` and `2`

## Exercise 8: The weekly report line
```python
counts = {}
for patient in patients:
    condition = patient["condition"]
    if condition in counts:
        counts[condition] = counts[condition] + 1
    else:
        counts[condition] = 1
print(counts)
```
Output: `{'Diabetes': 2, 'Checkup': 2, 'Blood pressure': 1}`

## Checking notes
Exercise 8 is the gate. If he can do it alone, Lesson 1 has landed and Lesson 3 can move faster. If he stalls, the stall point tells you the gap: loop, dictionary keys, or the counting pattern itself. Reteach only that piece, in the Lesson 2 warm up slot.
