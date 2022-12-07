import json

CANDIDATES_FILE = "candidates.json"


def load_candidates() -> list[dict]:
    """
    загружает данные из файла
    """
    with open(CANDIDATES_FILE, "r") as file:
        candidates_file = json.load(file)
        return candidates_file


def get_all():
    """
    получает всех кандидатов
    """
    for i in load_candidates():
        print(i["name"])


def get_by_pk(pk) -> dict:
    """
    возвращает кандидата по pk
    """
    for candidate in load_candidates():
        if int(pk) == candidate["pk"]:
            return candidate


def get_by_skill(skill_name) -> list[dict]:
    """
    возвращает кандидатов по навыку
    """
    candidates = []
    for data_candidate in load_candidates():
        if skill_name.lower() in data_candidate["skills"].lower():
            candidates.append(data_candidate)
    return candidates
