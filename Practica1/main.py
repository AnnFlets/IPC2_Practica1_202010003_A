import xml.dom.minidom as MD
#Librería utilizada para la escritura del archivo XML
import xml.etree.cElementTree as ET
#TDA -> Pila
# En pila, el último que ingresa es el primero que sale
from Pila import Pila
from Elemento import Elemento

def lecturaYEscritura():
    try:
        # LECTURA DE XML
        ruta = input("Ingrese la ruta del archivo XML a leer:")
        # Se lee el archivo
        xml = MD.parse(ruta)

        juegosViejos = xml.getElementsByTagName("JuegosViejos")
        listaPlataformas = xml.getElementsByTagName("ListaPlataformas")
        listadoJuegos = xml.getElementsByTagName("ListadoJuegos")

        # PILA PLATAFORMAS
        pilaPlataformas = Pila()

        # Se recorre la lista de plataformas y se almacenan los atributos de código y nombre de cada una
        for listaPlataforma in listaPlataformas:
            plataforma = listaPlataforma.getElementsByTagName("Plataforma")
            for infoPlataforma in plataforma:
                codigoPlataforma = infoPlataforma.getElementsByTagName("codigo")[0]
                nombrePlataforma = infoPlataforma.getElementsByTagName("nombre")[0]
                elemento = Elemento(codigoPlataforma.firstChild.data, nombrePlataforma.firstChild.data)
                pilaPlataformas.push(elemento)

        # Ordenamos la pila de plataformas
        pilaPlataformas.ordenar()

        # PILA JUEGOS
        pilaJuegos = Pila()

        for listadoJuego in listadoJuegos:
            juego = listadoJuego.getElementsByTagName("Juego")
            for infoJuego in juego:
                codigoJuego = infoJuego.getElementsByTagName("codigo")[0]
                nombreJuego = infoJuego.getElementsByTagName("nombre")[0]
                elemento = Elemento(codigoJuego.firstChild.data, nombreJuego.firstChild.data)
                pilaJuegos.push(elemento)
                platforms = []
                plataformasJ = infoJuego.getElementsByTagName("Plataformas")
                for plataformaJ in plataformasJ:
                    plataformaGame = infoJuego.getElementsByTagName("Plataforma")
                    for plataformaJuego in plataformaGame:
                        codigoPlataformaJuego = plataformaJuego.getElementsByTagName("codigo")[0]
                        platforms.append(codigoPlataformaJuego.firstChild.data)
                        elemento.asignarPlataforma(platforms)

        # Ordenamos la pila de juegos
        pilaJuegos.ordenar()

        # ESCRITURA DE XML
        # Creamos una etiqueta o elemento
        juegosViejos = ET.Element("JuegosViejos")
        # Creamos una sub-etiqueta o sub-elemento de un elemento mayor en jerarquía
        lstaPlata = ET.SubElement(juegosViejos, "ListaPlataformas")
        for i in range(len(pilaPlataformas.elementos)):
            plataforma = ET.SubElement(lstaPlata, "Plataforma")
            elementoListaOrd = pilaPlataformas.pop()
            ET.SubElement(plataforma, "codigo").text = elementoListaOrd.obtenerCodigo()
            ET.SubElement(plataforma, "nombre").text = elementoListaOrd.obtenerNombre()
        listadoJuegos = ET.SubElement(juegosViejos, "ListadoJuegos")
        for i in range(len(pilaJuegos.elementos)):
            juego = ET.SubElement(listadoJuegos, "Juego")
            elementoJuegoOrd = pilaJuegos.pop()
            ET.SubElement(juego, "codigo").text = elementoJuegoOrd.obtenerCodigo()
            ET.SubElement(juego, "nombre").text = elementoJuegoOrd.obtenerNombre()
            plataformasJ = ET.SubElement(juego, "Plataformas")
            for plataform in elementoJuegoOrd.obtenerPlataformas():
                plataformaJ = ET.SubElement(plataformasJ, "Plataforma")
                ET.SubElement(plataformaJ, "codigo").text = plataform
        # Se escribe dentro del parámetro la etiqueta o elemento raíz del árbol
        archivo = ET.ElementTree(juegosViejos)
        # Se crea el archivo XML
        archivo.write("escritura.xml")

        # Indentar las etiquetas del XML
        archivoXML = 'escritura.xml'
        docxml = ET.parse(archivoXML)
        raiz = docxml.getroot()
        xmlTextoOrdenado = MD.parseString(ET.tostring(raiz)).toprettyxml()

        # Sobreescribir el archivo xml para que aparezca con los saltos de línea e indentado
        file = open("escritura.xml", "w+")
        file.write(xmlTextoOrdenado)
        file.close()
        print("¡Archivo ordenado con éxito! :D")

    except:
        print("[ERROR]: Archivo no encontrado")

if __name__ == '__main__':
    lecturaYEscritura()