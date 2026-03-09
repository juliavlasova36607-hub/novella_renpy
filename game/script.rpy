# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
init python:
    def flash_text(message, duration=2.5, size=60):
        renpy.show('flas_screen',what=Text(message, size=size, color='#FFFFFF', text_align=0.5, yalign=0.5), zorder=1000,layer='screens')
        renpy.pause(duration)
        renpy.hide('flash_screen', layer='screens')

define systemVoice = Character('системный голос', color="#008080")
define e = Character('...', color= "#FFFFFF")
define marta = Character('Марта Селл', color= "#FFB6C1" )
define aren = Character('Арен', color= "#0000CD" )
define lina = Character('Лина Краус', color = "#F08080")
define iris = Character('Ирис Вальд', color= "#F")

image marta_sell = "marta_sell.jpg"
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