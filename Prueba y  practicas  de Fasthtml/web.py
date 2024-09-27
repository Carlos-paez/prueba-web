from fasthtml.common import *
app,rt = fast_app()
@rt('/')
def get(): return Div(P('Hola josé'), hx_get="/change")
@rt('/change')
def get(): return P('esto es FastHTML en Python :)')
serve()