[app]
title = Jarvis
package.name = jarvis
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

requirements = python3,kivy,plyer,requests,jnius

android.permissions = INTERNET, RECORD_AUDIO, WAKE_LOCK, FOREGROUND_SERVICE
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.skip_update = False
android.build_tools_version = 34.0.0
android.ndk = 25b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b

orientation = portrait
