package com.sporcu.akillitakip.data.local;

import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Query;
import androidx.room.Update;
import java.util.List;

@Dao
public interface WorkoutDao {
    @Insert
    void insert(Workout workout);

    @Update
    void update(Workout workout);

    @Query("SELECT * FROM workouts ORDER BY timestamp DESC")
    List<Workout> getAllWorkouts();

    @Query("SELECT AVG(heartRate) FROM workouts")
    int getAverageHeartRate();

    @Query("SELECT SUM(calories) FROM workouts")
    int getTotalCalories();
    
    @Query("DELETE FROM workouts")
    void deleteAll();
}
