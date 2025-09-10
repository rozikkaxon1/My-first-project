import random
import time

def intro():
    print("="*50)
    print("    🎯 SON TOPISH O‘YINIGA XUSH KELIBSIZ! 🎯")
    print("="*50)
    print("Men 1 dan 100 gacha bir son o‘ylayman.")
    print("Siz esa uni topishga harakat qilasiz.")
    print("Har bir noto‘g‘ri urinishdan so‘ng men sizga yordam beraman.")
    print("Boshladik!\n")
    time.sleep(1)

def get_user_guess():
    while True:
        guess = input("Tahminingizni kiriting (1-100): ")
        if guess.isdigit():
            return int(guess)
        else:
            print("⚠️ Faqat son kiriting iltimos.")

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guess_history = []

    while True:
        guess = get_user_guess()
        attempts += 1
        guess_history.append(guess)

        if guess < secret_number:
            print("🔻 Juda kichik son. Yana urinib ko‘ring.\n")
        elif guess > secret_number:
            print("🔺 Juda katta son. Yana urinib ko‘ring.\n")
        else:
            print(f"🎉 Tabriklaymiz! Siz to‘g‘ri topdingiz: {secret_number}")
            print(f"🔢 Urinishlar soni: {attempts}")
            print(f"📜 Sizning taxminlaringiz: {guess_history}")
            break

def main():
    intro()
    play_game()

    while True:
        choice = input("\n🔁 Yana o‘ynaysizmi? (ha/yo‘q): ").strip().lower()
        if choice == "ha":
            print("\n♻️ Qayta boshlayapmiz...\n")
            time.sleep(1)
            play_game()
        elif choice == "yo‘q":
            print("👋 Rahmat! O‘yin tugadi.")
            break
        else:
            print("⚠️ Iltimos, 'ha' yoki 'yo‘q' deb javob bering.")

# Dastur boshlanishi
if __name__ == "__main__":
    main()
