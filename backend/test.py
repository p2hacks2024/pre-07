import requests
import re

# APIエンドポイント
url = 'https://dify.ict-lab.org/v1/chat-messages'

# ヘッダー情報
headers = {
    'Authorization': 'Bearer app-LtocDiZ6vKnoB0QT7KwVUuKn',
    'Content-Type': 'application/json',
}

# データペイロード
data = {
    "inputs": {
        "idea_1_title": "夏は暑い",
        "idea_1_details": "夏が暑すぎるので外を歩き回るのがつらいのをどうにかしたい",
        "idea_2_title": "扇風機",
        "idea_2_details": "夏の定番アイテム"
    },
    "query": " ",
    "response_mode": "blocking",
    "conversation_id": "",
    "user": "abc-123"
}

# POSTリクエストの送信
response = requests.post(url, headers=headers, json=data)

data = response.json()

# レスポンスを出力
print("Status Code:", response.status_code)
print("Response Body:", response.json())

ans = data["answer"] 

url_pattern = r"\!\[image\]\(([^\)]+)\)"
match = re.search(url_pattern, ans)

if match:
    url = match.group(1)
    print("抽出されたURL:", url)

    # requestsを使用して画像をダウンロード
    output_file = "downloaded_image.png"
    try:
        response = requests.get("https://dify.ict-lab.org"+url, stream=True)
        response.raise_for_status()
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"画像を正常にダウンロードしました: {output_file}")
    except requests.exceptions.RequestException as e:
        print(f"画像のダウンロード中にエラーが発生しました: {e}")
else:
    print("URLが見つかりませんでした。")
