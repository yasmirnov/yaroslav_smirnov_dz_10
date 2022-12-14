from flask import Flask

from utils import load_candidates, get_by_pk, get_candidates_all, get_by_skill

app = Flask(__name__)


@app.route("/")
def page_main():
    """
    Главная страница
    """
    candidates = get_candidates_all()
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


@app.route("/candidate/<int:pk>")
def page_profile(pk):
    """
    Показывает кандидата по id(pk)
    """
    candidate = get_by_pk(pk)
    if not candidate:
        return 'Кандидат не найден'
    else:
        result = f'<img src=\'{candidate["picture"]}\'>' + '<br>'
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
        return f'<pre> {result} </pre>'


@app.route("/candidate/<skill>")
def get_candidate_by_skills(skill):
    """
    Показывает список кандидатов по навыку
    """
    candidates = get_by_skill(skill)
    result = '<br>'
    for candidate in candidates:
        result += candidate["name"] + '<br>'
        result += candidate["position"] + '<br>'
        result += candidate["skills"] + '<br>'
        result += '<br>'
    return f'<pre> {result} </pre>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
