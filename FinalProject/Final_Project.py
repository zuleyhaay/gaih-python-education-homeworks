info_dict = {}


def add_language(name, language_list, language):
    language_list.append(language)
    new_dict = {name: language_list}
    info_dict.update(new_dict)
    return info_dict


def list_languages(name, languages):
    print(name, "can speak these languages:", end=" ")
    for language in languages:
        print(language,end=" ")
    print("\n")


class Employee:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


class Manager:
    def __init__(self, name, age, language):
        self.name = name
        self.age = age
        self.language = language


if __name__ == '__main__':
    Luna = Employee("Luna", 23, ["French", "English", "Turkish"])
    update_dict = add_language("Luna", Luna.language, "German")
    list_languages("Luna", update_dict.get("Luna"))
    Stephan = Employee("Stephan", 28, ["French", "Italian"])
    update_dict = add_language("Stephan", Stephan.language, "Portuguese")
    list_languages("Stephan", update_dict.get("Stephan"))
