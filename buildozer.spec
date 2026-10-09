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

orientation = portrait
