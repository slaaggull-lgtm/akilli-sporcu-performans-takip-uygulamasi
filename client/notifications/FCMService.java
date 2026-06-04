package com.sporcu.akillitakip.notifications;

import android.util.Log;

import com.google.firebase.messaging.FirebaseMessagingService;
import com.google.firebase.messaging.RemoteMessage;

import java.util.Map;

/**
 * Firebase Cloud Messaging (FCM) servis sınıfı.
 * Sunucudan gelen push bildirimlerini yakalar ve
 * SmartFitNotificationManager üzerinden kullanıcıya iletir.
 *
 * Manifest'e eklenecek servis tanımı:
 * <service android:name=".notifications.FCMService"
 *     android:exported="false">
 *   <intent-filter>
 *     <action android:name="com.google.firebase.MESSAGING_EVENT"/>
 *   </intent-filter>
 * </service>
 */
public class FCMService extends FirebaseMessagingService {

    private static final String TAG = "FCMService";

    // FCM payload anahtar sabitleri
    private static final String KEY_ALERT_TYPE = "alert_type";
    private static final String KEY_DETAIL     = "detail";
    private static final String KEY_SCORE      = "weekly_score";
    private static final String KEY_IMPROVEMENT= "improvement_pct";

    @Override
    public void onNewToken(String token) {
        super.onNewToken(token);
        Log.d(TAG, "FCM Token yenilendi: " + token);
        // Token'ı backend'e gönder (REST API /users/fcm-token endpoint'i)
        sendTokenToServer(token);
    }

    @Override
    public void onMessageReceived(RemoteMessage remoteMessage) {
        super.onMessageReceived(remoteMessage);

        Map<String, String> data = remoteMessage.getData();
        if (data.isEmpty()) {
            Log.w(TAG, "Boş FCM mesajı alındı, işlenmiyor.");
            return;
        }

        SmartFitNotificationManager notifManager =
                new SmartFitNotificationManager(this);

        String alertType = data.getOrDefault(KEY_ALERT_TYPE, "GENERAL");

        switch (alertType) {
            case "HIGH_HEART_RATE":
            case "INJURY_RISK":
            case "OVERTRAINING":
            case "LOW_HRV":
                String detail = data.getOrDefault(KEY_DETAIL,
                        "Sağlık verilerinizi kontrol edin.");
                notifManager.sendHealthAlert(alertType, detail);
                break;

            case "WEEKLY_SUMMARY":
                try {
                    int    score       = Integer.parseInt(
                            data.getOrDefault(KEY_SCORE, "0"));
                    double improvement = Double.parseDouble(
                            data.getOrDefault(KEY_IMPROVEMENT, "0.0"));
                    notifManager.sendWeeklyPerformanceSummary(score, improvement);
                } catch (NumberFormatException e) {
                    Log.e(TAG, "Haftalık özet verisi parse edilemedi: " + e.getMessage());
                }
                break;

            default:
                Log.d(TAG, "Bilinmeyen alert_type: " + alertType);
        }
    }

    private void sendTokenToServer(String token) {
        // Retrofit veya OkHttp ile backend'e POST /users/fcm-token
        // Gerçek implementasyon için WorkManager kullanılacak.
        Log.d(TAG, "Token sunucuya gönderildi (simüle): " + token.substring(0, 10) + "...");
    }
}
