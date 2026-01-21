import datetime
from sqlalchemy import (
    DateTime,
    ForeignKeyConstraint,
    Index,
    Integer,
    PrimaryKeyConstraint,
    String,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = "players"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="players_pkey"),
        Index("players_index_0", "username"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    registration_date: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=False
    )

    game_events: Mapped[list["GameEvent"]] = relationship(
        "GameEvent",
        back_populates="player",
        cascade="all, delete"
    )

class Action(Base):
    __tablename__ = "actions"
    __table_args__ = (
        PrimaryKeyConstraint("action_id", name="actions_pkey"),
        Index("actions_index_0", "action_name"),
    )

    action_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    action_name: Mapped[str] = mapped_column(String(255), nullable=False)
    action_type: Mapped[str] = mapped_column(String(255), nullable=False)

    game_events: Mapped[list["GameEvent"]] = relationship(
        "GameEvent",
        back_populates="action",
        cascade="all, delete"
    )

class Level(Base):
    __tablename__ = "levels"
    __table_args__ = (
        PrimaryKeyConstraint("level_id", name="levels_pkey"),
    )

    level_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    difficulty: Mapped[str] = mapped_column(String(255), nullable=False)

    game_events: Mapped[list["GameEvent"]] = relationship(
        "GameEvent",
        back_populates="level",
        cascade="all, delete"
    )

class GameEvent(Base):
    __tablename__ = "game_events"
    __table_args__ = (
        ForeignKeyConstraint(
            ["player_id"],
            ["players.id"],
            name="game_events_player_id_fkey",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["action_id"],
            ["actions.action_id"],
            name="game_events_action_id_fkey",
            ondelete="CASCADE",
        ),
        ForeignKeyConstraint(
            ["level_id"],
            ["levels.level_id"],
            name="game_events_level_id_fkey",
            ondelete="CASCADE",
        ),
        PrimaryKeyConstraint("event_id", name="game_events_pkey"),
        Index("game_events_index_0", "player_id"),
        Index("game_events_index_1", "action_id"),
        Index("game_events_index_2", "level_id"),
        Index("game_events_index_3", "event_time"),
    )

    event_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    player_id: Mapped[int] = mapped_column(Integer, nullable=False)
    action_id: Mapped[int] = mapped_column(Integer, nullable=False)
    level_id: Mapped[int] = mapped_column(Integer, nullable=False)
    points: Mapped[int] = mapped_column(Integer, nullable=False)
    event_time: Mapped[datetime.datetime] = mapped_column(
        DateTime, nullable=False
    )

    player: Mapped["Player"] = relationship("Player", back_populates="game_events")
    action: Mapped["Action"] = relationship("Action", back_populates="game_events")
    level: Mapped["Level"] = relationship("Level", back_populates="game_events")
