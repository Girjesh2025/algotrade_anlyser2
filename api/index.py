from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AlgoTrade Analyzer</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; }
            h1 { color: #333; }
            .container { border: 1px solid #ddd; padding: 20px; border-radius: 5px; }
            .info { background-color: #e9f7fe; padding: 15px; border-radius: 5px; margin-bottom: 20px; }
            .button { display: inline-block; background: #0066cc; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; }
        </style>
    </head>
    <body>
        <h1>AlgoTrade Analyzer</h1>
        <div class="info">
            <p>This Streamlit app cannot run directly on Vercel. Please use one of the options below:</p>
        </div>
        <div class="container">
            <h2>Option 1: Run the app locally</h2>
            <p>Clone the repository and run it on your local machine:</p>
            <pre>git clone https://github.com/Girjesh2025/algotrade_anlyser2.git
cd algotrade_anlyser2
pip install -r requirements.txt
streamlit run app.py</pre>
            
            <h2>Option 2: Deploy on Streamlit Cloud</h2>
            <p>Streamlit Cloud is designed specifically for Streamlit apps and offers free hosting:</p>
            <a href="https://share.streamlit.io/" class="button">Deploy on Streamlit Cloud</a>
            
            <h2>Option 3: View the source code</h2>
            <p>Check out the GitHub repository:</p>
            <a href="https://github.com/Girjesh2025/algotrade_anlyser2" class="button">View on GitHub</a>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
