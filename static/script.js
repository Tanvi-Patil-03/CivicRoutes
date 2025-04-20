async function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatlogs = document.getElementById("chatlogs");

    chatlogs.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    
    const response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    chatlogs.innerHTML += `<p><strong>Bot:</strong> ${data.reply}</p>`;

    document.getElementById("user-input").value = "";
}
