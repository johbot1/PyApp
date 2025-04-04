# Checkpoints
## 1. Data Gathering & Setup: ✅ 
#### 1.1 Development: ✅
- [✅] 1.1.2 Create JSON files (or CSV/SQLite) for at least 3 common D&D races (e.g., Human, Elf, Dwarf), with male and female name lists. 
- [✅] 1.1.3 Set up a basic Flask or FastAPI project.
- [✅] 1.1.4 Create a simple HTML template with checkboxes for race selection and radio buttons for gender selection.  
#### 1.2 Testing: ✅
- [✅] 1.2.1 Verify that the JSON files are correctly formatted and accessible by Python code. 
- [✅] 1.2.2 Ensure the basic HTML form elements are displaying correctly in a browser.


## 2. Core Name Generation Logic:  ✅ 
#### 2.1 Development: ✅
- [✅] 2.1.1 Implement a Python function that reads the selected race(s) and gender from the HTML form.
- [✅] 2.1.2 Create a function that randomly selects a name from the appropriate JSON data.
- [✅] 2.1.3 Integrate the name generation function with the Flask/FastAPI route that handles the "Generate" button click.
#### 2.2 Testing: ✅
- [✅] 2.2.1 Test the name generation function with different race and gender selections.
- [✅] 2.2.2 Verify that the generated names are being displayed on the web page.
- [✅] 2.2.3 Test that if multiple races are selected, that a name from one of the selected races is always generated.


## 3. User Interface Enhancements & Refinement: ✅
#### 3.1 Development: ✅
- [✅] 3.1.1 Improve the HTML/CSS of the web page for a more visually appealing and user-friendly interface.
- [✅] 3.1.2 Add error handling (e.g., display a message if no races are selected).
#### 3.2 Testing: ✅
- [✅] 3.2.1 Test the app on different browsers and screen sizes.
- [✅] 3.2.2 Verify that the error handling works as expected.

    

## 4.Feedback:
- [✅] Error handling more specific
- [✅] Error location is by the option throwing the error
- [✅] Don't add name into Previous Name UNTIL new name generated
- [✅] Naming is more consistent and formatted for JSON
- [✅] Remove debugging statements in Javascript
- [✅] Break Javascript into a separate file
- [✅] Clean up JS

### Workflow:
    User selects race(s) and gender.
    User clicks "Generate."
    The app retrieves the corresponding name lists from the data source.
    The app randomly selects a name from the appropriate list(s).
    The generated name is displayed.

