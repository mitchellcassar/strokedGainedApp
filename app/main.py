from website import createApp

app = createApp()
app.config['SECURE_KEY'] = 'Super Secret Key'

if __name__ == '__main__':
    app.run(debug = True)


