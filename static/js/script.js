document.addEventListener("DOMContentLoaded", function () {
    // Array to store generated names (Limited to only the last 15)
    let generatedNames = [];
    let currentName = ""; // Stores the most recently generated name to prevent premature additions

    // Event listener for the "Generate Name" button
    document.getElementById('generate-button').addEventListener('click', function () {

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

                // Only add the previously generated name to the history if a new one is generated
                if (currentName) {
                    generatedNames.unshift(currentName); // Add previous name to history
                    if (generatedNames.length > 15) {
                        generatedNames.pop(); // Keep only the last 15 names
                    }
                }

                // Update display and set currentName to the new one
                document.getElementById('name-display').textContent = fullName;
                currentName = fullName; // Store the latest name
                updateGeneratedNamesDisplay();
            }
        })
        .catch(error => {
            console.error('Error:', error);
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
