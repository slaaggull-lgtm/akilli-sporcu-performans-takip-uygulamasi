PRAGMA foreign_keys = ON;

CREATE TABLE Users (
    user_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name     TEXT NOT NULL,
    age           INTEGER,
    height_cm     REAL,
    weight_kg     REAL,
    fitness_level TEXT,
    created_at    TEXT NOT NULL DEFAULT (DATE('now'))
);

CREATE TABLE Workouts (
    workout_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id          INTEGER NOT NULL,
    workout_date     TEXT NOT NULL,
    duration_minutes INTEGER,
    calories_burned  REAL,
    avg_heart_rate   REAL,
    notes            TEXT,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Exercises (
    exercise_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    workout_id       INTEGER NOT NULL,
    exercise_name    TEXT NOT NULL,
    set_count        INTEGER,
    rep_count        INTEGER,
    duration_seconds INTEGER,
    FOREIGN KEY (workout_id) REFERENCES Workouts(workout_id) ON DELETE CASCADE
);

CREATE TABLE PerformanceMetrics (
    metric_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id     INTEGER NOT NULL,
    metric_date TEXT NOT NULL,
    steps       INTEGER,
    distance_km REAL,
    sleep_hours REAL,
    hrv         REAL,
    vo2max      REAL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE INDEX idx_workouts_user_id ON Workouts(user_id);
CREATE INDEX idx_workouts_date ON Workouts(workout_date);
CREATE INDEX idx_metrics_user_id ON PerformanceMetrics(user_id);
