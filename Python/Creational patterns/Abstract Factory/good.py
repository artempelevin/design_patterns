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


class MSProjectFileGenerator(ABC):
    @abstractmethod
    def provide_calendars(self) -> MSProjectCalendars:
        pass

    @abstractmethod
    def provide_tasks(self) -> MSProjectTasks:
        pass


class MSProjectXmlFileGenerator(MSProjectFileGenerator):
    def provide_calendars(self) -> MSProjectCalendars:
        return MSProjectXmlCalendars()

    def provide_tasks(self) -> MSProjectTasks:
        return MSProjectXmlTasks()


class MSProjectJsonFileGenerator(MSProjectFileGenerator):
    def provide_calendars(self) -> MSProjectCalendars:
        return MSProjectJsonCalendars()

    def provide_tasks(self) -> MSProjectTasks:
        return MSProjectJsonTasks()


def generate_ms_project_file(ms_project_generator: MSProjectFileGenerator) -> str:
    return ms_project_generator.provide_calendars().provide_content() + \
           ms_project_generator.provide_tasks().provide_content()


def main() -> None:
    ms_project_xml_file = generate_ms_project_file(ms_project_generator=MSProjectXmlFileGenerator())
    print(f"MS Project File (XML):\n"
          f"{ms_project_xml_file}")

    ms_project_json_file = generate_ms_project_file(ms_project_generator=MSProjectJsonFileGenerator())
    print(f"MS Project File (JSON):\n"
          f"{ms_project_json_file}")


if __name__ == '__main__':
    main()
