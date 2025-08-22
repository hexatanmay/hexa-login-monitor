# Define the path for saving the image and log
$imagePath = "C:\Users\Administrator\Downloads\python\monitor failed login\security_logs\save\snapshot_$((Get-Date).ToString('yyyyMMdd_HHmmss')).jpg"
$logPath = "C:\Users\Administrator\Downloads\python\monitor failed login\security_logs\log.txt"

# Capture the image using FFmpeg
Start-Process -FilePath "C:\ffmpeg\bin\ffmpeg.exe" -ArgumentList "-f dshow -i video=""Integrated Webcam"" -vframes 1 `"$imagePath`""

# Log the event
$logEntry = "Failed login attempt at $(Get-Date). Image saved as $(Split-Path $imagePath -Leaf)"
Add-Content -Path $logPath -Value $logEntry