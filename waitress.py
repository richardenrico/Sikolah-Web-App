from sikolah import app
import waitress

if __name__ == "__main__":
    port = int(os.eniron.get('PORT', 33507))
    waitress.server(app, port=port)
