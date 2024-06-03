import keyboard

def klavye_takip():
    print("Klavye takip başladı. İzlemeyi sonlandırmak için 'q' tuşuna basın.")
    while True:
        try:
            tus = keyboard.read_event()
            if tus.event_type == keyboard.KEY_DOWN:
                print(f"Tuş: {tus.name}")
                if tus.name == "q":
                    print("İzleme sonlandırıldı.")
                    break
        except KeyboardInterrupt:
            break

klavye_takip()
