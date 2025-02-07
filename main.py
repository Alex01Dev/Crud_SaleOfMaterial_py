'''
Main starts the app and fetches the endpoints.
'''

from fastapi import FastAPI
from routes.usersRoutes import user
from routes.materialRoutes import material
from routes.loanRoutes import loans
app = FastAPI(
    title="Prestamos Amauri S.A de C.V",
    description="API de prueba para registrar de prestamo de material educativo"
)

app.include_router(user)
app.include_router(material)
app.include_router(loans)
