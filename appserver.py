"""
appserver.py
    - creates an app instance and runs the server 
"""
if __name__ == '__main__':
    from isaapp.application import create_app
    app = create_app()
    app.run()
