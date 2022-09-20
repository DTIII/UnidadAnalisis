from django.shortcuts import render
from django.http import HttpResponse
from .models import sqlServerConn
# Create your views here.

import pyodbc

def Index(request):
     conn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.10.11.196,1485;DATABASE=UnidadAnalasis;UID=MALTAX;PWD=MALTAX')
     cursor = conn.cursor()
     cursor.execute('select * from C_Oxxos')
     resultado=cursor.fetchall()
     return render(request, 'oxxo/index.html',{'sqlServerConn':resultado})