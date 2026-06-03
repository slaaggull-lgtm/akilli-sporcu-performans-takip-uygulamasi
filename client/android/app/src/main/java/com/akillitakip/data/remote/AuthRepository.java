package com.akillitakip.data.remote;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

/**
 * Firebase kimlik dogrulama islemlerini yoneten depo sinifi.
 *
 * MVVM mimarisinde bu sinif tek Firebase erisim noktasidir.
 * ViewModel bu sinifi dogrudan cagirarak UI'dan ayrilir.
 */
public class AuthRepository {

    private final FirebaseAuth mAuth;

    public AuthRepository() {
        this.mAuth = FirebaseAuth.getInstance();
    }

    /**
     * Kullanici girisi yapar.
     *
     * @param email    Kullanici e-postasi
     * @param password Sifre
     * @param listener Sonuc dinleyicisi
     */
    public void loginUser(String email, String password, OnAuthCompleteListener listener) {
        mAuth.signInWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        listener.onSuccess(mAuth.getCurrentUser());
                    } else {
                        String errorMsg = task.getException() != null
                                ? task.getException().getMessage()
                                : "Bilinmeyen hata";
                        listener.onError(errorMsg);
                    }
                });
    }

    /**
     * Yeni kullanici kaydeder.
     *
     * @param email    E-posta
     * @param password Sifre (en az 6 karakter)
     * @param listener Sonuc dinleyicisi
     */
    public void registerUser(String email, String password, OnAuthCompleteListener listener) {
        mAuth.createUserWithEmailAndPassword(email, password)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        listener.onSuccess(mAuth.getCurrentUser());
                    } else {
                        String errorMsg = task.getException() != null
                                ? task.getException().getMessage()
                                : "Kayit basarisiz";
                        listener.onError(errorMsg);
                    }
                });
    }

    /**
     * Mevcut oturum acik kullaniciya erisir.
     *
     * @return Oturum acik kullanici, yoksa null
     */
    public FirebaseUser getCurrentUser() {
        return mAuth.getCurrentUser();
    }

    /** Kullanicinin oturumunu kapatir. */
    public void signOut() {
        mAuth.signOut();
    }

    /**
     * Firebase kimlik dogrulama geri donus arayuzu.
     * Basarili ve hatali durumlari ayirir.
     */
    public interface OnAuthCompleteListener {
        void onSuccess(FirebaseUser user);
        void onError(String errorMessage);
    }
}
