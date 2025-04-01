function sendLineMessage(message) {
    fetch("https://api.line.me/v2/bot/message/push", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${LINE_ACCESS_TOKEN}`
        },
        body: JSON.stringify({
            to: ADMIN_USER_ID,
            messages: [{ type: "text", text: "測試訊息" }]
        })
    })
    .then(response => response.json())
    .then(data => console.log("訊息發送成功", data))
    .catch(error => {
        console.error("錯誤", error);
        alert("發送訊息失敗！");
    });
}
