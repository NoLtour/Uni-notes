---
aliases: [""]
tags: []
---

## JSON file

JSON ([[JavaScript]] Object Notation) is a lightweight, text-based format used for representing structured data. It is easy for humans to read and write and easy for machines to parse and generate. JSON is often used for exchanging data between a server and a web application, or between different systems, in a format that is both language-agnostic and human-readable.

Key features:
- Simple Structure: JSON data is represented as a collection of [[key-value pairs]] (similar to dictionaries in Python or objects in JavaScript). The keys are always strings, and the values can be various data types, such as:
	-   Strings
	-   Numbers
	-   Booleans (true/false)
	-   Arrays (ordered lists)
	-  Objects (nested [[key-value pairs]])
	- Null (empty or undefined values)
- Text Format: JSON files are plain text and are typically saved with the .json file extension.

An example could be:
```JSON
{
  "name": "John Doe",
  "age": 30,
  "isStudent": false,
  "courses": ["Math", "Science", "History"],
  "address": {
    "street": "123 Main St",
    "city": "Anytown"
  }
}
```
