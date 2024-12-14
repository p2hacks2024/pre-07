from fastapi import FastAPI, Depends, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import Base, User, Ideas, Tags, Palettes, Goods
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware 
import datetime
from fastapi.responses import FileResponse

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key", same_site="none", max_age=3600, https_only=True , session_cookie="session")

# CORSの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://p2hacks2024.pages.dev", "https://72dd05f4.p2hacks2024.pages.dev"],  # 特定のオリジンを許可
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
def create_idea(request: Request, title: str, description: str, file: UploadFile = File(None)):
    user_id = request.session.get('user_id')
    session = SessionLocal()
    image_path = None
    if file:
        image_path = f"{user_id}-{file.filename}-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        with open("images/"+image_path, "wb") as image_file:
            image_file.write(file.file.read())
    idea = Ideas(title=title, description=description, user_id=user_id, image=image_path)
    session.add(idea)
    session.commit()
    session.close()
    return {"message": "Idea created successfully"}

# 画像を返すエンドポイント
@app.get("/api/image/{filename}")
def get_image(filename: str):
    file_path = f"images/{filename}"
    return FileResponse(file_path)


# 検索を行うエンドポイント
@app.get("/api/search")
def search_ideas(keyword: str):
    return_ideas = []
    session = SessionLocal()
    ideas = session.query(Ideas).filter(Ideas.title.like(f"%{keyword}%")).all()
    session.close()
    return_ideas = [idea.id for idea in ideas]
    
    return return_ideas

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
    return {"username": username}

# ログアウト処理を行うエンドポイント
@app.post("/api/logout")
def logout(request: Request):
    request.session.pop('username', None)
    return {"message": "Logged out successfully"}