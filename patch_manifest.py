path = 'android/app/src/main/AndroidManifest.xml'
src = open(path, encoding='utf-8').read()

needed = [
    'android.permission.INTERNET',
    'android.permission.ACCESS_FINE_LOCATION',
    'android.permission.ACCESS_COARSE_LOCATION',
    'android.permission.CHANGE_WIFI_MULTICAST_STATE',
]

for perm in needed:
    if perm not in src:
        tag = f'<uses-permission android:name="{perm}" />'
        src = src.replace('<application', tag + '\n    <application', 1)

open(path, 'w', encoding='utf-8').write(src)
print('Manifest patched: разрешения добавлены')