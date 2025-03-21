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

        // Get the warning and error elements
        const raceWarning = document.getElementById('single-race-warning');
        const firstRaceError = document.getElementById('first-race-error');
        const firstGenderError = document.getElementById('first-gender-error');
        const lastRaceError = document.getElementById('last-race-error');

        // Clear previous errors
        firstRaceError.style.display = "none";
        firstGenderError.style.display = "none";
        lastRaceError.style.display = "none";

        let hasError = false;

        // Validation Checks
        if (!firstGender) {
            firstGenderError.textContent = "Please select a gender.";
            firstGenderError.style.display = "inline";
            hasError = true;
        }

        if (firstRaces.length === 0) {
            firstRaceError.textContent = "Please select at least one race.";
            firstRaceError.style.display = "inline";
            hasError = true;
        }

        if (lastRaces.length === 0) {
            lastRaceError.textContent = "Please select at least one race.";
            lastRaceError.style.display = "inline";
            hasError = true;
        }

        if (hasError) {
            console.log("Validation Failed: Missing selections.");
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
