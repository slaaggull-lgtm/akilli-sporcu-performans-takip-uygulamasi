package com.akillitakip.data.local;

import android.content.Context;
import androidx.room.Database;
import androidx.room.Room;
import androidx.room.RoomDatabase;
import com.akillitakip.data.local.entity.User;
import com.akillitakip.data.local.entity.Workout;

/**
 * Ana veritabani sinifi.
 * Room Persistence Library kullanan SQLite sarmalayici.
 *
 * Thread-safe Singleton deseni — double-checked locking ile.
 * Uygulamada tek bir veritabani ornegi kullanilmasini garanti eder.
 */
@Database(entities = {User.class, Workout.class}, version = 1, exportSchema = false)
public abstract class AppDatabase extends RoomDatabase {

    private static volatile AppDatabase INSTANCE;

    /** WorkoutDao erisim noktasi */
    public abstract WorkoutDao workoutDao();

    /**
     * Veritabani ornegini dondurur. Yoksa olusturur.
     *
     * @param context Uygulama context'i
     * @return AppDatabase singleton ornegi
     */
    public static AppDatabase getDatabase(final Context context) {
        if (INSTANCE == null) {
            synchronized (AppDatabase.class) {
                if (INSTANCE == null) {
                    INSTANCE = Room.databaseBuilder(
                            context.getApplicationContext(),
                            AppDatabase.class,
                            "sporcu_database"
                    ).build();
                }
            }
        }
        return INSTANCE;
    }
}
