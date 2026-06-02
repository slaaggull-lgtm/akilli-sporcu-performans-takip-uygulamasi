package com.akillitakip.data.local;

import androidx.room.Dao;
import androidx.room.Insert;
import androidx.room.Update;
import androidx.room.Query;
import com.akillitakip.data.local.entity.Workout;
import java.util.List;

/**
 * Antrenman verisi erisim nesnesi (DAO).
 * Room'un SQL sorgularini derleme zamaninda dogruladigi arayuz.
 */
@Dao
public interface WorkoutDao {

    /** Yeni antrenman kaydeder */
    @Insert
    void insert(Workout workout);

    /** Mevcut antrenman gunceller */
    @Update
    void update(Workout workout);

    /**
     * Tum antrenmanlar — en son yapilan en ustte.
     *
     * @return Zaman damgasina gore azalan sirada antrenman listesi
     */
    @Query("SELECT * FROM workouts ORDER BY timestamp DESC")
    List<Workout> getAllWorkouts();

    /**
     * Belirli bir kullanicinin antrenmanlarini getirir.
     *
     * @param userId Kullanici kimlik numarasi
     * @return Kullaniciya ait antrenman listesi
     */
    @Query("SELECT * FROM workouts WHERE userId = :userId ORDER BY timestamp DESC")
    List<Workout> getWorkoutsByUser(int userId);

    /**
     * Ortalama kalp atisi istatistigi.
     *
     * @return Tum antrenmanlar icin ortalama kalp atisi (bpm)
     */
    @Query("SELECT AVG(heartRate) FROM workouts")
    double getAverageHeartRate();

    /**
     * Toplam yakilan kalori.
     *
     * @return Tum antrenmanlar icin toplam kalori
     */
    @Query("SELECT SUM(calories) FROM workouts")
    double getTotalCalories();

    /**
     * Toplam antrenman sayisi.
     *
     * @return Veritabanindaki antrenman sayisi
     */
    @Query("SELECT COUNT(*) FROM workouts")
    int getWorkoutCount();

    /** Tum antrenman kayitlarini siler (test/sifirlama icin) */
    @Query("DELETE FROM workouts")
    void deleteAll();
}
