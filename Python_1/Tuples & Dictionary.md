# Python Data Structures: Dictionaries and Tuples

## 1. Introduction

Python provides several built-in data structures to store and organize data. Two useful examples are **Dictionaries** and **Tuples**.

- **Dictionary:** Stores data in key-value pairs.
- **Tuple:** Stores multiple values in an ordered collection that cannot be modified after creation.

Both structures are useful in different situations depending on how the data needs to be stored and accessed.

---

# 2. Python Dictionary

## 2.1 What is a Dictionary?

A dictionary is a built-in Python data structure that stores information in the form of **key-value pairs**.

Each key is used to access its corresponding value. Dictionaries are mutable, meaning their contents can be added, modified, or removed after creation.

### Syntax

```python
dictionary_name = {
    "key1": "value1",
    "key2": "value2"
}
```

### Example

```python
student = {
    "name": "Arjun",
    "age": 21,
    "course": "BCA",
    "university": "Adamas University"
}

print(student)
```

**Output:**

```text
{'name': 'Arjun', 'age': 21, 'course': 'BCA', 'university': 'Adamas University'}
```

## 2.2 Characteristics of Dictionaries

1. Store data in key-value pairs.
2. Mutable: values can be added, updated, or deleted.
3. Keys must be unique.
4. Keys must be hashable, such as strings, numbers, or tuples containing hashable values.
5. Values can be of different data types.
6. Dictionaries preserve insertion order in modern Python.

## 2.3 Accessing Dictionary Elements

Values can be accessed using their corresponding keys.

```python
student = {
    "name": "Arjun",
    "age": 21,
    "course": "BCA"
}

print(student["name"])
print(student["age"])
```

**Output:**

```text
Arjun
21
```

Another method is `get()`.

```python
print(student.get("course"))
print(student.get("marks", "Not Available"))
```

`get()` returns `None` by default when a key is missing, or a default value if one is provided. Unlike square-bracket access, it does not raise a `KeyError` for a missing key.

## 2.4 Adding and Updating Elements

A new key-value pair can be added by assigning a value to a new key.

```python
student["marks"] = 85
student["age"] = 22

print(student)
```

Here:
- `"marks"` is added to the dictionary.
- `"age"` is updated from 21 to 22.

## 2.5 Removing Elements

Python provides several methods to remove dictionary elements.

### Using `pop()`

```python
student.pop("age")
```

Removes the specified key and returns its value.

### Using `del`

```python
del student["course"]
```

Deletes the specified key-value pair.

### Using `clear()`

```python
student.clear()
```

Removes all elements from the dictionary.

## 2.6 Important Dictionary Methods

| Method | Description |
|---|---|
| `keys()` | Returns all dictionary keys |
| `values()` | Returns all dictionary values |
| `items()` | Returns key-value pairs |
| `get()` | Retrieves a value safely |
| `update()` | Adds or updates multiple entries |
| `pop()` | Removes a specified key |
| `popitem()` | Removes the last inserted key-value pair |
| `clear()` | Removes all entries |
| `copy()` | Creates a shallow copy |

### Example: Iterating Through a Dictionary

```python
student = {
    "name": "Arjun",
    "age": 21,
    "course": "BCA"
}

for key, value in student.items():
    print(key, ":", value)
```

**Output:**

```text
name : Arjun
age : 21
course : BCA
```

## 2.7 When Should We Use Dictionaries?

Dictionaries are useful when:
- Data needs to be stored with meaningful labels.
- Fast lookup using keys is required.
- Information needs to be updated frequently.
- We need to represent structured records.

**Real-world example:** A student database can store a student's name, roll number, department, and marks using key-value pairs.

---

# 3. Python Tuple

## 3.1 What is a Tuple?

A tuple is a built-in Python data structure used to store multiple values in a single variable.

Tuples are **ordered and immutable**, meaning their elements maintain their positions and cannot be changed after the tuple is created.

### Syntax

```python
tuple_name = (value1, value2, value3)
```

### Example

```python
student = ("Arjun", 21, "BCA", 85)

print(student)
```

**Output:**

```text
('Arjun', 21, 'BCA', 85)
```

## 3.2 Characteristics of Tuples

1. Ordered collection of elements.
2. Immutable: elements cannot be modified after creation.
3. Allows duplicate values.
4. Can store different data types.
5. Supports indexing and slicing.
6. Can contain other collections, including lists and dictionaries.

## 3.3 Accessing Tuple Elements

Tuple elements can be accessed using indexing.

```python
student = ("Arjun", 21, "BCA", 85)

print(student[0])
print(student[2])
```

**Output:**

```text
Arjun
BCA
```

Python uses zero-based indexing, meaning the first element has index 0.

Negative indexing can also be used.

```python
print(student[-1])
```

**Output:**

```text
85
```

## 3.4 Tuple Slicing

Slicing allows us to retrieve a portion of a tuple.

```python
numbers = (10, 20, 30, 40, 50, 60)

print(numbers[1:4])
```

**Output:**

```text
(20, 30, 40)
```

The starting index is included, but the ending index is excluded.

## 3.5 Immutability of Tuples

Once a tuple is created, its elements cannot be changed.

```python
numbers = (10, 20, 30)

numbers[1] = 50
```

**Output:**

```text
TypeError: 'tuple' object does not support item assignment
```

If we need to modify tuple data, we can convert it into a list, make the changes, and convert it back.

```python
numbers = (10, 20, 30)

temp = list(numbers)
temp[1] = 50

numbers = tuple(temp)

print(numbers)
```

**Output:**

```text
(10, 50, 30)
```

Note: Although a tuple cannot be structurally modified, a mutable object stored inside it, such as a list, can still be modified.

## 3.6 Single-Element Tuple

A single-element tuple requires a trailing comma.

```python
a = (10,)
b = (10)

print(type(a))
print(type(b))
```

**Output:**

```text
<class 'tuple'>
<class 'int'>
```

Without the comma, Python treats `(10)` as an ordinary integer expression.

## 3.7 Important Tuple Methods

Tuples have fewer built-in methods because they are immutable.

| Method | Description |
|---|---|
| `count()` | Counts occurrences of an element |
| `index()` | Returns the index of the first occurrence |

### Example

```python
numbers = (10, 20, 30, 20, 40, 20)

print(numbers.count(20))
print(numbers.index(30))
```

**Output:**

```text
3
2
```

## 3.8 Tuple Packing and Unpacking

### Packing

Assigning multiple values to a tuple is called tuple packing.

```python
student = ("Arjun", 21, "BCA")
```

### Unpacking

Assigning tuple elements to separate variables is called tuple unpacking.

```python
name, age, course = student

print(name)
print(age)
print(course)
```

**Output:**

```text
Arjun
21
BCA
```

The number of variables must normally match the number of tuple elements, unless extended unpacking is used.

## 3.9 When Should We Use Tuples?

Tuples are useful when:
- Data should remain unchanged.
- We need to store fixed collections of values.
- We want to return multiple values from a function.
- We need an immutable sequence that can potentially be used as a dictionary key.

**Real-world example:** Geographic coordinates can be represented as a tuple:

```python
location = (22.5726, 88.3639)
```

The tuple represents latitude and longitude.

---

# 4. Difference Between Dictionary and Tuple

| Feature | Dictionary | Tuple |
|---|---|---|
| Structure | Key-value pairs | Ordered sequence |
| Syntax | `{key: value}` | `(value1, value2)` |
| Mutable | Yes | No |
| Access | Using keys | Using indexes |
| Duplicate values | Allowed | Allowed |
| Duplicate keys | Not allowed | Not applicable |
| Ordering | Preserves insertion order | Ordered |
| Common use | Structured and labelled data | Fixed collections of values |

---

# 5. Practical Examples

## Example 1: Student Marks Using Dictionary

```python
student_marks = {
    "English": 85,
    "Mathematics": 90,
    "Computer Science": 95
}

total = sum(student_marks.values())
average = total / len(student_marks)

print("Total Marks:", total)
print("Average Marks:", average)
```

**Output:**

```text
Total Marks: 270
Average Marks: 90.0
```

## Example 2: Storing and Unpacking Coordinates Using Tuple

```python
coordinates = (22.5726, 88.3639)

latitude, longitude = coordinates

print("Latitude:", latitude)
print("Longitude:", longitude)
```

**Output:**

```text
Latitude: 22.5726
Longitude: 88.3639
```

---

# 6. Practice Questions

### Dictionary Practice

1. Create a dictionary containing your name, age, course, and university.
2. Add a new key called `semester` and assign its value.
3. Update the age stored in the dictionary.
4. Print all keys and values using a loop.
5. Create a dictionary of five subjects and their marks. Calculate the total and average marks.

### Tuple Practice

1. Create a tuple containing five integer values.
2. Print the first and last elements.
3. Count how many times a particular number occurs.
4. Find the index of a given element.
5. Unpack a tuple into separate variables.
6. Convert a tuple into a list, modify one element, and convert it back.

---

# 7. Conclusion

Dictionaries and tuples are important Python data structures, but they solve different problems.

- Dictionaries are useful for storing labelled information that may need to change.
- Tuples are useful for storing ordered collections of values that should remain unchanged.

Understanding these structures helps build a strong foundation for more advanced Python concepts, including functions, object-oriented programming, data processing, and algorithm development.

**Key takeaway:** Choose a dictionary when you need key-based access and mutability. Choose a tuple when you need an ordered, immutable collection.
