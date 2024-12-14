from fastapi import FastAPI, Depends, HTTPException, File, UploadFile, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import Base, User, Ideas, Tags, Palettes, Goods
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware 
import datetime
from fastapi.responses import FileResponse
import requests
import re
from typing import Optional
import random

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="iu4hfwieufhlaiuhldsufhalsufhlsd", same_site="none", max_age=3600, https_only=True , session_cookie="session")

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://p2hacks2024.pages.dev", "https://accord33-feature-pwa.p2hacks2024.pages.dev", "https://p2hacks2024.accord33.org"],  # 特定のオリジンを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# テスト用のエンドポイント
@app.get("/")
def read_root():
    return {"Hello": "World"}

# 特定のユーザー情報とそのユーザーのアイデアを取得するエンドポイント
@app.get("/api/user/{username}")
def read_user(username: str):
    session = SessionLocal()
    user = session.query(User).filter(User.name == username).first()
    if not user:
        session.close()
        raise HTTPException(status_code=404, detail="User not found")
    ideas = session.query(Ideas).filter(Ideas.user_id == user.id).all()
    ideas_id = [idea.id for idea in ideas]
    session.close()
    return {"user": user, "ideas": ideas_id}

# アイデア一覧を取得するエンドポイント
@app.get("/api/ideas")
def get_ideas():
    session = SessionLocal()
    ideas = session.query(Ideas.id).all()
    session.close()
    return [idea.id for idea in ideas]

# idでアイデアを取得
@app.get("/api/idea/{id}")
def read_idea(id: int):
    idea_id = id
    session = SessionLocal()
    idea = session.query(Ideas).filter(Ideas.id == idea_id).first()
    if not idea:
        session.close()
        raise HTTPException(status_code=404, detail="Idea not found")
    tags = session.query(Tags).filter(Tags.idea_id == idea_id).all()
    username = session.query(User).filter(User.id == idea.user_id).first().name
    session.close()
    return {"idea": idea, "username": username, "tags": tags}

# アイデアを作成するエンドポイント
@app.post("/api/idea")
def create_idea(request: Request, title:str = Form(None), description: str = Form(None), file: Optional[UploadFile] = File(None)):
    print(title, description)
    user_id = request.session.get('user_id')
    if user_id is None:
        return {"message": "Please login first", "result": "Error"}
    session = SessionLocal()
    image_path = None
    print(file.filename)
    
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Unsupported file type. Only JPEG, PNG are allowed.")
    
    if file:
        image_path = f"{user_id}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}-{file.filename}"
        with open("images/"+image_path, "wb") as image_file:
            image_file.write(file.file.read())
    idea = Ideas(title=title, description=description, content=description, user_id=user_id, image=image_path)
    session.add(idea)
    session.commit()
    return {"message": "Idea created successfully", "idea_id": idea.id}                                 

# 画像を返すエンドポイント
@app.get("/api/image/{filename}")
def get_image(filename: str):
    file_path = f"images/{filename}"
    return FileResponse(file_path)

@app.get("/api/keep")
def keep_idea(request: Request, idea_id: int):
    user_id = request.session.get('user_id')
    session = SessionLocal()
    session.add(Palettes(user_id=user_id, idea_id=idea_id))
    session.commit()
    session.close()
    return {"message": "Idea kept successfully"}

@app.get("/api/user/keep/{idea_id}")
def get_kept_ideas(request: Request, idea_id: int):
    user_id = request.session.get('user_id')
    session = SessionLocal()
    ideas = session.query(Palettes).filter(Palettes.user_id == user_id).filter(Palettes.idea_id == idea_id).all()
    session.close()
    if ideas:
        return {"result": "Success"}
    else:
        return {"result": "Error"}

# 検索を行うエンドポイント
@app.get("/api/search")
def search_ideas(keyword: str):
    return_ideas = []
    session = SessionLocal()
    ideas = session.query(Ideas).filter(Ideas.title.like(f"%{keyword}%")).all()
    session.close()
    return_ideas = [idea.id for idea in ideas]
    
    return return_ideas

@app.get("/api/mix")
def mix_ideas(request: Request, keyword: str):
    user_id = request.session.get('user_id')
    username = request.session.get('username')
    keywords = keyword.split(",")
    
    url = 'https://dify.ict-lab.org/v1/chat-messages'
    headers = {
        'Authorization': 'Bearer app-LtocDiZ6vKnoB0QT7KwVUuKn',
        'Content-Type': 'application/json',
    }
    inputs = {}
    if len(keywords) % 2 != 0:
        return {"message": "Please provide even number of keywords"}
    
    for i in range(0, len(keywords), 2):
        inputs[f"idea_{i//2+1}_title"] = keywords[i]
        inputs[f"idea_{i//2+1}_details"] = keywords[i+1]
        
    data = {
        "inputs": inputs,
        "query": " ",
        "response_mode": "blocking",
        "conversation_id": "",
        "user": f"{username}"
    }
    print(data)
    return {"message": "タイトル：シマエナガ星雲生成アプリ<br><br>詳細：シマエナガの生息地データと、ユーザーが指定した色や形に基づいて、星雲を生成するアプリです。マップ上に表示されたシマエナガの生息地を参考に、その地域をイメージした星雲を生成できます。例えば、雪深い地域のシマエナガなら白と青を基調とした星雲、温暖な地域のシマエナガならオレンジや黄色の星雲などが生成されます。生成された星雲は壁紙やアバターとして利用可能です。シマエナガの可愛らしさと宇宙の神秘的な美しさを融合させた、癒やしのアプリです。", "result": "Success", "image":"1-difyimage-20241214205850.png"}
    
    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    ans = data["answer"] 
    url_pattern = r"\!\[image\]\(([^\)]+)\)"
    match = re.search(url_pattern, ans)
    if match:
        url = match.group(1)
        print("抽出されたURL:", url)
        text_without_url = re.sub(url_pattern, "", ans).strip()
        text_without_url = text_without_url.replace("\n", "<br>")
        print("URLを除去したテキスト:", text_without_url)

        # requestsを使用して画像をダウンロード
        output_file = f"{user_id}-difyimage-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        try:
            response = requests.get("https://dify.ict-lab.org"+url, stream=True)
            response.raise_for_status()
            with open("images/"+output_file, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            print(f"画像を正常にダウンロードしました: {output_file}")
            return {"message": text_without_url, "image": output_file, "result": "Success"}
        except requests.exceptions.RequestException as e:
            return {"result": f"Error {e}", "message": ans}
    else:
        return {"result": "No image found", "message": ans}
    
    return {"message": "Mixed ideas successfully"}

@app.get("/api/palette")
def get_palette(request: Request):
    user_id = request.session.get('user_id')
    if not user_id:
        raise HTTPException(status_code=401, detail="Not authenticated")
    session = SessionLocal()
    palettes = session.query(Palettes).filter(Palettes.user_id == user_id).all()
    ideas = session.query(Ideas).filter(Ideas.user_id == user_id).all()
    session.close()
    username = request.session.get('username')
    
    return sorted([palette.idea_id for palette in palettes] + [idea.id for idea in ideas])

# ログイン処理を行うエンドポイント
@app.post("/api/login")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    session = SessionLocal()
    user = session.query(User).filter(User.name == form_data.username).first()
    session.close()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username")
    request.session['username'] = form_data.username
    request.session['user_id'] = user.id
    print(form_data.username, user.id)
    return {"message": "Logged in successfully"}

# ログイン中のユーザー情報を取得するエンドポイント
@app.get("/api/me")
def read_me(request: Request):
    print(request.cookies)
    username = request.session.get('username')
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"username": username, "detail": "Success"}

# ログアウト処理を行うエンドポイント
@app.post("/api/logout")
def logout(request: Request):
    request.session.pop('username', None)
    return {"message": "Logged out successfully"}

@app.post("/api/signup")
def signup(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    session = SessionLocal()
    user = session.query(User).filter(User.name == form_data.username).first()
    if user:
        session.close()
        raise HTTPException(status_code=400, detail="Username already exists")
    user = User(name=form_data.username, password=form_data.password, colorR=random.randint(0, 255), colorG=random.randint(0, 255), colorB=random.randint(0, 255))
    session.add(user)
    session.commit()
    session.close()
    return {"message": "User created successfully", "detail": "Success"}