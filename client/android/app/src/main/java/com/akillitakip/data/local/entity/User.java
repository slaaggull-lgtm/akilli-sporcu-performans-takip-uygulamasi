package com.akillitakip.data.local.entity;

import androidx.room.Entity;
import androidx.room.PrimaryKey;

/**
 * Kullanici varligi (Entity).
 * Sporcunun profil ve fiziksel parametre bilgilerini saklar.
 * Bu veriler antrenman yogunlugu algoritmalarinin temel girdisidir.
 */
@Entity(tableName = "users")
public class User {

    @PrimaryKey(autoGenerate = true)
    public int id;

    /** Firebase kullanici kimlik numarasi */
    public String firebaseUid;

    public String name;
    public String email;

    /** Yas — maksimum kalp atisi hesabinda kullanilir (220 - yas) */
    public int age;

    /** Boy (santimetre) */
    public double heightCm;

    /** Agirlik (kilogram) */
    public double weightKg;

    /**
     * Fitness seviyesi.
     * Degerler: "Beginner", "Intermediate", "Advanced"
     */
    public String fitnessLevel;

    /** Kayit tarihi (ISO 8601 formati: "2026-05-28") */
    public String createdAt;
}
