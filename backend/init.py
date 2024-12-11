import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Base, User, Ideas, Tags

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
idea1 = Ideas(title="Idea 1", description="Description for idea 1", user=user1)
idea2 = Ideas(title="Idea 2", description="Description for idea 2", user=user2)
idea3 = Ideas(title="Idea 3", description="Description for idea 3", user=user3, fork=idea1.id)
session.add(idea1)
session.add(idea2)
session.add(idea3)
session.commit()

# タグの追加
idea1.tags.append(Tags(tag="tag1"))
idea1.tags.append(Tags(tag="tag2"))
idea2.tags.append(Tags(tag="tag3"))
session.commit()



# セッションのクローズ
session.close()
