from colorama import init

print('\033[31m' + 'красный текст')
print('\033[39m') # сброс к цвету по умолчанию

from colorama import Fore, Back, Style
print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне')
print(Style.BRIGHT + 'стал ярче' + Style.RESET_ALL)
print('обычный текст')

rom colorama import init
from termcolor import colored

# используйте Colorama, чтобы Termcolor работал и в Windows
init()

# теперь вы можете применять Termcolor для вывода
# вашего цветного текста
print(colored('Termcolor and Colorama!', 'red', 'on_yellow')

init(autoreset=True)
print(Fore.GREEN + 'зеленый текст')
print('автоматический возврат к обычному')