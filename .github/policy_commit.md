# Policy de commit

## Format

```
<type>(<scope>): <description>
```

- **type** : obligatoire, voir liste ci-dessous
- **scope** : optionnel, module/partie concernée (ex: `cli`, `ci`, `bot`)
- **description** : à l'impératif, minuscule, pas de point final

## Types

- `feat!` : nouvelle fonctionnalité
- `fix` : correction de bug
- `refactor` : changement de code sans impact fonctionnel
- `docs` : documentation uniquement
- `test` : ajout/modif de tests
- `ci` : pipeline CI/CD

## Règles

1. Une ligne de résumé (72 caractères max)
2. Un commit = un changement logique
3. Description claire, pas de "fix stuff" ou "update"
4. Corps du message (optionnel) séparé par une ligne vide, explique le *pourquoi*
5. Pas d'emoji, pas de ponctuation superflue

## Exemples

```
feat(cli): add boot animation with rich progress bar
fix(ci): correct rsync path in sync workflow
refactor(bot): extract command handlers into separate module
docs: add setup instructions for devenv
chore: bump python dependencies
```

## Breaking changes

Ajouter `!` après le type/scope et expliquer dans le corps :

```
feat!: change config format from json to toml

Migration nécessaire, voir CHANGELOG.md
```