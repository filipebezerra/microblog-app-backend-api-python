from app import app

if __name__ == "__main__":
    app.run(
        debug=True,
        use_reloader=False,
        use_debugger=False,
        passthrough_errors=True
    )