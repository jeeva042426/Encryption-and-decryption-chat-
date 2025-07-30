from flask import Flask, render_template, request
from cryptography.fernet import Fernet
from ciphers import rail_fence, row_transposition

app = Flask(__name__)

# Generate symmetric key (for future use if needed)
fernet_key = Fernet.generate_key()
cipher_suite = Fernet(fernet_key)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None  # Ensure no empty result box on first load

    if request.method == 'POST':
        message = request.form.get('message', '').strip()
        mode = request.form.get('mode')
        cipher = request.form.get('cipher')

        if cipher == 'rail_fence':
            try:
                rails = int(request.form.get('rails', 3))
                if mode == 'encrypt':
                    result = rail_fence.encrypt(message, rails)
                else:
                    result = rail_fence.decrypt(message, rails)
            except Exception as e:
                result = f"Error: {str(e)}"
        elif cipher == 'row_transposition':
            key = request.form.get('key', '').strip()
            if not key or not key.isdigit() or len(set(key)) != len(key):
                result = "Please provide a valid numeric key with unique digits for Row Transposition."
            else:
                try:
                    if mode == 'encrypt':
                        result = row_transposition.encrypt(message, key)
                    else:
                        result = row_transposition.decrypt(message, key)
                except Exception as e:
                    result = f"Error during Row Transposition: {str(e)}"


    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
