DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS evtTimeline;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
    pwdHash TEXT NOT NULL,
    authority INTEGER DEFAULT 0,
    userType INTEGER DEFAULT 1
);

CREATE TABLE evtTimeline (
    evtId INTEGER PRIMARY KEY NOT NULL,
    evtTitle TEXT,
    updateT TIMESTAMP NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP, 'localtime')),
    dayNum INTEGER,
    evtType TEXT,
    teamName TEXT,
    teamType INTEGER,
    evtState TEXT
);