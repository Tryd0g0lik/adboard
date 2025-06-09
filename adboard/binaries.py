import base64
import json
import pickle


class Binary:

    def str_to_binary(self, string):
        """Преобразование строки в бинарные данные"""
        try:
            encoded_string = base64.b64encode(string).decode("utf-8")
            return encoded_string
        except UnicodeEncodeError as error:
            raise ValueError(f"Error encode: {error}")

    def object_to_binary(self, obj):
        """
        Here, is used library pickle for a work with a binary and json data.
        Преобразование объекта в бинарные данные"""
        return pickle.dumps(obj)


#     def binary_to_json(self, binary_data):
#         """
#         Here is used library pickle for a work with binary and json data
#         Бинарные данные -> JSON строка"""
#         # Сначала преобразуем бинарные данные в объект
#         obj = pickle.loads(binary_data)
#         # Затем объект в JSON строку
#         return json.dumps(obj, ensure_ascii=False)
#
#     def object_to_binary_json(self, obj):
#         json_str = json.dumps(obj, ensure_ascii=False)
#         return self.str_to_binary(json_str)
#
#     def binary_json_to_object(self, binary_data):
#         json_str = base64.b64decode(binary_data).decode('utf-8')
#         return json.loads(json_str)
#
#     def json_to_binary(self, json_str):
#         """
#         Here, is used library pickle for a work with binary and json data
#         JSON строка -> бинарные данные"""
#         # Сначала преобразуем JSON в объект
#         obj = json.loads(json_str)
#         # Затем объект в бинарные данные
#         return pickle.dumps(obj)
#
#     def binary_to_object(self, binary_data):
#         """Бинарные данные -> исходный объект"""
#         return pickle.loads(binary_data)
#
#
# # Исходный объект (может быть любым: dict, list, класс и т.д.)
# original_object = {
#     "name": "Иван",
#     "age": 30,
#     "items": ["яблоко", "книга", 42],
#     "meta": {"version": 1.1}
# }
