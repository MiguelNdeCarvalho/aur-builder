from ui import create_app
from flask_toastr import Toastr

app = create_app()

toastr = Toastr(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
