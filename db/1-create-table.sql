CREATE TABLE IF NOT EXISTS "players" (
	"id" serial NOT NULL UNIQUE,
	"username" varchar(255) NOT NULL,
	"registration_date" timestamp NOT NULL,
	PRIMARY KEY ("id")
);

CREATE INDEX "players_index_0"
ON "players" ("username");

CREATE TABLE IF NOT EXISTS "actions" (
	"action_id" serial NOT NULL UNIQUE,
	"action_name" varchar(255) NOT NULL,
	"action_type" varchar(255) NOT NULL,
	PRIMARY KEY ("action_id")
);

CREATE INDEX "actions_index_0"
ON "actions" ("action_name");

CREATE TABLE IF NOT EXISTS "levels" (
	"level_id" serial NOT NULL UNIQUE,
	"difficulty" varchar(255) NOT NULL,
	PRIMARY KEY ("level_id")
);

CREATE TABLE IF NOT EXISTS "game_events" (
	"event_id" serial NOT NULL UNIQUE,
	"player_id" int NOT NULL,
	"action_id" int NOT NULL,
	"level_id" int NOT NULL,
	"points" int NOT NULL,
	"event_time" timestamp NOT NULL,
	PRIMARY KEY ("event_id")
);

CREATE INDEX "game_events_index_0"
ON "game_events" ("player_id");

CREATE INDEX "game_events_index_1"
ON "game_events" ("action_id");

CREATE INDEX "game_events_index_2"
ON "game_events" ("level_id");

CREATE INDEX "game_events_index_3"
ON "game_events" ("event_time");

ALTER TABLE "game_events"
ADD FOREIGN KEY ("player_id") REFERENCES "players" ("id")
ON UPDATE NO ACTION
ON DELETE CASCADE;

ALTER TABLE "game_events"
ADD FOREIGN KEY ("action_id") REFERENCES "actions" ("action_id")
ON UPDATE NO ACTION
ON DELETE CASCADE;

ALTER TABLE "game_events"
ADD FOREIGN KEY ("level_id") REFERENCES "levels" ("level_id")
ON UPDATE NO ACTION
ON DELETE CASCADE;
