# python-design-patterns
Collection of software design patterns implemented in Python.

## Dependency Injection
Instead of creating all dependencies inside a class you pass them in from th outside.

### Disadvantages of the Initial Implementation
- **Hardcoded functionality**: Processing logic is tightly coupled to specific implementations
- **Hardcoded order of pipeline steps**: The sequence of operations cannot be easily modified or rearranged
- **Hard to test**: Difficult to unit test individual components due to tight coupling and lack of dependency injection

#### Examples of Problems
1. **Changing data source**: If you want to load data from memory instead of CSV, you need to modify the class internals
2. **Changing export destination**: If you want to export to a database instead of CSV, you need to modify the class code

### Step 1
First, refactor class methods as outside functions to decouple the logic from the class.
Next, decouple data transformation into fn.

#### Changes from a001_start_here.py to a002_step_01.py
- Extracted `_load_data_from_csv()` method into a standalone `load_data_from_csv()` function
- Extracted `_export_to_json()` method into a standalone `export_to_json()` function
- Extracted inline data transformation logic into a standalone `clean_data()` function
- The `DataPipeline.run()` method now calls these external functions instead of using internal methods
- Logic is now decoupled from the class, making it easier to reuse and test independently
