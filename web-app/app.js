document.getElementById("recommendation-form").addEventListener("submit", async (event) => {
    event.preventDefault();
    const userId = document.getElementById("user-id").value;

    try {
        const response = await fetch(`/api/recommendations?user_id=${userId}`);
        const data = await response.json();

        const recommendationsDiv = document.getElementById("recommendations");
        recommendationsDiv.innerHTML = `<h2>Recommendations:</h2><ul>${data.recommendations.map(item => `<li>${item}</li>`).join('')}</ul>`;
    } catch (error) {
        console.error("Error fetching recommendations:", error);
    }
});
