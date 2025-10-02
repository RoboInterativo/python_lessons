    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
    from sqlalchemy import String, Integer

    class Base(DeclarativeBase):
        pass

    class Tasks(Base):
        __tablename__ = "tasks"
        id: Mapped[int] = mapped_column(primary_key=True)
        Column("id", Integer, primary_key=True),
    sqlite_autoincrement=True,
        title: Mapped[str] = mapped_column(String)
        status: Mapped[str] = mapped_column(String)
        created_at  Mapped[str] = mapped_column(String)



                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    status TEXT DEFAULT 'не выполнено',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
