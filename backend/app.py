from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.models import Base, Ideas, User, Tags
from starlette.middleware.sessions import SessionMiddleware
from starlette.requests import Request

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/")
def read_root():
    # ルートエンドポイント
    return {"Hello": "World"}

@app.get("/api/ideas/{idea_id}")
def read_item(idea_id: int):
    # 特定のアイデアと関連するタグを取得
    session = SessionLocal()
    idea = session.query(Ideas).filter(Ideas.id == idea_id).first()
    if not idea:
        session.close()
        raise HTTPException(status_code=404, detail="Idea not found")
    tags = session.query(Tags).filter(Tags.idea_id == idea_id).all()
    session.close()
    return {"idea": idea, "tags": tags}

@app.get("/api/ideas")
def read_items():
    # すべてのアイデアのIDを取得
    session = SessionLocal()
    ideas = session.query(Ideas.id).all()
    session.close()
    return [idea.id for idea in ideas]

@app.post("/api/idea")
def create_item(request: Request, title: str, description: str):
    # 新しいアイデアを作成
    user_id = request.session.get('user_id')
    session = SessionLocal()
    idea = Ideas(title=title, description=description, user_id=user_id)
    session.add(idea)
    session.commit()
    session.close()
    return idea

@app.post("/api/login")
def login(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    # ログイン処理
    session = SessionLocal()
    user = session.query(User).filter(User.name == form_data.username).first()
    session.close()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username")
    request.session['username'] = form_data.username
    request.session['user_id'] = user.id
    print(form_data.username, user.id)
    return {"message": "Logged in successfully"}

@app.get("/api/me")
def read_me(request: Request):
    # ログイン中のユーザー情報を取得
    username = request.session.get('username')
    if not username:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return {"username": username}

@app.post("/api/logout")
def logout(request: Request):
    # ログアウト処理
    request.session.pop('username', None)
    return {"message": "Logged out successfully"}