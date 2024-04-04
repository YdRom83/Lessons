from view import app

class Run:
    @staticmethod
    def run_app():
        app.run(debug=True)