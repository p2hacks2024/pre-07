import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import *
import time

DATABASE_URL = "sqlite:///db.sqlite3"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# データベースの初期化
Base.metadata.drop_all(bind=engine)  # 既存のテーブルを削除
Base.metadata.create_all(bind=engine)  # 新しいテーブルを作成

# セッションの作成
session = SessionLocal()

# ユーザーの追加
user1 = User(name="test", password="aaa", colorR=255, colorG=0, colorB=0)
user2 = User(name="Neko Lovers", password="aaa", colorR=0, colorG=255, colorB=0)
user3 = User(name="Accord33", password="aaa" , colorR=0, colorG=0, colorB=255)
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

# アイデアの追加
idea1 = Ideas(title="星雲ジェネレータ", description="星雲を生成するアプリ", content="星雲を生成するアプリです", user_id=1)
idea2 = Ideas(title="猫フリクター", description="食品の温度を自動調整してくれるシステム", content="食品の温度を自動調整してくれるシステムです"*50, user_id=2)
idea3 = Ideas(title="持ち運べる扇風機", description="暑い夏を生き抜くために扇風機を持ち運べたらいいなぁ", content="持ち運び可能な扇風機です", user_id=3)
idea4 = Ideas(title='アイデアマッチング', description='アイデアをマッチングするアプリ', content='AIを使ってアイデア同士をマッチングさせて面白いアイデアになったら良いよね', user_id=3, image="1-p!nt.png-20241215051341.png")
idea5 = Ideas(title="シマエナガマップ", description="シマエナガの生息地をマップで表示するアプリ", content="シマエナガの生息地をマップで表示するアプリです", user_id=1)
idea6 = Ideas(title="猫のためのエアコン", description="猫のためのエアコンを作りたい", content="猫のためのエアコンを作りたいです", user_id=2)
session.add(idea1)
session.add(idea2)
session.add(idea3)
session.add(idea4)
session.add(idea5)
session.add(idea6)
session.commit()

palette1 = Palettes(user_id=1, idea_id=2)
palette2 = Palettes(user_id=1, idea_id=3)
palette3 = Palettes(user_id=1, idea_id=6)
session.add(palette1)
session.add(palette2)
session.add(palette3)
session.commit()


# セッションのクローズ
session.close()
