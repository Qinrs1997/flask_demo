from apps import create_app


app = create_app()



if __name__ == '__main__':
    # app.run(host='127.0.0.1',port=5000)
    server = pywsgi.WSGIServer(('0.0.0.0', 5000), app)
    server.serve_forever()