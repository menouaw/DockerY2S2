## Registre Docker Miroir - Guide rapide

### Objectif
Ce registre miroir permet de contourner les limitations de téléchargement (40 pulls/h/ip) imposées par Docker Hub pour les utilisateurs non authentifiés.

### Utilisation

#### Images officielles
```bash
# Au lieu de:
docker pull nginx

# Utilisez:
docker pull registry.nospy.fr/library/nginx
```

#### Images non officielles
```bash
# Au lieu de:
docker pull bitnami/wordpress

# Utilisez:
docker pull registry.nospy.fr/bitnami/wordpress
```

#### Exécution de conteneurs
```bash
docker run -d registry.nospy.fr/library/nginx
```

#### Si vous rencontrez l'erreur "rate limit exceeded"
C'est exactement pourquoi ce registre existe ! Modifiez simplement votre commande pour utiliser notre registre comme indiqué ci-dessus.