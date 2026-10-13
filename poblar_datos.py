import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'inmorent_project.settings')
django.setup()

from inmobiliaria.models import Comuna, Propiedad

print("Limpiando registros antiguos...")
# Esto borra todo lo anterior para que solo queden las nuevas comunas y propiedades
Propiedad.objects.all().delete()
Comuna.objects.all().delete()

print("Iniciando carga de datos de Osorno...")

# 1. Crear las comunas/sectores de Osorno
comuna1 = Comuna.objects.create(
    codigo_clasificacion='COM-FRAN',
    nombre='Francke',
    region='Región de Los Lagos',
    activa=True
)

comuna2 = Comuna.objects.create(
    codigo_clasificacion='COM-OVE',
    nombre='Ovejería',
    region='Región de Los Lagos',
    activa=True
)

comuna3 = Comuna.objects.create(
    codigo_clasificacion='COM-PORT',
    nombre='Portal Osorno',
    region='Región de Los Lagos',
    activa=True
)

print("Sectores de Osorno creados exitosamente.")

# 2. Tus propiedades personalizadas de Osorno
propiedades_data = [
    # Francke (4)
    {'codigo': 'PROP-001', 'dir': 'Los Piñones 1542', 'tipo': 'CASA', 'precio': 450000, 'dorm': 3, 'banos': 2, 'disp': True, 'comuna': comuna1},
    {'codigo': 'PROP-002', 'dir': 'Los Abedules 453', 'tipo': 'DEPARTAMENTO', 'precio': 350000, 'dorm': 2, 'banos': 1, 'disp': True, 'comuna': comuna1},
    {'codigo': 'PROP-003', 'dir': 'Av. Héroes de la Concepción 789', 'tipo': 'CASA', 'precio': 500000, 'dorm': 3, 'banos': 2, 'disp': False, 'comuna': comuna1},
    {'codigo': 'PROP-004', 'dir': 'Los Cafetales 123', 'tipo': 'OFICINA', 'precio': 400000, 'dorm': 1, 'banos': 1, 'disp': True, 'comuna': comuna1},
    
    # Ovejería (4)
    {'codigo': 'PROP-005', 'dir': 'Felizardo Azenjo 98', 'tipo': 'CASA', 'precio': 320000, 'dorm': 2, 'banos': 1, 'disp': True, 'comuna': comuna2},
    {'codigo': 'PROP-006', 'dir': 'Av. Tratado de la Paz de las Canoas 54', 'tipo': 'DEPARTAMENTO', 'precio': 300000, 'dorm': 1, 'banos': 1, 'disp': True, 'comuna': comuna2},
    {'codigo': 'PROP-007', 'dir': 'Pangue 678', 'tipo': 'CASA', 'precio': 480000, 'dorm': 3, 'banos': 2, 'disp': False, 'comuna': comuna2},
    {'codigo': 'PROP-008', 'dir': 'Capullo 15', 'tipo': 'OFICINA', 'precio': 450000, 'dorm': 2, 'banos': 1, 'disp': True, 'comuna': comuna2},
    
    # Portal Osorno (2)
    {'codigo': 'PROP-009', 'dir': 'Moraleda 921', 'tipo': 'CASA', 'precio': 550000, 'dorm': 2, 'banos': 2, 'disp': True, 'comuna': comuna3},
    {'codigo': 'PROP-010', 'dir': 'Bahía Pargua 3987', 'tipo': 'OFICINA', 'precio': 650000, 'dorm': 1, 'banos': 2, 'disp': True, 'comuna': comuna3},
]

for p in propiedades_data:
    Propiedad.objects.create(
        codigo_propiedad=p['codigo'],
        direccion=p['dir'],
        tipo_propiedad=p['tipo'],
        precio_arriendo=p['precio'],
        dormitorios=p['dorm'],
        banos=p['banos'],
        disponible=p['disp'],
        comuna=p['comuna']
    )

print("¡Las 10 propiedades de Osorno se han creado exitosamente y sin registros antiguos!")