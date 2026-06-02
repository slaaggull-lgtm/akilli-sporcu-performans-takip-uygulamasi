package com.akillitakip.presentation;

import com.google.firebase.auth.FirebaseUser;

/**
 * Kimlik dogrulama durum modeli.
 *
 * Sealed class benzeri Java yaklasimi.
 * ViewModel bu sinifi LiveData ile gozlemlenerek UI'a iletir.
 *
 * Durumlar:
 *   IDLE    — Beklemede, henuz islem yok
 *   LOADING — Islem devam ediyor (ProgressBar gosterilir)
 *   SUCCESS — Basarili (Dashboard'a yonlendir)
 *   ERROR   — Hata (Snackbar goster)
 */
public class AuthState {

    public enum Status {
        IDLE, LOADING, SUCCESS, ERROR
    }

    private final Status status;
    private final String errorMessage;
    private final FirebaseUser user;

    private AuthState(Status status, String errorMessage, FirebaseUser user) {
        this.status = status;
        this.errorMessage = errorMessage;
        this.user = user;
    }

    // --- Fabrika Metodlari ---

    public static AuthState idle() {
        return new AuthState(Status.IDLE, null, null);
    }

    public static AuthState loading() {
        return new AuthState(Status.LOADING, null, null);
    }

    public static AuthState success(FirebaseUser user) {
        return new AuthState(Status.SUCCESS, null, user);
    }

    public static AuthState error(String message) {
        return new AuthState(Status.ERROR, message, null);
    }

    // --- Getter'lar ---

    public Status getStatus() { return status; }
    public String getErrorMessage() { return errorMessage; }
    public FirebaseUser getUser() { return user; }
    public boolean isLoading() { return status == Status.LOADING; }
    public boolean isSuccess() { return status == Status.SUCCESS; }
    public boolean isError() { return status == Status.ERROR; }
}
