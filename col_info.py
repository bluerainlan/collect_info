<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>請假申請表</title>
    <script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>
</head>
<body>
    <h2>請假申請表</h2>
    <form id="leaveForm">
        <label>姓名：</label>
        <input type="text" id="name" required><br>

        <label>日期：</label>
        <input type="date" id="date" required><br>

        <label>年級：</label>
        <select id="grade">
            <option value="一年級">一年級</option>
            <option value="二年級">二年級</option>
            <option value="三年級">三年級</option>
        </select><br>

        <label>請假事由：</label>
        <textarea id="reason" required></textarea><br>

        <button type="button" onclick="submitLeave()">提交</button>
    </form>

    <script>
        const LINE_ACCESS_TOKEN = "你的 Channel Access Token";  // 填入你的 LINE Bot Token
        const ADMIN_USER_ID = "管理員的 User ID";  // 填入管理員的 User ID

        async function initLiff() {
            await liff.init({ liffId: "你的 LIFF ID" });
            if (!liff.isLoggedIn()) {
                liff.login();
            }
        }

        async function submitLeave() {
            const name = document.getElementById("name").value;
            const date = document.getElementById("date").value;
            const grade = document.getElementById("grade").value;
            const reason = document.getElementById("reason").value;
            
            const userId = liff.getDecodedIDToken()?.sub || "未知使用者";

            const leaveMessage = `📌 **請假申請**\n👤 姓名：${name}\n📅 日期：${date}\n🎓 年級：${grade}\n📝 事由：${reason}\n🔗 申請人 LINE ID: ${userId}`;

            // 發送請假訊息給管理員
            sendLineMessage(leaveMessage);

            alert("請假申請已提交！");
            liff.closeWindow();
        }

        function sendLineMessage(message) {
            fetch("https://api.line.me/v2/bot/message/push", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": `Bearer ${LINE_ACCESS_TOKEN}`
                },
                body: JSON.stringify({
                    to: ADMIN_USER_ID,
                    messages: [{ type: "text", text: message }]
                })
            }).then(response => response.json())
              .then(data => console.log("訊息發送成功", data))
              .catch(error => console.error("錯誤", error));
        }

        initLiff();
    </script>
</body>
</html>
