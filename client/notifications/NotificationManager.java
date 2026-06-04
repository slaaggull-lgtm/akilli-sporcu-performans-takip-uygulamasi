package com.sporcu.akillitakip.notifications;

import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.os.Build;

import androidx.core.app.NotificationCompat;
import androidx.core.app.NotificationManagerCompat;

/**
 * Uygulama genelinde tüm bildirimleri yöneten merkezi sınıf.
 * Antrenman hatırlatmaları, sakatlık uyarıları ve performans
 * geri bildirim bildirimlerini kapsır.
 *
 * @author Akıllı Sporcu Takip Ekibi
 */
public class SmartFitNotificationManager {

    // ------------------------------------------------------------------ //
    //  Kanal Sabitleri
    // ------------------------------------------------------------------ //
    public static final String CHANNEL_WORKOUT     = "channel_workout_reminder";
    public static final String CHANNEL_ALERT       = "channel_health_alert";
    public static final String CHANNEL_PERFORMANCE = "channel_performance";

    // Bildirim ID aralıkları (çakışmayı önlemek için)
    private static final int ID_WORKOUT_BASE     = 1000;
    private static final int ID_ALERT_BASE       = 2000;
    private static final int ID_PERFORMANCE_BASE = 3000;

    private final Context context;

    public SmartFitNotificationManager(Context context) {
        this.context = context.getApplicationContext();
        createNotificationChannels();
    }

    // ------------------------------------------------------------------ //
    //  Kanal Oluşturma (Android 8+ zorunlu)
    // ------------------------------------------------------------------ //

    private void createNotificationChannels() {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return;

        NotificationManager manager =
                context.getSystemService(NotificationManager.class);

        // Antrenman hatırlatma kanalı
        NotificationChannel workoutChannel = new NotificationChannel(
                CHANNEL_WORKOUT,
                "Antrenman Hatırlatmaları",
                NotificationManager.IMPORTANCE_DEFAULT
        );
        workoutChannel.setDescription(
                "Günlük antrenman saati ve hedef hatırlatmaları."
        );

        // Sağlık uyarısı kanalı (yüksek öncelik)
        NotificationChannel alertChannel = new NotificationChannel(
                CHANNEL_ALERT,
                "Sağlık Uyarıları",
                NotificationManager.IMPORTANCE_HIGH
        );
        alertChannel.setDescription(
                "Nabız eşiği aşımı, sakatlık riski ve aşırı antrenman uyarıları."
        );
        alertChannel.enableVibration(true);
        alertChannel.setVibrationPattern(new long[]{0, 500, 200, 500});

        // Performans bildirim kanalı
        NotificationChannel performanceChannel = new NotificationChannel(
                CHANNEL_PERFORMANCE,
                "Performans Güncellemeleri",
                NotificationManager.IMPORTANCE_LOW
        );
        performanceChannel.setDescription(
                "Haftalık performans özeti ve kişisel rekor bildirimleri."
        );

        manager.createNotificationChannel(workoutChannel);
        manager.createNotificationChannel(alertChannel);
        manager.createNotificationChannel(performanceChannel);
    }

    // ------------------------------------------------------------------ //
    //  Bildirim Göndericileri
    // ------------------------------------------------------------------ //

    /**
     * Günlük antrenman hatırlatma bildirimi.
     *
     * @param title   Bildirim başlığı
     * @param message Bildirim metni
     * @param notifId Benzersiz bildirim ID
     */
    public void sendWorkoutReminder(String title, String message, int notifId) {
        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(context, CHANNEL_WORKOUT)
                        .setSmallIcon(android.R.drawable.ic_media_play)
                        .setContentTitle(title)
                        .setContentText(message)
                        .setPriority(NotificationCompat.PRIORITY_DEFAULT)
                        .setAutoCancel(true);

        NotificationManagerCompat.from(context)
                .notify(ID_WORKOUT_BASE + notifId, builder.build());
    }

    /**
     * Kritik sağlık uyarısı bildirimi (titreşimli, yüksek öncelik).
     *
     * @param alertType Uyarı türü (örn: "HIGH_HEART_RATE", "INJURY_RISK")
     * @param detail    Detay metni
     */
    public void sendHealthAlert(String alertType, String detail) {
        String title = resolveAlertTitle(alertType);

        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(context, CHANNEL_ALERT)
                        .setSmallIcon(android.R.drawable.ic_dialog_alert)
                        .setContentTitle(title)
                        .setContentText(detail)
                        .setStyle(new NotificationCompat.BigTextStyle().bigText(detail))
                        .setPriority(NotificationCompat.PRIORITY_HIGH)
                        .setAutoCancel(true);

        NotificationManagerCompat.from(context)
                .notify(ID_ALERT_BASE + alertType.hashCode(), builder.build());
    }

    /**
     * Haftalık performans özet bildirimi.
     *
     * @param weeklyScore   Haftalık performans skoru (0-100)
     * @param improvementPct Geçen haftaya göre değişim yüzdesi
     */
    public void sendWeeklyPerformanceSummary(int weeklyScore, double improvementPct) {
        String direction = improvementPct >= 0 ? "📈 +" : "📉 ";
        String message   = String.format(
                "Bu haftaki performans skorun: %d/100\n%s%.1f%% değişim.",
                weeklyScore, direction, Math.abs(improvementPct)
        );

        NotificationCompat.Builder builder =
                new NotificationCompat.Builder(context, CHANNEL_PERFORMANCE)
                        .setSmallIcon(android.R.drawable.ic_menu_compass)
                        .setContentTitle("🏆 Haftalık Performans Raporu")
                        .setContentText(message)
                        .setStyle(new NotificationCompat.BigTextStyle().bigText(message))
                        .setPriority(NotificationCompat.PRIORITY_LOW)
                        .setAutoCancel(true);

        NotificationManagerCompat.from(context)
                .notify(ID_PERFORMANCE_BASE, builder.build());
    }

    /**
     * Kişisel rekor bildirimi.
     *
     * @param metricName Kırılan rekor metriği (örn: "5km Koşu")
     * @param newValue   Yeni rekor değeri
     * @param unit       Birim (örn: "dk:sn", "km/s")
     */
    public void sendPersonalRecordAlert(String metricName, double newValue, String unit) {
        String message = String.format(
                "Tebrikler! %s alanında yeni kişisel rekor: %.2f %s 🎉",
                metricName, newValue, unit
        );

        sendWorkoutReminder("🏅 Kişisel Rekor!", message, metricName.hashCode());
    }

    // ------------------------------------------------------------------ //
    //  Yardımcı Metodlar
    // ------------------------------------------------------------------ //

    private String resolveAlertTitle(String alertType) {
        switch (alertType) {
            case "HIGH_HEART_RATE":  return "❤️ Yüksek Nabız Uyarısı";
            case "INJURY_RISK":      return "⚠️ Sakatlık Riski Tespit Edildi";
            case "OVERTRAINING":     return "🛑 Aşırı Antrenman Uyarısı";
            case "LOW_HRV":          return "💤 Yetersiz Toparlanma Uyarısı";
            default:                 return "📢 Sağlık Bildirimi";
        }
    }

    /** Belirtilen kanalın tüm bildirimlerini temizler. */
    public void clearChannel(String channelId) {
        NotificationManagerCompat manager = NotificationManagerCompat.from(context);
        manager.cancelAll();
    }
}
