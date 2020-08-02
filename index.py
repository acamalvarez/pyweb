import tornado.web
import tornado.ioloop

class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world! This is my first tornado tutorial.")

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.write("Querying tweet with id " + id)

class queryStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        n = int(self.get_argument("n"))
        r = "odd" if n % 2 else "even"

        self.write("the number " + str(n) + " is " + r)

class sumStringRequestHandler(tornado.web.RequestHandler):
    def get(self):
        x = int(self.get_argument("x"))
        y = int(self.get_argument("y"))

        result = str(x + y)

        self.write(str(x) + " + " + str(y) + " = " + result)

class staticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

def make_app():
    return tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/blog", staticRequestHandler),
        (r"/isEven", queryStringRequestHandler),
        (r"/tweet/([0-9]+)", resourceRequestHandler),
        (r"/sum", sumStringRequestHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8881)
    print("I'm listeing on port 8881")
    tornado.ioloop.IOLoop.current().start()
