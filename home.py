from flask import Flask, render_template_string
from select_nuclides import load_isotopes

app = Flask(__name__)


@app.route('/')
def index():
    """Display the home page with a link to NUBASE and the isotope list."""
    return render_template_string(
        """
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <title>Neutron Reaction Home</title>
        </head>
        <body>
            <h1>Neutron Reaction</h1>
            <p>This project uses data from <a href='https://www-nds.iaea.org/nubase/nubase2020.htm' target='_blank'>NUBASE</a> to read properties of isotopes.</p>
            <p><a href='/isotopes'>Select Isotopes</a></p>
        </body>
        </html>
        """
    )


@app.route('/isotopes')
def isotopes():
    """Render the isotope selection page using the list from the JSON file."""
    isotopes_list = load_isotopes()
    items = '\n'.join(f"<li>{name}</li>" for name in isotopes_list)
    return render_template_string(
        f"""
        <!DOCTYPE html>
        <html lang='en'>
        <head>
            <meta charset='UTF-8'>
            <title>Isotope Selection</title>
        </head>
        <body>
            <h1>Select an Isotope</h1>
            <ul>
                {items}
            </ul>
        </body>
        </html>
        """
    )


if __name__ == '__main__':
    app.run(debug=True)
