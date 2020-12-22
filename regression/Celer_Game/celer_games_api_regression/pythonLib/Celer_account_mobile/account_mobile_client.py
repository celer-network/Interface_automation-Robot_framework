def test_run():
    with open('server.crt', 'rb') as f:
        certificate_chain = f.read()
