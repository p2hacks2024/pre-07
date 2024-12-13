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
user1 = User(name="test", password="aaa",email="test@example.com")
user2 = User(name="test2", password="bbb", email="test2@exampe.com")
user3 = User(name="test3", password="ccc", email="test3@example.com")
session.add(user1)
session.add(user2)
session.add(user3)
session.commit()

# アイデアの追加
idea1 = Ideas(title="Idea 1", description="Description for idea 1", user=user1, content="5000兆円欲しい")
idea2 = Ideas(title="Idea 2", description="Description for idea 2", user=user2, content="5000兆円欲しい")
idea3 = Ideas(title="Idea 3", description="Description for idea 3", user=user3, content="5000兆円欲しい"*50)
idea4 = Ideas(title="Idea 4", description="Description for idea 4", user=user1, content="5000兆円欲しい")
idea5 = Ideas(title="Idea 5", description="Description for idea 5", user=user2, content="5000兆円欲しい")
idea6 = Ideas(title="Idea 6", description="Description for idea 6", user=user3, content="5000兆円欲しい")
idea7 = Ideas(title="Idea 7", description="Description for idea 7", user=user1, content="5000兆円欲しい")
idea8 = Ideas(title="Idea 8", description="Description for idea 8", user=user2, content="5000兆円欲しい8")
session.add(idea1)
session.add(idea2)
session.add(idea3)
session.add(idea4)
session.add(idea5)
session.add(idea6)
session.add(idea7)
session.add(idea8)
session.commit()

# タグの追加
idea1.tags.append(Tags(tag="tag1"))
idea1.tags.append(Tags(tag="tag2"))
idea2.tags.append(Tags(tag="tag3"))
session.commit()


palette1 = Palettes(user=user1, idea=idea2)
palette2 = Palettes(user=user1, idea=idea3)
palette3 = Palettes(user=user1, idea=idea5)
session.add(palette1)
session.add(palette2)
session.add(palette3)
session.commit()

# セッションのクローズ
session.close()
