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


### Step 2
Inject these functions instead of calling them from class -> turn the `run` method into a higher order function/method.

#### Changes from a002_step_01.py to a003_step_02.py
- Added `Callable` import from `typing` module
- Modified `run()` method to accept a `loader_fn` parameter of type `Callable[[], Data]`
- The `run()` method now calls the injected `loader_fn()` instead of hardcoded `load_data_from_csv()`
- In `main()`, the loader function is now passed as an argument: `pipeline.run(load_data_from_csv)`
- This allows different data loading strategies to be injected at runtime without modifying the class

### Step 3
Previous changes were made using functions, but we can also use a class-based approach and inject objects instead of functions.

#### Changes from a003_step_02.py to a004_step_03.py
- Created class-based implementations: `InMemoryLoader`, `JSONExporter`, and `CleanMissingFields`
- Added `__init__()` method to `DataPipeline` that accepts loader, transformer, and exporter objects as parameters
- The `run()` method no longer takes parameters; it uses the injected objects stored in instance variables
- Changed `run()` to call methods on injected objects: `self.loader.load()`, `self.transformer.transform()`, `self.exporter.export()`
- In `main()`, objects are created first and then injected into `DataPipeline` via constructor
- This class-based approach provides better encapsulation and makes it easier to create different implementations with internal state

**Note**: The `DataPipeline` constructor currently depends on specific concrete types (`InMemoryLoader`, `JSONExporter`, `CleanMissingFields`), but this can be addressed using protocols to depend on interfaces instead.