from abc import ABC, abstractmethod


class MSProjectCalendars(ABC):
    @abstractmethod
    def provide_content(self) -> str:
        pass


class MSProjectXmlCalendars(MSProjectCalendars):
    def provide_content(self) -> str:
        return "<Calendars>\n" \
               "    Some info....\n" \
               "</Calendars>\n"


class MSProjectJsonCalendars(MSProjectCalendars):
    def provide_content(self) -> str:
        return '"calendars": "Some info..."\n'


class MSProjectTasks(ABC):
    @abstractmethod
    def provide_content(self) -> str:
        pass


class MSProjectXmlTasks(MSProjectTasks):
    def provide_content(self) -> str:
        return "<Tasks>\n" \
               "    Some info....\n" \
               "</Tasks>\n"


class MSProjectJsonTasks(MSProjectTasks):
    def provide_content(self) -> str:
        return '"tasks": "Some info..."\n'


def generate_ms_project_file(file_type: str) -> str:
    if file_type == 'xml':
        return _generate_ms_project_xml_file()
    elif file_type == 'json':
        return _generate_ms_project_json_file()
    raise ValueError('Unknown file type')


def _generate_ms_project_xml_file() -> str:
    return MSProjectXmlCalendars().provide_content() + \
           MSProjectXmlTasks().provide_content()


def _generate_ms_project_json_file() -> str:
    return MSProjectJsonCalendars().provide_content() + \
           MSProjectJsonTasks().provide_content()


def main() -> None:
    ms_project_xml_file = generate_ms_project_file(file_type='xml')
    print(f"MS Project File (XML):\n"
          f"{ms_project_xml_file}")

    ms_project_json_file = generate_ms_project_file(file_type='json')
    print(f"MS Project File (JSON):\n"
          f"{ms_project_json_file}")


if __name__ == '__main__':
    main()
