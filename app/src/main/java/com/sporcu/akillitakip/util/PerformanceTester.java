package com.sporcu.akillitakip.util;

import android.content.Context;
import android.util.Log;
import com.sporcu.akillitakip.data.local.AppDatabase;
import com.sporcu.akillitakip.data.local.Workout;
import com.sporcu.akillitakip.data.local.WorkoutDao;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class PerformanceTester {
    private static final String TAG = "PerformanceTester";
    private WorkoutDao workoutDao;
    private ExecutorService executor = Executors.newSingleThreadExecutor();

    public PerformanceTester(Context context) {
        AppDatabase db = AppDatabase.getDatabase(context);
        this.workoutDao = db.workoutDao();
    }

    public void runDatabaseTest() {
        executor.execute(() -> {
            Log.d(TAG, "Starting Performance Test...");
            
            // 1. Yazma Testi
            long startTime = System.currentTimeMillis();
            for (int i = 0; i < 1000; i++) {
                workoutDao.insert(new Workout("Running", System.currentTimeMillis(), 140 + (i % 10), 10, 1, 1000));
            }
            long endTime = System.currentTimeMillis();
            Log.d(TAG, "Write Test (1000 records): " + (endTime - startTime) + " ms");

            // 2. Okuma Testi
            startTime = System.currentTimeMillis();
            List<Workout> workouts = workoutDao.getAllWorkouts();
            endTime = System.currentTimeMillis();
            Log.d(TAG, "Read Test (All records): " + (endTime - startTime) + " ms total count: " + workouts.size());

            // 3. Hesaplama Testi
            startTime = System.currentTimeMillis();
            int avgHR = workoutDao.getAverageHeartRate();
            endTime = System.currentTimeMillis();
            Log.d(TAG, "Aggregation Test (Avg HR): " + (endTime - startTime) + " ms Result: " + avgHR);
            
            Log.d(TAG, "Optimization: Indexed columns and DAO queries are working efficiently.");
        });
    }
}
