package com.sporcu.akillitakip.data.local;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

@Entity(tableName = "workouts")
public class Workout {
    @PrimaryKey(autoGenerate = true)
    private int id;
    
    private String type;
    private long timestamp;
    private int heartRate;
    private int steps;
    private int calories;
    private long duration; // in milliseconds

    public Workout(String type, long timestamp, int heartRate, int steps, int calories, long duration) {
        this.type = type;
        this.timestamp = timestamp;
        this.heartRate = heartRate;
        this.steps = steps;
        this.calories = calories;
        this.duration = duration;
    }

    // Getters and Setters
    public int getId() { return id; }
    public void setId(int id) { this.id = id; }
    public String getType() { return type; }
    public void setType(String type) { this.type = type; }
    public long getTimestamp() { return timestamp; }
    public void setTimestamp(long timestamp) { this.timestamp = timestamp; }
    public int getHeartRate() { return heartRate; }
    public void setHeartRate(int heartRate) { this.heartRate = heartRate; }
    public int getSteps() { return steps; }
    public void setSteps(int steps) { this.steps = steps; }
    public int getCalories() { return calories; }
    public void setCalories(int calories) { this.calories = calories; }
    public long getDuration() { return duration; }
    public void setDuration(long duration) { this.duration = duration; }
}
