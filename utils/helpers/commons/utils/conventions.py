class Casing:
    @staticmethod
    def convert_title_case_to_snake_casing(str_: str) -> str:
        action_name = ""
        for id_, letter in enumerate(str_):
            if letter.isupper() and id_:
                action_name += "_"
            action_name += letter.lower()
        return action_name

    @staticmethod
    def convert_snake_casing_to_title_casing(str_: str) -> str:
        action_name = ""
        for id_, letter in enumerate(str_):
            if not id_:
                action_name += letter.upper()
            elif id_ and letter == "_":
                action_name += ""
            elif id_ and str_[id_ - 1] == "_":
                action_name += letter.upper()
            else:
                action_name += letter.lower()
        return action_name

    @staticmethod
    def convert_list_of_title_casing_to_joined_snake_casing(list_of_class_names):
        converted_items = []
        for class_name in list_of_class_names:
            converted_items.append(
                Casing.convert_title_case_to_snake_casing(class_name)
            )
        return "__".join(converted_items)

    @staticmethod
    def convert_joined_snake_casing_to_list_of_title_casing(joined_snake_casing_str):
        splitted_str = joined_snake_casing_str.split("__")
        list_title_casing = []
        for str_ in splitted_str:
            list_title_casing.append(Casing.convert_snake_casing_to_title_casing(str_))
        return list_title_casing
