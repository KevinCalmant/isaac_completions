"""
appserver.py
    - Creates an app instance andd runs the dev serv
"""
if __name__ == '__main__':
    from isaapi.application import create_app
    app = create_app()
    app.run()
