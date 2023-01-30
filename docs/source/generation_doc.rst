Generation de la documentation
==============================

La documentation est généré à partir de fichier source ReStrucredText (fichier rst) sur le site Readthedocs.

Installation de sphinx
**********************

Installer les package anaconda:

- sphinx
- sphinx-rtd-theme

Configuration
*************
Dans un terminal il faut lancer la commande ::

    sphinx-quickstart docs


Génération
**********

Avant d'envoyer les sources sur le dépôt de code, il est possible de visualiser la documentation avec vscode.
Lancer la commande pour générer la documentation en local::

    sphinx-build.exe .\docs\source\ .\docs\build\

Il suffit d'ouvrir le fichier index.html avaec le raccourci [alt+L+O]

