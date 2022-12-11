from flask import Flask

from utils import load_candidates

app = Flask(__name__)


@app.route("/")
def page_main():
    """Главная страница"""
    candidates = load_candidates()
    result = '<pre>'

    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
        result += '</pre>'
        return result


app.run()
