import json

CANDIDATES_FILE = "candidates.json"


def load_candidates() -> list[dict]:
    with open(CANDIDATES_FILE, "r") as file:
        return json.load(file)


def get_candidates_all():
    """
    получает всех кандидатов
    """
    return load_candidates()


def get_by_pk(pk):
    """
    возвращает кандидата по pk
    """
    for candidate in load_candidates():
        if int(pk) == candidate["pk"]:
            return candidate
    return None


def get_by_skill(skill_name) -> list:
    """
    возвращает кандидатов по навыку
    """
    candidates = []
    for data_candidate in load_candidates():
        if skill_name.lower() in data_candidate["skills"].lower().split(', '):
            candidates.append(data_candidate)
    return candidates
