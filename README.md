## Ejecucion

Para poder levantar esta API se necesita abrir un terminal en el root de esta crpeta y correr los siguiente comandos

```bash
docker build -t api .

docker run -d -p 8000:8000 --name api api

```
> [!IMPORTANT]
> Nosotros assumimos que se tiene Docker Instalado

Si hay alguna necesidad de remover el contendor se usa este comando

```bash
docker rm -f api

```

Esto contenedor instalara los requerimientos necesarios

Para poder hacer uso de los endpoints se abrira una pagina en el navegador a esta direccion `http://localhost:8000/docs/` para poder usar el swagger de fastapi y probar cada enpoint.

## Notas y Obsevaciones

Para iniciar, me gustaría comentar que se creó esta API REST en FASTAPI, ya que es un framework basado en Python que facilita mucho y reduce el tiempo de creación de endpoints y microservicios. Además, es muy flexible al permitir configurar servicios, librerías, utilidades y configuraciones para adaptarse a cualquier necesidad del backend.

Aquí se crearon dos endpoints: el primero extrae un número de una lista de números del 1 al 100, y el otro genera una lista con los números extraídos. Todo esto se maneja en una clase que se inicializa con un constructor con los números de la lista inicial que se pide, y se llama a esta clase y a sus métodos dependiendo de la necesidad de los endpoints.

Por consistencia se crea un .gitignore al subir a un repo pero por ahora lo evitare ya que subire todos los archivos contenidos en al carpeta.