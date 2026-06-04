package com.sporcu.akillitakip.notifications;

import android.content.Context;

import androidx.work.Data;
import androidx.work.ExistingPeriodicWorkPolicy;
import androidx.work.OneTimeWorkRequest;
import androidx.work.PeriodicWorkRequest;
import androidx.work.WorkManager;
import androidx.work.Worker;
import androidx.work.WorkerParameters;

import java.util.concurrent.TimeUnit;

/**
 * WorkManager tabanlı bildirim zamanlayıcısı.
 * Günlük antrenman hatırlatmalarını ve haftalık
 * performans özetlerini arka planda zamanlar.
 */
public class NotificationScheduler {

    private static final String WORK_DAILY_REMINDER  = "daily_workout_reminder";
    private static final String WORK_WEEKLY_SUMMARY  = "weekly_performance_summary";

    private final Context context;

    public NotificationScheduler(Context context) {
        this.context = context.getApplicationContext();
    }

    /**
     * Günlük antrenman hatırlatmasını zamanlar (24 saatte bir tekrar).
     *
     * @param hour    Bildirim saati (0-23)
     * @param message Hatırlatma metni
     */
    public void scheduleDailyWorkoutReminder(int hour, String message) {
        Data inputData = new Data.Builder()
                .putString("message", message)
                .putInt("hour", hour)
                .build();

        PeriodicWorkRequest workRequest =
                new PeriodicWorkRequest.Builder(
                        DailyReminderWorker.class,
                        24, TimeUnit.HOURS
                )
                .setInputData(inputData)
                .build();

        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
                WORK_DAILY_REMINDER,
                ExistingPeriodicWorkPolicy.REPLACE,
                workRequest
        );
    }

    /**
     * Haftalık performans özeti bildirimine zamanlar (7 günde bir).
     */
    public void scheduleWeeklyPerformanceSummary() {
        PeriodicWorkRequest weeklyWork =
                new PeriodicWorkRequest.Builder(
                        WeeklySummaryWorker.class,
                        7, TimeUnit.DAYS
                )
                .build();

        WorkManager.getInstance(context).enqueueUniquePeriodicWork(
                WORK_WEEKLY_SUMMARY,
                ExistingPeriodicWorkPolicy.KEEP,
                weeklyWork
        );
    }

    /** Tüm zamanlanmış bildirimleri iptal eder. */
    public void cancelAll() {
        WorkManager.getInstance(context).cancelAllWork();
    }

    // ------------------------------------------------------------------ //
    //  Worker Sınıfları
    // ------------------------------------------------------------------ //

    public static class DailyReminderWorker extends Worker {

        public DailyReminderWorker(Context ctx, WorkerParameters params) {
            super(ctx, params);
        }

        @Override
        public Result doWork() {
            String message = getInputData().getString("message");
            if (message == null) message = "Bugünkü antrenmanını tamamlamayı unutma! 💪";

            SmartFitNotificationManager manager =
                    new SmartFitNotificationManager(getApplicationContext());
            manager.sendWorkoutReminder(
                    "🏋️ Antrenman Zamanı!", message, (int) System.currentTimeMillis()
            );
            return Result.success();
        }
    }

    public static class WeeklySummaryWorker extends Worker {

        public WeeklySummaryWorker(Context ctx, WorkerParameters params) {
            super(ctx, params);
        }

        @Override
        public Result doWork() {
            // Gerçek uygulamada Room DB'den haftalık skor çekilir.
            // Şimdilik sabit örnek değerlerle çalışıyor.
            SmartFitNotificationManager manager =
                    new SmartFitNotificationManager(getApplicationContext());
            manager.sendWeeklyPerformanceSummary(78, +12.5);
            return Result.success();
        }
    }
}
