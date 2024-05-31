from dataclasses import dataclass


@dataclass
class DataCompany:
    main: str
    goal: str
    relationship: str
    values: str
    achievements: str
    offer: str


@dataclass
class DataSearchWithFilter:
    python: str


data_company = DataCompany(
    main='Yellow - молодая компания, которая занимается разработкой мобильных приложений, облачных систем, а также систем с использованием AI и машинного обучения',
    goal='Наш главный ориентир',
    relationship='Такого же отношения',
    values='Наши ценности',
    achievements='Наши достижения',
    offer='компания предлагает соискателям'
)

data_search_with_filter = DataSearchWithFilter(
    python='Python'
)
