import colorama

colorama.init()

print("Атрибути модуля colorama:")
print(dir(colorama))

print("Документация модуля colorama:")
print(help(colorama))

print(colorama.Back.GREEN + "Hello Python" + colorama.Style.RESET_ALL)
