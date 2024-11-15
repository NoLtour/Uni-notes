---
aliases: ["YAML"]
tags: []
---

## YAML file

A YAML file is a text file that uses the YAML (YAML Ain't Markup Language) format, which is designed for easy readability and is commonly used for configuration files and data serialization. YAML files are structured using indentation (similar to Python) to represent nested data, making them straightforward and human-readable.

Key Features of YAML Files:
- Human-Friendly: YAML’s syntax is clean and easy to read, as it uses simple [[key-value pairs]] and indentation to structure data.
- Supports Nested Data: YAML allows hierarchical data structures using indentation, making it ideal for complex configurations.
- Commonly Used for Configurations: YAML is often used to configure applications because it allows setting parameters in a readable way.

A simple YAML file example could be:

```YAML
name: My Application
version: 1.0
settings:
  debug: true
  logging_level: INFO
database:
  host: localhost
  port: 5432
  username: admin
  password: secret
```

To some extent you can think of them as [[JSON file]]s that take the python approach to readability.