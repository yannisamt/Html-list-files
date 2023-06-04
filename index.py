import os

# Obtention du chemin du dossier courant
dossier_courant = os.getcwd()

# Liste des fichiers dans le dossier courant avec l'extension .txt
fichiers = [fichier for fichier in os.listdir(dossier_courant) if fichier.endswith('.txt')]

# Création du contenu de la page HTML
contenu_html = '''
<html>
<head>
<script>
var fichiers = [
'''
for fichier in fichiers:
    contenu_html += f'    "{fichier}",\n'
contenu_html += '''
];

function rechercher() {
    var saisie = document.getElementById("recherche").value.toLowerCase();
    if (saisie.length < 4) {
        return;
    }

    var correspondances = [];

    for (var i = 0; i < fichiers.length; i++) {
        if (fichiers[i].toLowerCase().includes(saisie)) {
            correspondances.push(fichiers[i]);
        }
    }

    var contenuPromises = correspondances.map(function(nom_fichier) {
        return fetch(nom_fichier)
            .then(function(response) {
                return response.text();
            });
    });

    Promise.all(contenuPromises)
        .then(function(contenus) {
            var contenu = "";
            for (var i = 0; i < contenus.length; i++) {
                contenu += "<p>" + contenus[i] + "</p>";
            }
            document.getElementById("contenu").innerHTML = contenu;
        })
        .catch(function(error) {
            console.error(error);
        });
}

</script>
</head>
<body>
<input type="text" id="recherche" placeholder="Rechercher...">
<button onclick="rechercher()">Valider</button>
<div id="contenu"></div>
</body>
</html>
'''

# Écriture du contenu dans un fichier HTML
with open('index.html', 'w') as fichier_html:
    fichier_html.write(contenu_html)
s