from pynput import keyboard
import FileAccess
import TypeToWord
import time

def main():
    
    city_file = FileAccess.NewFile("CityList.dat", 0, "")
    city_file.get_content()
    total_cities = city_file.get_len()

    time.sleep(5)
    for each in range(total_cities-1):
        wordMaker(city_file.get_string())

def split(word):
    word = word.replace("\n", "")
    word = word.replace(" ", "")
    return [char for char in word]

def wordMaker(city):
    c_keyboard = TypeToWord.Keys(' ')
    
    abbs_file = FileAccess.NewFile("abbs.dat", 0, "")
    abbs_file.get_content()
    total_abbs = abbs_file.get_len()

    new_city = split(city)
    

    c_pressed = 0
    

    for y in range(49):
        for x in new_city:
            c_pressed += 1
            c_keyboard.c_key = x
            c_keyboard.input_key()
            if c_pressed == len(new_city):
                c_pressed = 0
                for n in abbs_file.get_string():
                    c_keyboard.c_key = n
                    c_keyboard.input_key()
        c_keyboard.enter()
        time.sleep(0.01)

main()