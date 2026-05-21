# VotaDev 🗳️

O **VotaDev** é uma aplicação em Python desenvolvida para validar a elegibilidade eleitoral de um cidadão com base no seu ano de nascimento. O projeto nasceu como um desafio prático para consolidar conceitos de lógica de programação, manipulação de bibliotecas nativas, tratamento de erros e versionamento com Git/GitHub.

---

## 🚀 Status do Projeto & Roadmap

Atualmente, o projeto está na **Fase 1 (Versão de Terminal)**. O planejamento de evolução da aplicação está dividido nas seguintes etapas:

- [x] **Fase 1 (CLI):** Lógica principal via terminal, automação de data e tratamento de exceções.
- [ ] **Fase 2 (Web/Interface):** Criação de uma interface gráfica para o usuário utilizando **Flask** (HTML/CSS).
- [ ] **Fase 3 (Autenticação & Dados):** Implementação de sistema de **Login** para usuários e integração com **Banco de Dados** para salvar o histórico de consultas.

---

## 🛠️ Tecnologias e Ferramentas (Fase Inicial)

- **Python 3.14+** (Lógica de negócios)
- **Módulo `datetime`** (Para captura dinâmica do ano atual)
- **Git & GitHub** (Controle de versão e gerenciamento de tarefas via GitHub Projects)

---

## 🎯 Funcionalidades Atuais

- **Cálculo Dinâmico:** Calcula a idade exata do usuário sem depender de um ano fixado no código (sempre atualizado).
- **Tratamento de Erros (_Bulletproof_):** Proteção contra entradas inválidas utilizando blocos `try/except` (o programa não quebra se o usuário digitar letras ou caracteres especiais).
- **Validação Eleitoral:** Informa se o voto é proibido (menor de 16 anos), opcional (16, 17 ou acima de 70 anos) ou obrigatório (entre 18 e 70 anos).

---
