<!-- DisplayResponse.svelte -->
<script>
    import { onMount } from 'svelte';
    
    // Define a reactive variable to store the response
    let response = '';
    let userInput = '';

    // Function to handle form submission
    async function handleSubmit(event) {
        event.preventDefault(); // Prevent default form submission behavior
        
        // Display loading message while fetching data
        response = 'Loading...';
        
        try {
            const fetchResult = await fetch('http://127.0.0.1:8000/api/dgpt', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    user_input: userInput,
                }),
            });
            
            // Check if request was successful (status 200)
            if (fetchResult.ok) {
                const data = await fetchResult.json(); // Parse response JSON
                response = data.response; // Update response
            } else {
                response = 'Error: Failed to fetch data'; // Update response with error message
            }
        } catch (error) {
            console.error('Fetch error:', error);
            response = 'Error: Failed to fetch data'; // Update response with error message
        }
    }
</script>

<h2>Response</h2>
<form on:submit={handleSubmit}>
    <label for="user-input">User Input:</label>
    <input class="text-black" type="text" id="user-input" bind:value={userInput}>
    <button type="submit">Submit</button>
</form>

<p>{response}</p>
