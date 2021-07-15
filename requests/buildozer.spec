[app]

title = KivyMD Travel App
package.name = KivyMDTravelApp
package.domain = org.KivyMDTravelApp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,jpeg,jpg
version = 0.1
requirements = python3,kivy==2.0.0,https://github.com/kivymd/KivyMD/archive/master.zip,pygments,sdl2_ttf==2.0.15,pillow,numpy,matplotlib
#,requests,urllib3
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.presplash_color = #FFFFFF
android.accept_sdk_license = True
android.arch = armeabi-v7a
#ios.kivy_ios_url = https://github.com/kivy/kivy-ios
#ios.kivy_ios_branch = master
#ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
#ios.ios_deploy_branch = 1.7.0
android.permissions = INTERNET 

[buildozer]

log_level = 2
warn_on_root = 1



#[app]

#title = KivyMD Kitchen Sink
#package.name = kitchen_sink
#package.domain = org.kivymd
#source.dir = .
#source.include_exts = py,png,jpg,jpeg,ttf,kv,json,txt
#source.include_patterns = assets/*
#version = 0.1
#android.numeric_version = 1
#requirements = kivy==2.0.0, kivymd==0.104.2, sdl2_ttf == 2.0.15, pillow
#orientation = portrait
#fullscreen = 1
#android.presplash_color = #FFFFFF
#android.permissions = WRITE_EXTERNAL_STORAGE
#android.api = 28
#android.minapi = 21
#android.ndk = 19b
#android.skip_update = False
#android.accept_sdk_license = True
#android.arch = armeabi-v7a


#[buildozer]

#log_level = 2
#warn_on_root = 0
#build_dir = ./.buildozer
#bin_dir = ./bin
