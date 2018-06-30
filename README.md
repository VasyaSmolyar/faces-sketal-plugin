# faces-sketal-plugin
Плагин для наложения множества фильтров на лица для Вк бота Sketal https://github.com/vk-brain/sketal, также основывается на этом проекте https://github.com/vasilysinitsin/Faces
# Установка
1. Установите Sketal по его инструкции
2. Скачайте файлы плагина и перекиньте папку faces-sketal-plugin в папку plugins бота
3. Переименуйте папку faces-sketal-plugin в faces
4. В settings.py бота добавить строчку
```
from plugins.faces.faces_plugin import FacesPlugin
```
5. В settings.py бота в PLUGINS добавить строчку
```
 FacesPlugin("{тут желаемая команда}", prefixes=prefixes),
```
