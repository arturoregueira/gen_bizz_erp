from app import create_app

theapp = create_app()

if __name__ == "__main__":

    theapp.run(
        host='0.0.0.0',  # Allows the app to be accessible externally, not just localhost
        port=5000,       # Specifies the port number to run the server (default is 5000)
        debug=True,      # Enables debug mode for automatic reloads and better error messages
        #threaded=True,   # Enables handling multiple requests concurrently
        #use_reloader=True,  # Ensures the app reloads upon code changes
    )

#nothing should be here!!!