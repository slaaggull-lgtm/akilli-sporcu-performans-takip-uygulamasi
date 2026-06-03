package com.akillitakip.data.local.entity;

import androidx.room.Entity;
import androidx.room.ForeignKey;
import androidx.room.Index;
import androidx.room.PrimaryKey;

/**
 * Antrenman varligi (Entity).
 * Room bu sinifi SQLite tablosuna donusturur.
 *
 * user_id uzerinde foreign key ve indeksleme uygulanmistir.
 * Sorgu hizini artirmak icin timestamp kolonuna da indeks eklendi.
 */
@Entity(
    tableName = "workouts",
    foreignKeys = @ForeignKey(
        entity = User.class,
        parentColumns = "id",
        childColumns = "userId",
        onDelete = ForeignKey.CASCADE
    ),
    indices = {
        @Index("userId"),
        @Index("timestamp")
    }
)
public class Workout {

    @PrimaryKey(autoGenerate = true)
    public int id;

    /** Antrenmanin sahibi olan kullanicinin id'si */
    public int userId;

    /** Antrenman turu: "Kosu", "Yuzme", "Bisiklet" vs. */
    public String workoutType;

    /** Unix zaman damgasi (milisaniye) */
    public long timestamp;

    /** Sure (dakika) */
    public int durationMinutes;

    /** Ortalama kalp atisi (bpm) */
    public int heartRate;

    /** Yakilan kalori (kcal) */
    public double calories;

    /** Adim sayisi */
    public int steps;

    /** Kat edilen mesafe (km) */
    public double distanceKm;

    /** Kullanici notu (opsiyonel) */
    public String notes;
}
