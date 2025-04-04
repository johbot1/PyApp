document.addEventListener("DOMContentLoaded", function () {
    // Array to store generated names (Limited to only the last 15)
    let generatedNames = [];
    let currentName = ""; // Stores the most recently generated name to prevent premature additions

    // Get important UI elements
    const generateButton = document.getElementById('generate-button');
    const raceWarning = document.getElementById('single-race-warning');
    const firstRaceError = document.getElementById('first-race-error');
    const firstGenderError = document.getElementById('first-gender-error');
    const lastRaceError = document.getElementById('last-race-error');
    const nameDisplay = document.getElementById('name-display');
    const displayContainer = document.getElementById('generated-names-display');

    // Ensure essential elements exist before adding event listeners
    if (!generateButton || !raceWarning || !firstRaceError || !firstGenderError || !lastRaceError || !nameDisplay || !displayContainer) {
        return; // Stop execution if required elements are missing
    }

    // Event listener for the "Generate Name" button
    generateButton.addEventListener('click', function () {

        // Get selected races for the first name
        const firstRaces = Array.from(document.querySelectorAll('input[name="first-race"]:checked')).map(el => el.value);
        // Get selected gender for the first name
        const firstGenderInput = document.querySelector('input[name="first-gender"]:checked');
        const firstGender = firstGenderInput ? firstGenderInput.value : '';
        // Get selected races for the last name
        const lastRaces = Array.from(document.querySelectorAll('input[name="last-race"]:checked')).map(el => el.value);

        // Clear previous errors
        firstRaceError.style.display = "none";
        firstGenderError.style.display = "none";
        lastRaceError.style.display = "none";
        raceWarning.style.display = "none";

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
            return;
        }


        // Fetch request to generate name
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
        .then(response => { // If the app cannot generate a name, it will error here out here ....
            if (!response.ok) throw new Error("Failed to generate name.");
            return response.json();
        })
        .then(data => {
            if (data.firstName && data.lastName) {
                const fullName = `${data.firstName} ${data.lastName}`;

                // Only add the previously generated name to the history if a new one is generated
                if (currentName) {
                    generatedNames.unshift(currentName); // Add previous name to history
                    if (generatedNames.length > 15) {
                        generatedNames.pop(); // Keep only the last 15 names
                    }
                }

                // Update display and set currentName to the new one
                nameDisplay.textContent = fullName;
                currentName = fullName; // Store the latest name
                updateGeneratedNamesDisplay();
            }
        })
        .catch(() => { // ...and then display the no network error here!
            // Display error message in UI instead of logging to console
            nameDisplay.textContent = "Error: Unable to generate a name at this time. Is the app currently running?";
        });
    });

    // Function to update the previously generated names display
    function updateGeneratedNamesDisplay() {
        displayContainer.innerHTML = ""; // Clear previous list

        // Add all generated names to the display
        generatedNames.forEach(name => {
            const nameElement = document.createElement("div");
            nameElement.textContent = name;
            displayContainer.appendChild(nameElement);
        });
    }
});
