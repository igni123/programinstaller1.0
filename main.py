# created by igni
# 2024.04.16
import subprocess
import os
username = os.environ.get('USERNAME')
folder_name = ".programinstaller"
exe_paths = [
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\bdcamsetup.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\ChromeSetup.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\EV3_Classroom_Windows_1.5.3_Global.msi',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\Flowgorithm.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\GeoGebraCalculator-Windows-Installer-6-0-836-0.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\Install_LapodaTale21_449.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\kdenlive-24.02.2.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\OBS-Studio-30.1.2-Full-Installer-x64.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\PhotoScapeSetup_V3-7.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\RoboMindSetup7.0.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\Scratch 3.29.1 Setup.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\SmallBasic_v1.2.msivlc-3.0.20-win64.exe',
    rf'C:\Users\{username}\Desktop\{folder_name}\exes\vlc-3.0.20-win64.exe'
]
for exe_path in exe_paths:
    try:
        subprocess.run([exe_path], check=True)
        print(f"Installation of {exe_path} successful!")
    except subprocess.CalledProcessError as e:
        print(f"Installation of {exe_path} failed with error code {e.returncode}")
while True:
    user_input = input()
    if user_input == "":
        print("Exiting...")
        break
