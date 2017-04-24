#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 20:20:28 2017

@author: gabrielligeiro
"""
import json
import random
import critical

#importando os Inspermons
with open("inspermons.json", "r") as arquivo1:
    inspermons = json.load(arquivo1)
#MOSTRANDOS OS INSPERMONS
    
def mostra_ipmon(ipmon):
    print("Inspermon : {0}".format(ipmon["nome"])) 
    print("poder = {0}".format(ipmon["poder"])) 
    print("vida = {0}".format(ipmon["vida"])) 
    print("defesa = {0}".format(ipmon["defesa"]))
    print("tipo = {0}".format(ipmon["tipo"]))
    print("xp = {0}\n".format(ipmon["xp"]))

#Batalha (ACRESCENTAR texto de dano!)
def batalharound(vidaoponente,poderoponente,defesaoponente,vidajogador,poderjogador,defesajogador,critical,aleatoriomons,nomejogador,tipojogador,tipooponente):
    perguntaround = str(input("Você deseja batalhar com {0}?" .format(aleatoriomons["nome"])))
    perguntaround_lower = perguntaround.lower()
    while perguntaround_lower == "sim":
        print("A vida do seu {0} é:{1}".format(nomejogador,vidajogador))
        print("A vida do {0} é:{1}".format(aleatoriomons["nome"],vidaoponente))
        a = ( poderjogador*critical - defesaoponente)
        if tipojogador == "agua" and tipooponente == "fogo":
            a = a * 1.5
        if tipojogador == "fogo" and tipooponente == "ar":
            a = a * 1.5
        if tipojogador == "ar" and tipooponente == "terra":
            a = a * 1.5
        if tipojogador == "terra" and tipooponente == "agua":
            a = a * 1.5
        if a < 0:
            a = a * (-1)
        vidaoponente = vidaoponente - a
        if critical != 1:
            print("Seu Inspermon deu um dano critical !!")
        if vidaoponente <= 0:
            print ("O seu Inspermon ganhou a batalha!")
            return 1
        b = (poderoponente*critical - defesajogador)
        if tipooponente == "agua" and tipojogador == "fogo":
            b = b * 1.5
        if tipooponente == "fogo" and tipojogador == "ar":
            b = b * 1.5
        if tipooponente == "ar" and tipojogador == "terra":
            b = b * 1.5
        if tipooponente == "terra" and tipojogador == "agua":
            b = b * 1.5
        if b < 0:
            b = b * (-1)
        vidajogador = vidajogador - b
        if critical != 1:
            print ("Seu Inspermon sofreu um dano critical !!")
        
        print("A vida do seu {0} é:{1}".format(nomejogador,vidajogador))
        print("A vida do {0} é:{1}".format(aleatoriomons["nome"],vidaoponente))
        
        if vidajogador <= 0:
            print ("O seu Inspermon perdeu a batalha... D:")
            return 0
      
        
        perguntaround = str(input("Você deseja continuar batalhando com {0}?" .format(aleatoriomons["nome"])))
        perguntaround_lower = perguntaround.lower()
        
    return 2        
        
        
#mostrando o INSPERDEX       
def mostra_insperdex():
    print("A sua Insperdex tem o(s) senguinte(s) Inspermons: ")
    for i in range(len(insperdex)):
        mostra_ipmon(insperdex[i])
        
#CARREGANDO O JOGO
while True:    
    load = input("Você deseja carregar um save?")
    if load == "sim":
        with open("save_ep2.json","r") as arquivo:
            base_dados = json.load(arquivo)
            meuinspermon = base_dados[1]
            insperdex = base_dados[0]
            nomejogador = meuinspermon["nome"]
            vidajogador = meuinspermon["vida"]
            poderjogador = meuinspermon["poder"]
            defesajogador = meuinspermon["defesa"]
            xpjogador = meuinspermon["xp"]
            pikaxuXP = xpjogador
            tipojogador = meuinspermon["tipo"] 
            print("Seu pokemon é o {0}!".format(nomejogador))
            mostra_ipmon(meuinspermon)
            break
    else:
        #ESCOLHANDO UM INSPERMON PARA O JOGADOR!!!

        pokestatus = inspermons[0]
        nomejogador = pokestatus["nome"]
        print("Seu pokemon é o {0}!".format(nomejogador))
        vidajogador = pokestatus["vida"]
        poderjogador = pokestatus["poder"]
        defesajogador = pokestatus["defesa"]
        xpjogador = pokestatus["xp"]
        tipojogador = pokestatus["tipo"]
        pikaxuXP = xpjogador
        meuinspermonz = []
        meuinspermonz.append(pokestatus)
        meuinspermon = meuinspermonz[0]
        mostra_ipmon (pokestatus)
        break


#INSPERDEX
insperdex = []




#rodando o jogo
while True:
   
    
    pergunta = str(input("O que você deseja fazer? \n => Passear \n => Acessar Insperdex(insperdex) \n => Dormir \n"))
    perguntalower = pergunta.lower()
    
    #DORMIR
    if perguntalower == "dormir":
        save = input("Você deseja salvar o jogo?")
        if save == "sim":
            print("Salvando...!")
            dados = [insperdex,meuinspermon]
            with open("save_ep2.json","w") as arquivo:
                json.dump(dados, arquivo)
                break
        if save == "nao":
            print("Até a proxima!")
            break
    #LUTAR
    if perguntalower == "passear":
        print("Você encontrou um Inspermon!!!")
        #ESCOLHANDO UM INSPERMON ALEATORIAMENTE PARA BATALHA!!!
        aleatoriomons = random.choice(inspermons)
        #ADICIONAR O INSPERMON AO INSPERDEX!
        insperdex.append(aleatoriomons)
        
        #VOLTANDO A BATALHA
        
        aleatoriostatus = aleatoriomons
        vidaoponente = aleatoriostatus["vida"]
        poderoponente = aleatoriostatus["poder"]
        defesaoponente = aleatoriostatus["defesa"]
        tipooponente = aleatoriostatus["tipo"]
        #BATALHA!!!!!!!!!!
        resultado = batalharound (vidaoponente,poderoponente,defesaoponente,
                                  vidajogador,poderjogador,defesajogador, 
                                  critical.critical(),aleatoriomons,nomejogador,
                                  tipojogador,tipooponente)
        if resultado == 1:
          pikaxuXP = pikaxuXP + 1  
          if pikaxuXP % 3 == 0:
              defesajogador += 5
              poderjogador += 3
              vidajogador += 5
              meuinspermon["vida"]= vidajogador
              meuinspermon["poder"]= poderjogador
              meuinspermon["defesa"]= defesajogador
              meuinspermon["xp"] = pikaxuXP 
              
    #INSPERDEX
    if perguntalower == "insperdex":
        mostra_insperdex()
    
