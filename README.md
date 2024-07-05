# Sorting_App 2.0 - Flet
Requisitos:
flet==0.22.*

python 3.12*

Puede instalar python mediante el cmd (Windows)

```
winget install python
```
o en linux (Ubuntu, Debian ETC:)

```
sudo apt-get install python
```

Nota: para linux se deben realizar una preparación previa, para evitar errores de ejecución en el desarrollo:

A. Gstreamer para audio - Librerias completas
```
apt install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-doc gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio
```
B. MPV para video 

```
sudo apt install libmpv-dev mpv
```



Para poder ejecutar esta aplicacion como programador se debe considerar  preparar un entorno virtual para evitar descargar dependencias y tener problemas de mezca en las mismas, para esto se debe realizar lo siguiente:


1. Se establece un entorno virtual mediante venv


Windows
```
python -m venv .venv
```

Linux /Mac

```
python3 -m venv .venv
```



2. Se debe activar el entorno virtual:

Windows
```
.venv\Scripts\activate
```


Mac

```
source .venv/bin/activate
```

3. Se instala Flet mediante  la paqueteria de Python(PIP)
```
pip install flet
```

4. Para ejecutar la aplicacion en modo programador con salida por consola, debe ejecutar lo siguiente:

```
flet run
```

Nota: Se puede ejecutar la aplicacion en modo web, pero el modulo de carga del archivo txt, no funciona debido a que se requiere algunos ajustes adicionales, esto se hace  mediante el siguiente comando:

```
flet run --web --port puerto_de_su_preferencia
```

Puede acceder a la documentación mas detallada mediante el enlace: 
[text](https://flet.dev/docs/)