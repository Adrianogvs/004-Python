# Guia Básico de Git e GitHub

## Introdução
Git é um sistema de controle de versão distribuído que permite rastrear alterações no código-fonte durante o desenvolvimento de software. Já o GitHub é uma plataforma baseada em Git para hospedagem de código e colaboração entre desenvolvedores.

---

## 1. Criando e Clonando Repositórios
- **Criar um repositório local:**
  ```sh
  git init
  ```
- **Clonar um repositório existente:**
  ```sh
  git clone <URL_DO_REPOSITORIO>
  ```

---

## 2. Salvando Alterações no Repositório Local
- **Adicionar arquivos ao controle de versão:**
  ```sh
  git add <arquivo>
  ```
- **Fazer um commit das mudanças:**
  ```sh
  git commit -m "Mensagem descritiva da alteração"
  ```

---

## 3. Desfazendo Alterações no Repositório Local
- **Descartar mudanças em um arquivo modificado:**
  ```sh
  git checkout -- <arquivo>
  ```
- **Remover arquivos do staging:**
  ```sh
  git reset HEAD <arquivo>
  ```
- **Resetar completamente as mudanças:**
  ```sh
  git reset --hard
  ```

---

## 4. Enviando e Baixando Alterações com o Repositório Remoto
- **Enviar commits para o repositório remoto:**
  ```sh
  git push origin <branch>
  ```
- **Baixar e aplicar mudanças do repositório remoto:**
  ```sh
  git pull origin <branch>
  ```
- **Baixar mudanças sem aplicar automaticamente:**
  ```sh
  git fetch
  ```

---

## 5. Trabalhando com Branches
- **Criar uma nova branch:**
  ```sh
  git branch <nome-da-branch>
  ```
- **Mudar para uma branch existente:**
  ```sh
  git checkout <nome-da-branch>
  ```
- **Criar e mudar para uma nova branch:**
  ```sh
  git checkout -b <nome-da-branch>
  ```
- **Mesclar uma branch na branch atual:**
  ```sh
  git merge <nome-da-branch>
  ```
- **Deletar uma branch local:**
  ```sh
  git branch -d <nome-da-branch>
  ```

---

## 6. Comandos Úteis no Dia a Dia
- **Listar todas as branches:**
  ```sh
  git branch
  ```
- **Exibir um histórico visual das branches:**
  ```sh
  git log --oneline --graph
  ```
- **Rebasear commits de outra branch:**
  ```sh
  git rebase <nome-da-branch>
  ```

---

## Conclusão
O uso do Git e GitHub permite um controle eficiente das versões do código, colaboração remota e rastreamento de mudanças. Praticar esses comandos diariamente ajuda a melhorar a fluência no uso dessas ferramentas essenciais para desenvolvimento de software.

