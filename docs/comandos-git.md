# Comandos aprendidos

### Novo repositório

1. Inicializar
    ```PowerShell
    git init
    ```

2. Adicionar arquivos 
    ```PowerShell
    git add .
    ```

3. Gravar alterações
    ```PowerShell
    git commit -m " "
    ```

4. Define a branch
    ```PowerShell
    git branch -M main
    ```

5. Conecta ao repositório (GitHub)
    ```PowerShell
    https://github.com/nanda-marques/exercicios-python.git
    ```

6. Envia os arquivos
    ```PowerShell
    git push -u origin main
    ```

### Remover (git add)
```PowerShell
git reset # nome_arquivo/nome_pasta
git reset # (remove todas adições)
```

### Remover pasta git (git Init)
```PowerShell
Remove-Item -Recurse -Force .git
```

## Gitignore 

Para evitar que pastas como `__pycache__` sejam versionado (na raiz ou em subpastas), adicione **/`__pycache__/` e `*.py[cod]` no arquivo `.gitignore`

Caso já tenham sido adicionadas e o Git ainda insista em rastreá-las por já estarem no histórico, execute 
```cmd
Get-ChildItem -Recurse -Filter "__pycache__" | ForEach-Object { git rm -r --cached $_.FullName }
```