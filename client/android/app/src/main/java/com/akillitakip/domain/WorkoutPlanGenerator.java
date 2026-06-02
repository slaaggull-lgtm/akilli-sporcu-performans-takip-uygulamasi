package com.akillitakip.domain;

/**
 * Kisisellestirilmis antrenman plani uretici.
 *
 * Kullanicinin profiline (seviye, haftalik gun sayisi, hedef, ekipman)
 * gore uygun antrenman bolunmesi ve yogunluk stratejisi secer.
 *
 * Spor bilimleri referanslari:
 *   - Selye'nin Genel Adaptasyon Sendromu (GAS)
 *   - Lineer ve Dalgali Periodizasyon modelleri
 *   - Hacim/Yogunluk iliskisi (MEV ve MRV esikleri)
 */
public class WorkoutPlanGenerator {

    /**
     * Kullanici profili veri transfer nesnesi.
     */
    public static class UserProfile {
        /** "Beginner", "Intermediate", "Advanced" */
        public String level;

        /** Haftada kac gun antrenman yapabilir (2-6 arasi) */
        public int weeklyDays;

        /** "Gym" veya "Home" */
        public String equipment;

        /** "Strength", "Hypertrophy" veya "FatLoss" */
        public String goal;

        /** Yas (maksimum kalp atisi ve toparlanma icin) */
        public int age;
    }

    /**
     * Kullanici profiline gore antrenman bolunmesi ve stratejisini secer.
     *
     * Kural 1 — Gun sayisina gore bolunme:
     *   2-3 gun → Full Body (tum vucudu her seansta calis)
     *   4 gun   → Upper/Lower Split (ust/alt vucut ayirimi)
     *   5+ gun  → Push/Pull/Legs (itis/cekis/bacak)
     *
     * Kural 2 — Seviye ve hedefe gore set/tekrar:
     *   Beginner → %60-70 1RM, 8-10 set/kas grubu, Lineer ilerleme
     *   Diger    → %70-85 1RM, 12-20 set/kas grubu, DUP (Dalgali Periodizasyon)
     *
     * @param profile Kullanici profili
     * @return Antrenman plani ozeti (metin)
     */
    public String generateSplitsAndStrategy(UserProfile profile) {
        StringBuilder plan = new StringBuilder();

        // Kural 1: Bolunme secimi
        if (profile.weeklyDays <= 3) {
            plan.append("Bolunme: Tum Vucut (Full Body)\n");
            plan.append("Neden: Dusuk frekansta kas sentezini maksimumda tutmak.\n\n");
        } else if (profile.weeklyDays == 4) {
            plan.append("Bolunme: Ust / Alt Vucut (Upper/Lower Split)\n");
            plan.append("Neden: Kas gruplarina 48 saat toparlanma suresi tanimak.\n\n");
        } else {
            plan.append("Bolunme: Itis / Cekis / Bacak (Push/Pull/Legs)\n");
            plan.append("Neden: Yuksek hacimli antrenmanlari optimize etmek.\n\n");
        }

        // Kural 2: Yogunluk stratejisi
        if ("Beginner".equals(profile.level)) {
            plan.append("Yogunluk: %60-70 1RM (Maksimum Tek Tekrar)\n");
            plan.append("Hacim: Kas grubu basina haftada 8-10 set\n");
            plan.append("Strateji: Lineer (Linear) Ilerleme Modeli\n");
            plan.append("Aciklama: Her antrenmanda kucuk agirlik artislari (+2.5 kg).\n");
        } else {
            plan.append("Yogunluk: %70-85 1RM\n");
            plan.append("Hacim: Kas grubu basina haftada 12-20 set\n");
            plan.append("Strateji: Gunluk Dalgali Periodizasyon (DUP)\n");
            plan.append("Aciklama: Her gun farkli rep araligi (kuvvet/hipertrofi/dayaniklilik).\n");
        }

        // Ekipman notu
        if ("Home".equals(profile.equipment)) {
            plan.append("\nEkipman Notu: Ev antrenman versiyonlari secilecek ");
            plan.append("(vucutagirlik + dambil alternatifleri).\n");
        }

        return plan.toString();
    }

    /**
     * Belirli bir gun icin egzersiz listesi uretir.
     *
     * @param dayIndex  Haftanin kacinci gunu (1'den baslar)
     * @param splitType "FullBody", "Upper", "Lower", "Push", "Pull" veya "Legs"
     * @return O gun yapilacak egzersizlerin listesi (metin)
     */
    public String generateDayExercises(int dayIndex, String splitType) {
        switch (splitType) {
            case "Push":
                return "Gün " + dayIndex + " (İtiş):\n"
                        + "1. Bariyer Bench Press 4x8\n"
                        + "2. Omuz Press 3x10\n"
                        + "3. Triceps Dips 3x12\n"
                        + "4. Lateral Raise 3x15\n";
            case "Pull":
                return "Gün " + dayIndex + " (Çekiş):\n"
                        + "1. Barbell Row 4x8\n"
                        + "2. Pull-Up 3x8\n"
                        + "3. Biceps Curl 3x12\n"
                        + "4. Face Pull 3x15\n";
            case "Legs":
                return "Gün " + dayIndex + " (Bacak):\n"
                        + "1. Squat 4x8\n"
                        + "2. Romanian Deadlift 3x10\n"
                        + "3. Leg Press 3x12\n"
                        + "4. Calf Raise 4x15\n";
            default:
                return "Gün " + dayIndex + " (Tüm Vücut):\n"
                        + "1. Squat 3x10\n"
                        + "2. Bench Press 3x10\n"
                        + "3. Barbell Row 3x10\n"
                        + "4. Shoulder Press 2x12\n";
        }
    }
}
