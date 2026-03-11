# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
init python:
    def flash_text(message, duration=2.5, size=60):
        renpy.show('flash_screen',what=Text(message, size=size, color='#FFFFFF', text_align=0.5, yalign=0.5), zorder=1000,layer='screens')
        renpy.pause(duration)
        renpy.hide('flash_screen', layer='screens')

image marta_sell = "marta_sell.jpg"
image cabinet = "cabinet_gilogo_sectora.jpg"
image coridor = "coridor.jpg"
# image kvartira = "" # Квартира
# image lina = "" # Появление Лины
# image perexod = "" # Переход между секторами
# image zal_otrazheniy = "" # зал отражений
# image komnata_bez_vremeniwith = "" # комната без времени
# image perekrestok_mirow = "" # Перекресток миров
# image door_straxa = "" # Дверь страха
# image door_somneniy = "" # Дверь сомнений
# image door_istini = "" # Дверь истины
# image zal_istin = "" # Зал вечных истин
# image open_istini = "" # Открытие истины 
# image pogranichie_mirow = "" # пограничье миров
# image vozvrashenie = "" # Возвращение

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

default swiss_knife_available = False   

# Игра начинается здесь:
label start:
    scene black 
    $ renpy.notify("Громче, чем тишина") # Название игры 
    
    scene arhiv
    show eileen happy

    $ renpy.pause(1.0)

    jump chapter_1