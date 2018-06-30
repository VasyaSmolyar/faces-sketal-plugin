from handler.base_plugin_command import CommandPlugin
from .faces_core import faces
from vk.helpers import upload_photo


class FacesPlugin(CommandPlugin):
    __slots__ = ('names')

    def __init__(self, *commands, prefixes=None, strict=False):
        super().__init__(*commands, prefixes=prefixes, strict=strict)
        self.names = { 'улыбку': 'smile_2',

        'весёлой': 'smile',
        'весёлым': 'smile',
        'весело': 'smile',

        'старым': 'old',
        'старой': 'old',

        'молодым': 'young',
        'молодой': 'young',

        'мужчиной': 'male',
        'мужиком': 'male',
        'парнем': 'male',
        'поцем': 'male',

        'женщиной': 'female',
        'тёлкой': 'female',
        'тётей': 'female_2',
        'кисой': 'female_2',
        "хитменом": "hitman",
        "очкариком": "fun_glasses",
        "усатым": "mustache_free",
        "паном": "pan",
        "хайзенбергом": "heisenberg",
        "красивым": "hot",
        "звездой": "hollywood"}

    async def process_message(self, msg):
        command, text = self.parse_message(msg)
        if not text or text not in self.filters.keys():
            return await msg.answer('Список доступных фильтров:\n' + ", ".join(self.names))

        if not any(k.endswith('_type') and v == "photo"
            for k, v in msg.brief_attaches.items()):
                return await msg.answer('Вы не прислали фото!')

        photo_url = None
        for a in await msg.get_full_attaches():
            if a.type == "photo" and a.url:
                photo_url = a.url
                break
        else:
            return await msg.answer('Для работы необходимо прикрепить фото.')
        try:
            image = faces.FaceAppImage(url=photo_url)
            new_image = image.apply_filter(self.names[text])
            at = await upload_photo(self.api, new_image)
            if not at:
                return await msg.answer("Не удалось отправить картинку.")
            return await msg.answer("Вот результат", attachment=at)
        except (faces.BadFilterID,KeyError):
            return await msg.answer("Такого фильтра нет.")
        except faces.ImageHasNoFaces:
            return await msg.answer("На фото нет лица.")
        except faces.BaseFacesException:
            return await msg.answer("Ошибка, возможно стоит прикрепить другую фотографию")
        