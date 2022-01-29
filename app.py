from typing import Optional, Awaitable

import tornado.ioloop as io_loop
import tornado.web as wb


class Controller(wb.RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        pass

    def get(self):
        self.write("Hello World")


def make_app():
    routes = [('/', Controller)]
    return wb.Application(routes)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    io_loop.IOLoop.current().start()
