#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:20:28 2017

@author: gabrielligeiro
"""
import json
import random


#importando os Inspermons
with open("inspermons.json", "r") as arquivo1:
    inspermons = json.load(arquivo1)

#MOSTRANDOS OS INSPERMONS
    
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"])) 
    print("poder = {0}".format(ipmon["poder"])) 
    print("vida = {0}".format(ipmon["vida"])) 
    print("defesa = {0}\n".format(ipmon["defesa"]))

#Batalha
def batalha(vidaoponente,poderoponente,defesaoponente,vidajogador,poderjogador,defesajogador):
    while vidajogador > 0 and vidaoponente > 0:
        vidaoponente = vidaoponente - ( poderjogador - defesaoponente)
        if vidaoponente <= 0:
            return print("Você gahou a batalha!")
        vidajogador = vidajogador - (poderoponente - defesajogador)
        if vidajogador <= 0:
            return print("Você perdeu!")

 #INSPERDEX
insperdex = []
#mostrando o INSPERDEX  (ESTA COM ERRO, SO PRINTA O PRIMEIRO)     
def mostra_insperdex():
    print("A sua Insperdex tem o(s) senguinte(s) Inspermons: ")
    for i in range(len(insperdex)):
        mostra_ipmon(insperdex[i])   
#ESCOLHANDO UM INSPERMON PARA O JOGADOR!!!

pokestatus = inspermons[0]
print("Seu pokemon é o {0}!".format(pokestatus["nome"]))
vidajogador = pokestatus["vida"]
poderjogador = pokestatus["poder"]
defesajogador = pokestatus["defesa"]



#rodando o jogo
while True:
    pergunta = str(input("Você deseja passear ou dormir ou acessar Insperdex? "))
    perguntalower = pergunta.lower()
    
    #DORMIR
    if perguntalower == "dormir":
        break
    #LUTAR
    if perguntalower == "passear":
        print("Você encontrou um Inspermon!!!")
        #ESCOLHANDO UM INSPERMON ALEATORIAMENTE PARA BATALHA!!!
        aleatoriomons = random.choice(inspermons)
        #ADICIONAR O INSPERMON AO INSPERDEX!
        insperdex.append(aleatoriomons)
        #BATALHAR OU NÃO BATALHAR, EIS A QUESTÃO
        
        fugir = str(input("Você deseja batalhar com {0}?" .format(aleatoriomons["nome"])))
        fugirlower = fugir.lower()
        #VOLTANDO A BATALHA
        if fugirlower == "sim":
            aleatoriostatus = aleatoriomons
            vidaoponente = aleatoriostatus["vida"]
            poderoponente = aleatoriostatus["poder"]
            defesaoponente = aleatoriostatus["defesa"]
            #BATALHA!!!!!!!!!!
            batalha (vidaoponente,poderoponente,defesaoponente,vidajogador,poderjogador,defesajogador)
            
        if fugirlower == "não":
            continue
        if fugirlower == "nao":
            continue
    #INSPERDEX
    if perguntalower == "insperdex":
        mostra_insperdex()

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        