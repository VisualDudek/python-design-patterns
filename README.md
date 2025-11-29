# python-design-patterns
Collection of software design patterns implemented in Python.

## Dependency Injection

### Disadvantages of the Initial Implementation
- **Hardcoded functionality**: Processing logic is tightly coupled to specific implementations
- **Hardcoded order of pipeline steps**: The sequence of operations cannot be easily modified or rearranged
- **Hard to test**: Difficult to unit test individual components due to tight coupling and lack of dependency injection

#### Examples of Problems
1. **Changing data source**: If you want to load data from memory instead of CSV, you need to modify the class internals
2. **Changing export destination**: If you want to export to a database instead of CSV, you need to modify the class code
