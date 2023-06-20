# Index

1. [English Version](#english-version)
    1. [What is this project?](#what-is-this-project)
    1. [What do i need to run this project?](#what-do-i-need-to-run-this-project)
    1. [How it works?](#how-it-works)
    1. [How to manage the domains i want to monitor](#how-to-manage-the-domains-i-want-to-monitor)
1. [Versão em Português](#versão-em-português)
    1. [O que é este projeto?](#o-que-é-este-projeto)
    1. [O que eu preciso para rodar esse projeto?](#o-que-eu-preciso-para-rodar-esse-projeto)
    1. [Como ele funciona?](#como-ele-funciona)
    1. [Como gerenciar os dominíos que eu vou monitorar](#how-to-manage-the-domains-i-want-to-monitor)

# What is this project?

This is a simple script with the purpose of getting the state of a domain on RegistroBr and notify the user when the renovation day comes.

# What do i need to run this project?

The libraries used on this project are:

- win10toast-click

# How it works?

This project works connecting to a RegistroBr API and verifying each domain on `src/data/input/domains.json`.

When you run `domainReminder.py` it wil create two files:

`src/data/input/renovation-dates.json` &rarr; Stores the renovation dates recovered from API (this file is like a cache for the script to work offline)

`src/data/output/delayed-domains.json` &rarr; Stores all domains expired with their renovation dates

# How to manage the domains i want to monitor?

To add a domain to the list of domains to be verified you just need to add a new line on `src/data/input/domain.json`

To remove a domain from the list of domains to be verified you just need to remove the domain line on `src/data/input/domain.json`

# **Versão em Português**


# O que é este projeto?

Este projeto é um script simples com o objetivo de obter o estado de um domínio no RegistroBr e notificar o usuário quando o dia da renovação chegar

# O que eu preciso para rodar este projeto?

As bibliotecas utilizadas neste projeto foram:

- win10toast-click

# Como ele funciona?

Este projeto funciona conectando-se com a API do RegistroBr e verificando cada domínio presente em `src/data/input/domains.json`

Quando você executa `domainReminder.py` ele vai criar dois arquivos:

`src/data/input/renovation-dates.json` &rarr; Armazena as datas de renovação recuperadas pela API (este arquivo é como um cache para o script poder funcionar offline)

`src/data/output/delayed-domains.json` &rarr; Armazena todos os domínios expirados com suas respectivas datas de renovação

# Como gerenciar os dominíos que eu vou monitorar?

Para adicionar um domínio na lista de domínios que serão verificados você só precisa editar o arquivo `src/data/input/domain.json` e lá adicionar uma nova linha com o seu domínio

Para remover um domínio da lista de domínios que serão verificados você só precisa remover a linha referente a ele em `src/data/input/domain.json`