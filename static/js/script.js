document.addEventListener("DOMContentLoaded", function () {
    // Array to store generated names (Limited to only the last 15)
    let generatedNames = [];

    // Event listener for the "Generate Name" button
    document.getElementById('generate-button').addEventListener('click', function () {
        console.log("Button clicked!"); // Logs every time the button is clicked

        // Get selected races for the first name
        const firstRaces = Array.from(document.querySelectorAll('input[name="first-race"]:checked')).map(el => el.value);
        // Get selected gender for the first name
        const firstGenderInput = document.querySelector('input[name="first-gender"]:checked');
        const firstGender = firstGenderInput ? firstGenderInput.value : '';
        // Get selected races for the last name
        const lastRaces = Array.from(document.querySelectorAll('input[name="last-race"]:checked')).map(el => el.value);

        // Get the warning element
        const raceWarning = document.getElementById('single-race-warning');

        // Validation Checks
        if (firstRaces.length === 0 && !firstGender && lastRaces.length === 0) {
            document.getElementById('name-display').textContent = "Please configure your options before generating a name.";
            console.log("Validation Failed: No selections made.");
            return;
        }

        if (!firstGender) {
            document.getElementById('name-display').textContent = "Please select a gender.";
            console.log("Validation Failed: No gender selected.");
            return;
        }

        // Show or hide warnings based on selections
        if ((firstRaces.length === 1 && lastRaces.length === 0) || (lastRaces.length === 1 && firstRaces.length === 0)) {
            raceWarning.textContent = "One race selected, using for both first and last name.";
            raceWarning.style.display = "block";
        } else {
            raceWarning.style.display = "none";
        }

        // Fetch request to generate name
        console.log("Validation Passed: Sending request...");
        fetch('/generate_name', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                firstRaces: firstRaces,
                firstGender: firstGender,
                lastRaces: lastRaces
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.firstName && data.lastName) {
                const fullName = `${data.firstName} ${data.lastName}`;

                // Add the new name to the list (limit it to 15 names)
                generatedNames.unshift(fullName);
                if (generatedNames.length > 15) {
                    generatedNames.pop();
                }

                // Update the display with the new name and the full list
                document.getElementById('name-display').textContent = fullName;
                updateGeneratedNamesDisplay();
            } else {
                document.getElementById('name-display').textContent = data.error || "An error occurred.";
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('name-display').textContent = 'An error occurred.';
        });
    });

    // Function to update the previously generated names display
    function updateGeneratedNamesDisplay() {
        const displayContainer = document.getElementById('generated-names-display');
        displayContainer.innerHTML = ""; // Clear previous list

        // Add all generated names to the display
        generatedNames.forEach(name => {
            const nameElement = document.createElement("div");
            nameElement.textContent = name;
            displayContainer.appendChild(nameElement);
        });
    }
});
